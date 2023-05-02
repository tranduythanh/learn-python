import re
import numpy as np
from sympy import symbols

class LPP:
    def __init__(self):
        self.Coeff_C = []
        self.Objective = ''
        self.Coeff_A = []
        self.Coeff_B = []
        self.Sign_A = []

    def read_problem(self, file_name):
        # In ra dòng chữ "Linear programming problem:".
        print('Linear programming problem:')
        # Gọi hàm read_file() để đọc dữ liệu từ file và lưu vào biến data.
        data = self.read_file(file_name)
        # Tính số lượng hàng của ma trận hệ số ràng buộc bằng cách lấy chiều dài của data trừ 2 và lưu vào biến n.
        n = len(data) - 2
        # Gọi hàm find_max_variable_index() để tìm chỉ số biến lớn nhất trong dữ liệu và lưu vào biến max_variable_index.
        max_variable_index = self.find_max_variable_index(data)
        # Gọi hàm parse_coeff_C() để phân tích hệ số của hàm mục tiêu từ dòng đầu tiên của data và lưu vào thuộc tính self.Coeff_C.
        self.parse_coeff_C(data[0], max_variable_index)
        # Lưu giá trị cuối cùng của dòng đầu tiên trong data (đây là hàm mục tiêu 'Min' hoặc 'Max') vào thuộc tính self.Objective.
        self.Objective = data[0][-1]
        # Lấy các dòng từ dữ liệu data từ vị trí thứ nhất đến vị trí n+1 và lưu vào biến A.
        A = data[1:n + 1]
        # Gọi hàm parse_data() để phân tích ma trận hệ số ràng buộc và các giá trị bên phải của các ràng buộc từ A.
        self.parse_data(A, max_variable_index)

    # Mở file với tên file_name ở chế độ đọc ('r') và gán vào biến f.
    # Đọc từng dòng của file, tách các từ trong mỗi dòng và lưu kết quả vào biến data.
    # In nội dung của từng dòng trong data.
    # Trả về giá trị của biến data.
    def read_file(self, file_name):
        with open(file_name, 'r') as f:
            data = [line.split() for line in f]
            for line in data:
                print(' '.join(line))
        return data

    # Khởi tạo giá trị lớn nhất của chỉ số biến là 0 và lưu vào biến max_index.
    # Duyệt qua từng dòng trong dữ liệu data:
    # a. Duyệt qua từng phần tử s trong dòng đó.
    # b. Kiểm tra nếu 'x' không nằm trong s, tiếp tục vòng lặp với phần tử tiếp theo.
    # c. Gọi hàm self.var_index(s) và lưu kết quả vào biến n.
    # d. Kiểm tra nếu n là None, tiếp tục vòng lặp với phần tử tiếp theo.
    # e. Nếu n lớn hơn max_index, cập nhật max_index bằng giá trị của n.
    # Trả về giá trị của biến max_index.
    def find_max_variable_index(self, data):
        max_index = 0
        for line in data:
            for s in line:
                if 'x' not in s:
                    continue
                n = self.var_index(s)
                if n is None:
                    continue
                if n > max_index:
                    max_index = n
        return max_index

    # Khai báo mẫu regex pattern để tìm kiếm các chuỗi có dạng 'x' kèm theo một dãy số.
    # Tìm kiếm chuỗi phù hợp với pattern trong chuỗi mono và lưu kết quả vào biến result.
    # Kiểm tra nếu result là None hoặc rỗng, trả về None.
    # Lấy nhóm kết quả thứ nhất (dãy số sau 'x') từ result và chuyển đổi thành số nguyên, sau đó trả về kết quả.
    def var_index(self, mono):
        pattern = r'x(\d+)'
        result = re.search(pattern, mono)
        if result is None or result == '':
            return None
        digits = int(result.group(1))
        return int(digits)
    
    # Gọi hàm var_index() với đầu vào là mono và lưu kết quả vào biến index.
    # Kiểm tra nếu index là None, trả về None.
    # Tách hệ số từ chuỗi mono bằng cách tách chuỗi theo ký tự 'x', lấy phần tử đầu tiên, thay thế ký tự '*' bằng rỗng và chuyển đổi thành số thực, sau đó lưu vào biến coeff.
    # Trả về một tuple chứa index và coeff.
    def parse_coeff_index(self, mono):
        index = self.var_index(mono)
        if index is None:
            return None
        coeff = float(mono.split('x')[0].replace('*', ''))
        return index, coeff

    # Tạo một danh sách coeff_C1 từ dòng row, loại bỏ các ký tự '+'.
    # Khởi tạo một từ điển rỗng coeff_C_dict để lưu các hệ số của hàm mục tiêu.
    # Duyệt qua từng phần tử s trong danh sách coeff_C1:
    # a. Gọi hàm parse_coeff_index() với đầu vào là s và lưu kết quả vào các biến index và coeff.
    # b. Thêm cặp khóa-giá trị (index, coeff) vào từ điển coeff_C_dict.
    # Tạo danh sách self.Coeff_C từ từ điển coeff_C_dict với các chỉ số biến từ 1 đến max_variable_index, lấy giá trị hệ số tương ứng hoặc 0 nếu không có hệ số cho chỉ số đó.
    def parse_coeff_C(self, row, max_variable_index):
        coeff_C1 = [c for c in row[:-2] if c != '+']
        coeff_C_dict = {}
        for s in coeff_C1:
            index, coeff = self.parse_coeff_index(s)
            coeff_C_dict[index] = coeff
        self.Coeff_C = [coeff_C_dict.get(i, 0) for i in range(1, max_variable_index + 1)]

    # Duyệt qua từng dòng row trong ma trận A:
    # a. Tạo danh sách coeff_A1 từ dòng row, loại bỏ các ký tự '+'.
    # b. Khởi tạo một từ điển rỗng coeff_A_dict để lưu các hệ số của hàm ràng buộc.
    # c. Duyệt qua từng phần tử s trong danh sách coeff_A1:
    # i. Gọi hàm parse_coeff_index() với đầu vào là s và lưu kết quả vào các biến index và coeff.
    # ii. Thêm cặp khóa-giá trị (index, coeff) vào từ điển coeff_A_dict.
    # d. Thêm danh sách các hệ số vào self.Coeff_A từ từ điển coeff_A_dict với các chỉ số biến từ 1 đến max_variable_index, lấy giá trị hệ số tương ứng hoặc 0 nếu không có hệ số cho chỉ số đó.
    # e. Thêm giá trị phần tử cuối cùng của dòng row vào self.Coeff_B.
    # f. Thêm phần tử kế cuối của dòng row vào self.Sign_A.
    def parse_data(self, A, max_variable_index):
        for row in A:
            coeff_A1 = [s for s in row[:-2] if s != '+']
            coeff_A_dict = {}
            for s in coeff_A1:
                index, coeff = self.parse_coeff_index(s)
                coeff_A_dict[index] = coeff
            self.Coeff_A.append([coeff_A_dict.get(i, 0) for i in range(1, max_variable_index + 1)])
            self.Coeff_B.append(row[-1])
            self.Sign_A.append(row[-2])

    # In ra chuỗi 'Canonical form:'.
    # Chuyển đổi self.Coeff_A, self.Coeff_B, self.Coeff_C thành mảng numpy với kiểu dữ liệu là float và lưu vào các biến A_CT, B_CT, C_CT.
    # Gọi hàm generate_canonical_coefficients() với đầu vào là A_CT và C_CT, lưu kết quả trả về vào các biến A_CT, C_CT.
    # Gọi hàm print_objective_function() với đầu vào là C_CT để in hàm mục tiêu.
    # Gọi hàm print_constraints() với đầu vào là A_CT và B_CT để in các hàm ràng buộc.
    # Gọi hàm print_variable_constraints() với đầu vào là số lượng biến để in ràng buộc của các biến.
    def canonical_form(self):
        print('Canonical form:')
        A_CT = np.array(self.Coeff_A, dtype=float)
        B_CT = np.array(self.Coeff_B, dtype=float)
        C_CT = np.array(self.Coeff_C, dtype=float)
        A_CT, C_CT = self.generate_canonical_coefficients(A_CT, C_CT)
        self.print_objective_function(C_CT)
        self.print_constraints(A_CT, B_CT)
        self.print_variable_constraints(len(C_CT))

    # Phương thức generate_canonical_coefficients này thực hiện chuyển đổi các hệ số và ma trận hệ số của hàm mục tiêu và các ràng buộc của bài toán tối ưu hóa tuyến tính ban đầu sang dạng chuẩn (canonical form). Để làm điều này, nó thêm các biến slack cho các ràng buộc và điều chỉnh hàm mục tiêu nếu cần thiết (nhân với -1 nếu là bài toán tối đa hóa).
    # 
    # Thao tác gồm:
    # 
    # Duyệt qua từng phần tử sign của self.Sign_A với chỉ số i:
    # a. Khởi tạo mảng numpy slack_vars có kích thước (len(self.Sign_A), 1), kiểu dữ liệu float và các giá trị bằng 0.
    # b. Nếu sign là '<=', gán giá trị 1 cho phần tử thứ i của slack_vars.
    # c. Nếu sign là '>=', gán giá trị -1 cho phần tử thứ i của slack_vars.
    # d. Nối cột slack_vars vào ma trận A_CT.
    # Tính số cột còn thiếu trong ma trận A_CT so với số cột của ma trận C_CT và lưu vào biến n.
    # Nối n cột có giá trị 0 vào ma trận C_CT.
    # Nếu hàm mục tiêu là 'Max', nhân ma trận C_CT với -1.
    # Trả về A_CT và C_CT.
    def generate_canonical_coefficients(self, A_CT, C_CT):
        for i, sign in enumerate(self.Sign_A):
            slack_vars = np.zeros((len(self.Sign_A), 1), dtype=float)
            if sign == '<=':
                slack_vars[i] = 1
            elif sign == '>=':
                slack_vars[i] = -1
            A_CT = np.hstack((A_CT, slack_vars))
        n = A_CT.shape[1] - C_CT.shape[0]
        C_CT = np.hstack((C_CT, np.zeros(n, dtype=float)))
        if self.Objective == 'Max':
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

if __name__ == "__main__":
    file_name = 'problem.txt'
    lpp = LPP()
    lpp.read_problem(file_name)
    lpp.canonical_form()