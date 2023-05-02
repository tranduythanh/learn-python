import re
import numpy as np
from sympy import symbols
import lpp

class LinearTransform:
    def __init__(self, file_name):
        p = lpp.LPP()
        p.read_problem(file_name)
        self.LPP = p

    def convert_to_dual(self):
        transposed_constraints = np.transpose(self.LPP.Coeff_A)
        print('Dual problem is:')
        self.print_dual_objective()
        self.print_dual_constraints(transposed_constraints)
        self.print_dual_variable_constraints()

    def print_dual_objective(self):
        dual_objective = 'Max' if self.LPP.Objective == 'Min' else 'Min'
        F = "f(y) = " + " + ".join([f"{b}*y{j+1}" for j, b in enumerate(self.LPP.Coeff_B)]) + f" ---> {dual_objective}"
        print(F)

    def print_dual_constraints(self, transposed_constraints):
        for i, c in enumerate(self.LPP.Coeff_C):
            PT = " + ".join([f"{transposed_constraints[i][j]}*Y{j+1}" for j in range(len(self.LPP.Coeff_B))])
            inequality = "<=" if self.LPP.Objective == 'Min' else ">="
            print(f'\t {PT} {inequality} {c}')

    def print_dual_variable_constraints(self):
        dual_signs = [('<=' if d == '>=' else ('>=' if d == '<=' else '=<>E')) for d in self.LPP.Sign_A]
        if self.LPP.Objective == 'Max':
            dual_signs = [('<=' if d == '>=' else ('>=' if d == '<=' else '=<>E')) for d in self.LPP.Sign_A]

        variables = ', '.join([f'y{j+1}{dual_signs[j]}0' for j in range(len(self.LPP.Coeff_B))]) + '.'
        print('\t', variables)

    
    

    # In ra chuỗi 'Canonical form:'.
    # Chuyển đổi self.Coeff_A, self.Coeff_B, self.Coeff_C thành mảng numpy với kiểu dữ liệu là float và lưu vào các biến A_CT, B_CT, C_CT.
    # Gọi hàm generate_canonical_coefficients() với đầu vào là A_CT và C_CT, lưu kết quả trả về vào các biến A_CT, C_CT.
    # Gọi hàm print_objective_function() với đầu vào là C_CT để in hàm mục tiêu.
    # Gọi hàm print_constraints() với đầu vào là A_CT và B_CT để in các hàm ràng buộc.
    # Gọi hàm print_variable_constraints() với đầu vào là số lượng biến để in ràng buộc của các biến.
    def canonical_form(self):
        print('Canonical form:')
        A_CT = np.array(self.LPP.Coeff_A, dtype=float)
        B_CT = np.array(self.LPP.Coeff_B, dtype=float)
        C_CT = np.array(self.LPP.Coeff_C, dtype=float)
        A_CT, C_CT = self.generate_canonical_coefficients(A_CT, C_CT)
        A_CT, C_CT = self.simplify_canonical_coefficients(A_CT, C_CT)
        self.print_objective_function(C_CT)
        self.print_constraints(A_CT, B_CT)
        self.print_variable_constraints(len(C_CT))

    def simplify_canonical_coefficients(self, A_CT, C_CT):
        # Tìm các cột trong A_CT có tất cả các phần tử bằng 0
        zero_columns = np.all(A_CT == 0, axis=0)
        
        # Tìm các cột trong A_CT có ít nhất một phần tử khác 0
        non_zero_columns = np.logical_not(zero_columns)
        
        # Tìm các phần tử trong C_CT không bằng 0
        corresponding_C_CT = (C_CT != 0)

        # Kết hợp hai điều kiện: các cột không chứa toàn số 0 trong A_CT hoặc các phần tử không bằng 0 trong C_CT
        columns_to_keep = np.logical_or(non_zero_columns, corresponding_C_CT)

        # Loại bỏ các cột trong A_CT không thỏa mãn điều kiện
        A_CT_simplified = A_CT[:, columns_to_keep]
        
        # Loại bỏ các phần tử trong C_CT không thỏa mãn điều kiện
        C_CT_simplified = C_CT[columns_to_keep]

        # Trả về A_CT và C_CT sau khi được đơn giản hóa
        return A_CT_simplified, C_CT_simplified

    # Phương thức generate_canonical_coefficients này thực hiện chuyển đổi các hệ số và ma trận hệ số của hàm mục tiêu và các ràng buộc của bài toán tối ưu hóa tuyến tính ban đầu sang dạng chuẩn (canonical form). Để làm điều này, nó thêm các biến slack cho các ràng buộc và điều chỉnh hàm mục tiêu nếu cần thiết (nhân với -1 nếu là bài toán tối đa hóa).
    # 
    # Thao tác gồm:
    # 
    # Duyệt qua từng phần tử sign của self.LPP.Sign_A với chỉ số i:
    # a. Khởi tạo mảng numpy slack_vars có kích thước (len(self.LPP.Sign_A), 1), kiểu dữ liệu float và các giá trị bằng 0.
    # b. Nếu sign là '<=', gán giá trị 1 cho phần tử thứ i của slack_vars.
    # c. Nếu sign là '>=', gán giá trị -1 cho phần tử thứ i của slack_vars.
    # d. Nối cột slack_vars vào ma trận A_CT.
    # Tính số cột còn thiếu trong ma trận A_CT so với số cột của ma trận C_CT và lưu vào biến n.
    # Nối n cột có giá trị 0 vào ma trận C_CT.
    # Nếu hàm mục tiêu là 'Max', nhân ma trận C_CT với -1.
    # Trả về A_CT và C_CT.
    def generate_canonical_coefficients(self, A_CT, C_CT):
        for i, sign in enumerate(self.LPP.Sign_A):
            slack_vars = np.zeros((len(self.LPP.Sign_A), 1), dtype=float)
            if sign == '<=':
                slack_vars[i] = 1
            elif sign == '>=':
                slack_vars[i] = -1
            A_CT = np.hstack((A_CT, slack_vars))
        n = A_CT.shape[1] - C_CT.shape[0]
        C_CT = np.hstack((C_CT, np.zeros(n, dtype=float)))
        if self.LPP.Objective == 'Max':
            C_CT = -1 * C_CT
        return A_CT, C_CT

    def print_objective_function(self, C_CT):
        x_vars = symbols(f"x:{len(C_CT)+1}")[1:]
        F = "f(x) = " + ' + '.join([f"{C_CT[i]:.1f}*{x_vars[i]}" for i in range(len(C_CT)) if C_CT[i] != 0]) + f" ---> Min"
        print(F)

    def print_constraints(self, A_CT, B_CT):
        x_vars = symbols(f"x:{A_CT.shape[1]+1}")[1:]
        for i, b in enumerate(B_CT):
            constraint = ' + '.join([f"{A_CT[i, j]:.1f}*{x_vars[j]}" for j in range(A_CT.shape[1]) if A_CT[i, j] != 0]) + f" = {b:.1f}"
            print('\t', constraint)

    def print_variable_constraints(self, num_vars):
        x_vars = symbols(f"x:{num_vars+1}")[1:]
        constraints = ', '.join([f"{x_vars[i]}>=0" for i in range(num_vars)]) + '.'
        print('\t', constraints)


if __name__ == '__main__':
    file_name = 'problem.txt'
    linear_transform = LinearTransform(file_name)
    linear_transform.convert_to_dual()
    linear_transform.canonical_form()
