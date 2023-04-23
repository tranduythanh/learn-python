import numpy as np
import re
from prettytable import PrettyTable, ALL
from colorama import Fore, Back, Style


class AlgoParams:
    def __init__(self, u_size, v_size):
        self.u = np.empty(u_size)
        self.v = np.empty(v_size)
        self.u[:] = np.nan
        self.v[:] = np.nan
        self.u[0] = 0
        self.delta = np.empty((u_size, v_size))
        self.delta[:] = np.nan
        self.delta_max = np.nan
        self.delta_max_pos = (np.nan, np.nan)
        self.theta_min = np.nan
        self.theta_min_pos = (np.nan, np.nan)
        self.cycle = []
        self.cycle_mat = np.empty((u_size, v_size))


class TransProb:
    def __init__(self, supply, demand, cost):
        self.supply = supply
        self.demand = demand
        self.cost = cost
        self.steps = []


    def _nan_indice(self, list):
        ret = []
        for i in range(len(list)):
            if np.isnan(list[i]):
                ret.append(i)
        return ret
    

    def _cell_value(self, cell_allocation, cell_cost, cell_delta, cell_cycle, color=True):
        begin = ''
        end = ''
        if color:
            begin = Back.GREEN+Fore.BLACK
            end = Style.RESET_ALL
        if np.isnan(cell_allocation):
            background = ''
            begin = Fore.GREEN
            end = Fore.RESET
            cell_allocation = ''
            begin = ''
            end = ''
        else:
            cell_allocation = int(cell_allocation)

        cycle_str = ''
        if cell_cycle == 1:
            cycle_str = '    (+)'
        elif cell_cycle == -1:
            cycle_str = '    (-)'
        else:
            cycle_str = '       '
 
        if cell_delta is None:
            cell_delta = ''

        s = '({})      {:4}\n\n{}\n\n{}{}{}'.format(cell_cost, cell_delta, cycle_str, begin, cell_allocation, end)
        return s


    def total_cost(self, allocation):
        a = allocation.copy()
        a[np.isnan(a)] = 0
        return np.sum(a*self.cost)
    

    def table_string(self, allocation, algo_params=None, color=True):
        # create a table object
        table = PrettyTable()
        table.header = False
        table.hrules = ALL
        table.top_left_junction_char = '┌'
        table.top_right_junction_char = '┐'
        table.bottom_right_junction_char = '┘'
        table.bottom_left_junction_char = '└'
        table.vertical_char = '│'
        table.horizontal_char = '─'
        table.right_junction_char = '┤'
        table.left_junction_char = '├'
        table.top_junction_char = '┬'
        table.bottom_junction_char = '┴'
        table.junction_char = '┼'
        table.align = 'l'

        first_cell = '\\  b_j\n  \\\na_i \\'
        last_cell = '\\  u_i\n  \\\nv_j \\'

        first_row = [first_cell] + self.demand.tolist()
        if algo_params is not None:
            first_row += ['']
        table.add_row(first_row)
        
        # add rows to the table
        for i in range(len(allocation)):
            row = []
            row.append(self.supply[i])
            for k in range(len(allocation[i])):
                cell_delta = None
                cycle_mat_cell = None
                if algo_params is not None:
                    cycle_mat_cell = algo_params.cycle_mat[i, k]
                    cell_delta = algo_params.delta[i, k]
                    if cell_delta > 0:
                        cell_delta = str(cell_delta)
                        if color:
                            cell_delta = Fore.CYAN+cell_delta+Fore.RESET
                row.append(self._cell_value(allocation[i, k], self.cost[i, k], cell_delta, cycle_mat_cell, color))
            if algo_params is not None:
                row.append(algo_params.u[i])
            table.add_row(row)
        if algo_params is not None:
            v  = ['']+algo_params.v[:].tolist()+[last_cell]
            table.add_row(v)
        return table.get_string()


    # Hàm này thực hiện thuật toán "Góc Tây Bắc" để 
    # tìm phân bổ ban đầu cho bài toán vận chuyển. 
    # Thuật toán sẽ điền giá trị vào mảng allocation 
    # từ góc trên bên trái, lần lượt từ trên xuống 
    # dưới và từ trái sang phải.
    def north_west_corner_rule(self):
        # Sao chép supply (vector phát) và demand (vector thu) 
        # để tránh làm thay đổi giá trị trên 2 vector gốc này
        # trong quá trình thực thi code bên dưới
        _supply = self.supply.copy()
        _demand = self.demand.copy()

        # Khởi tạo mảng allocation với các giá trị 0
        allocation = np.zeros((len(_supply), len(_demand)))

        i, j = 0, 0

        # Tiếp tục phân bổ từ trên xuống dưới, từ trái sang phải
        while i < len(_supply) and j < len(_demand):
            if _supply[i] < _demand[j]:
                allocation[i, j] = _supply[i]
                _demand[j] -= _supply[i]
                i += 1
            else:
                allocation[i, j] = _demand[j]
                _supply[i] -= _demand[j]
                j += 1
        
        # Chuyển đổi các giá trị 0 thành giá trị NaN
        allocation[allocation==0] = np.nan

        # Trả kết quả
        return allocation


    # Hàm này tính toán giá trị của v[j] dựa vào 
    # giá trị u[i] đã biết, thông qua ma trận 
    # allocation và tham số algo_params.
    def _calculate_v_by_ui(self, allocation, algo_params, i):
        j_set = self._nan_indice(algo_params.v)
        for j in j_set:
            cell = allocation[i][j]
            if np.isnan(cell):
                continue
            if cell >= 0 and np.isnan(algo_params.v[j]):
                algo_params.v[j] = self.cost[i, j] - algo_params.u[i]
                self._calculate_u_by_vj(allocation, algo_params, j)


    # Hàm này tính toán giá trị của u[i] dựa vào 
    # giá trị v[j] đã biết, thông qua ma trận 
    # allocation và tham số algo_params.
    def _calculate_u_by_vj(self, allocation, algo_params, j):
        i_set = self._nan_indice(algo_params.u)
        for i in i_set:
            cell = allocation[i][j]
            if np.isnan(cell):
                continue
            if cell > 0:
                algo_params.u[i] = self.cost[i, j] - algo_params.v[j]
                self._calculate_v_by_ui(allocation, algo_params, i)


    # Hàm này tính toán giá trị vector u và v từ phân 
    # bổ hiện tại. Hàm này sẽ gọi hàm _calculate_v_by_ui 
    # để bắt đầu quá trình tính toán đệ quy.
    def calculate_uv(self, allocation, algo_params):
        self._calculate_v_by_ui(allocation, algo_params, 0)


    # Hàm này tính toán giá trị delta dựa trên giá trị 
    # u và v đã có, để đánh giá sự cải thiện của phương án.
    def calculate_delta(self, algo_params):
        for i in range(self.cost.shape[0]):
            for j in range(self.cost.shape[1]):
                algo_params.delta[i,j] = algo_params.u[i]+algo_params.v[j]-self.cost[i,j]

    # Hàm này loại bỏ các hàng và cột không liên quan 
    # (chỉ có một ô không phải NaN) trong ma trận A. 
    # Hàm sẽ lặp lại việc loại bỏ cho đến khi không 
    # còn hàng và cột nào để loại bỏ.
    def _remove_lonely_rc(self, A):
        updated = False
        notnanA = ~np.isnan(A)
        counts = np.count_nonzero(notnanA, axis=1)
        for i in range(len(counts)):
            if counts[i] == 1:
                A[i, :] =  np.nan
                updated = True
        
        counts = np.count_nonzero(notnanA, axis=0)
        for i in range(len(counts)):
            if counts[i] == 1:
                A[:, i] =  np.nan
                updated = True
        if updated:
            return self._remove_lonely_rc(A)
        return A


    # Hàm này tìm kiếm và trả về ô tiếp theo trong cùng 
    # một hàng của ô hiện tại (current_cell), nếu có, 
    # dựa trên danh sách các ô (_list) được cung cấp. 
    # Nếu không tìm thấy ô tiếp theo, hàm trả về None.
    def _get_next_cell_in_row(self, current_cell, _list):
        for e in _list:
            if e[0] == current_cell[0]:
                return e
        return None
    
    
    # Hàm này tìm kiếm và trả về ô tiếp theo trong cùng 
    # một cột của ô hiện tại (current_cell), nếu có, 
    # dựa trên danh sách các ô (_list) được cung cấp. 
    # Nếu không tìm thấy ô tiếp theo, hàm trả về None.
    def _get_next_cell_in_col(self, current_cell, _list):
        for e in _list:
            if e[1] == current_cell[1]:
                return e
        return None
    

    # Hàm này phân tích và trích xuất chu trình từ 
    # ma trận A, bắt đầu từ ô được chỉ định (start_cell). 
    # Hàm sẽ lặp lại việc tìm kiếm ô tiếp theo trong 
    # cùng một cột, sau đó tìm kiếm ô tiếp theo trong 
    # cùng một hàng, cho đến khi không còn tìm thấy ô 
    # tiếp theo nào. Kết quả cuối cùng là một chu trình 
    # và ma trận chu trình, trong đó các ô có giá trị 
    # 1 hoặc -1 tương ứng với vị trí của các ô trong chu trình.
    def _parse_cyle(self, A, start_cell):
        # Tìm tất cả vị trí của các ô không phải NaN trong ma trận A.
        pos = np.where(~np.isnan(A))

        _list = []

        # Duyệt qua các vị trí không phải NaN và thêm chúng vào danh sách _list.
        for i in range(len(pos[0])):
            _list.append((pos[0][i], pos[1][i]))
        
        # Khởi tạo chu trình với phần tử đầu tiên là start_cell.
        cycle = [start_cell]

        while True:
            # Loại bỏ ô cuối cùng của chu trình hiện tại khỏi danh sách _list.
            _list = [x for x in _list if x != cycle[-1]]

            # Tìm ô tiếp theo trong cùng cột với ô cuối cùng của chu trình hiện tại.
            next_cell = self._get_next_cell_in_col(cycle[-1], _list)
            
            # Nếu không tìm thấy ô tiếp theo, thoát vòng lặp.
            if next_cell is None:
                break
            
            # Thêm ô tiếp theo vào chu trình.
            cycle.append(next_cell)

            _list = [x for x in _list if x != cycle[-1]]

            # Tìm ô tiếp theo trong cùng hàng với ô cuối cùng của chu trình hiện tại.
            next_cell = self._get_next_cell_in_row(cycle[-1], _list)
            if next_cell is None:
                break

            cycle.append(next_cell)
        
        # Khởi tạo ma trận cycle_mat với kích thước giống ma trận A.
        cycle_mat = np.empty(A.shape)
        
        # Nếu vị trí của ô là chẵn, gán giá trị 1 cho ô đó trong ma trận cycle_mat.
        for i in range(len(cycle)):
            if i%2 == 0:
                cycle_mat[cycle[i][0], cycle[i][1]] = 1
            else:
                cycle_mat[cycle[i][0], cycle[i][1]] = -1

        return cycle, cycle_mat
    
    # Hàm này trả về danh sách các vị trí của các ô không phải NaN trong ma trận matrix.
    def _get_non_nan_cell_positions(self, matrix):
        # Tìm chỉ số của tất cả các giá trị không phải NaN trong ma trận.
        non_nan_indices = np.argwhere(~np.isnan(matrix))

        # Khởi tạo một danh sách để lưu trữ các vị trí không phải NaN.
        non_nan_positions = []

        # Thêm từng vị trí không phải NaN vào danh sách.
        for i, j in non_nan_indices:
            non_nan_positions.append((i, j))

        return non_nan_positions
    

    # Hàm này dùng để phát hiện chu trình trong ma trận allocation, bắt đầu từ ô start_cell.
    def detect_cycle(self, allocation, start_cell):
        # Sao chép ma trận allocation vào biến A.
        A = allocation.copy()
        
        # Loại bỏ các hàng và cột không nằm trong chu trình (nếu có) trong A bằng hàm _remove_lonely_rc(A).
        A = self._remove_lonely_rc(A)
        
        # Xác định chu trình và ma trận cycle_mat bằng hàm _parse_cyle(A, start_cell).
        cycle, cycle_mat = self._parse_cyle(A, start_cell)
        
        # Trả về chu trình và ma trận cycle_mat.
        return cycle, cycle_mat


    # Hàm này kiểm tra xem ma trận matrix có chứa chu trình hay không. 
    # Nếu có, hàm trả về True; nếu không, trả về False.
    def does_contains_cycle(self, matrix):
        # Tìm tất cả các vị trí không phải NaN trong ma trận matrix bằng hàm _get_non_nan_cell_positions(matrix).
        poss = self._get_non_nan_cell_positions(matrix)
        
        # Duyệt qua từng vị trí không phải NaN trong ma trận matrix.
        for pos in poss:
            # Kiểm tra xem có chu trình nào bắt đầu từ vị trí đó không bằng cách sử dụng hàm detect_cycle(matrix, pos).
            # Nếu có chu trình có độ dài ít nhất là 4, trả về True.
            # Nếu không tìm thấy chu trình nào, trả về False.
            cycle, cycle_mat = self.detect_cycle(matrix, pos)
            if len(cycle) >= 4:
                return True
        return False


    def draw_cycle(self, allocation, algo_params):
        ret = self.table_string(allocation, algo_params, color=False)
        lines = ret.split('\n')
        A = []
        # draw col link
        for line in lines:
            A.append(list(line))
        A = np.array(A)
        At = np.transpose(A)

        
        tlines = []
        max_len = 0
        for i in range(len(At)):
            tline = ''.join(At[i].tolist())
            pattern = r"(?<=\+).*?(?=-)"
            tline = re.sub(r"(?<=\+).*?(?=-)", lambda m: "*"*len(m.group(0)), tline)
            tline = re.sub(r"(?<=-).*?(?=\+)", lambda m: "*"*len(m.group(0)), tline)
            tlines.append(tline)
            if len(tline) > max_len:
                max_len = len(tline)

        for i in range(len(tlines)):
            if len(tlines[i]) < max_len:
                tlines[i] +=' '*(max_len-len(tlines[i]))
        
        At = []
        for tline in tlines:
            At.append(list(tline))
        At = np.array(At)
        A = np.transpose(At)

        lines = []
        for i in range(len(A)):
            line = ''.join(A[i].tolist())
            lines.append(line)

        # draw row link
        for i in range(len(lines)):
            pattern = r"(?<=\(\+\)).*?(?=\(-\))"
            lines[i] = re.sub(r"(?<=\(\+\)).*?(?=\(-\))", lambda m: "*"*len(m.group(0)), lines[i])
            lines[i] = re.sub(r"(?<=\(-\)).*?(?=\(\+\))", lambda m: "*"*len(m.group(0)), lines[i])
        
        ret = '\n'.join(lines)
        ret = ret.replace('*', Fore.LIGHTRED_EX+'*'+Fore.RESET)
        print(ret)


    # Hàm này tìm giá trị theta_min trong ma trận matrix dựa trên chu trình cycle.
    def find_theta_min(self, matrix, cycle):
        # Tạo một danh sách positions chứa các vị trí có chỉ số lẻ trong chu trình.
        positions = []
        for i in range(len(cycle)):
            if i%2==1:
                positions.append(cycle[i])
        
        # Tạo một ma trận masked, đặt các vị trí không được chọn thành NaN.
        mask = np.ones(matrix.shape, dtype=bool)
        mask[tuple(zip(*positions))] = False
        masked_matrix = np.where(mask, np.nan, matrix)

        # Tìm giá trị nhỏ nhất và chỉ số tương ứng của nó.
        min_value = np.nanmin(masked_matrix)
        min_indices = np.where(masked_matrix == min_value)

        # Sắp xếp các chỉ số theo thứ tự từ trên xuống dưới, từ trái sang phải.
        sorted_indices = sorted(zip(*min_indices), key=lambda x: x[0]+x[1])

        # Chuyển đổi các chỉ số thành tọa độ 2D.
        sorted_positions = [(r, c) for r, c in sorted_indices]

        # Trả về giá trị nhỏ nhất và các vị trí tương ứng.
        return min_value, sorted_positions

    # Hàm này tìm giá trị delta_max trong ma trận delta của 
    # algo_params và trả về giá trị lớn nhất và vị trí tương ứng của nó.
    def find_delta_max(self, algo_params):
        max_index = np.argmax(algo_params.delta)
        max_row = max_index // 4
        max_col = max_index % algo_params.delta.shape[1]
        delta_max = np.nanmax(algo_params.delta)
        return delta_max, (max_row, max_col)

    # Hàm này tính mức độ suy biến của ma trận allocation 
    # bằng cách tính tổng số ô không phải NaN và trừ đi 
    # tổng kích thước của ma trận.
    def get_degeneration_order(self, allocation):
        num_non_nan = len(np.argwhere(~np.isnan(allocation)))
        return sum(allocation.shape)-1 - num_non_nan

    # Hàm này cập nhật lại ma trận allocation dựa trên giá trị delta_max và vị trí tương ứng của nó. 
    def re_allocate_base_on_delta_max(self, allocation, algo_params, delta_max_pos, draw=True):
        # Đặt giá trị 0 vào vị trí delta_max trong ma trận allocation.
        allocation[delta_max_pos[0], delta_max_pos[1]] = 0
        
        # Xác định chu trình và ma trận cycle_mat dựa trên vị trí delta_max.
        cycle, cycle_mat = self.detect_cycle(allocation, start_cell=delta_max_pos)
        algo_params.cycle = cycle
        algo_params.cycle_mat = cycle_mat

        if draw:
            self.draw_cycle(allocation, algo_params)

        # Tìm giá trị theta_min và các vị trí tương ứng.
        theta_min, theta_min_poss = self.find_theta_min(allocation, algo_params.cycle)
        algo_params.theta_min = theta_min
        algo_params.theta_min_pos = theta_min_poss[0]
        
        # Cập nhật lại ma trận allocation dựa trên theta_min và cycle_mat.
        _allocation = allocation + theta_min*algo_params.cycle_mat
        
        # Chuyển đổi các giá trị 0 trong ma trận cập nhật thành NaN.
        _allocation[_allocation==0] = np.nan
        
        # Trả về ma trận cập nhật.
        return _allocation.copy()

    # Hàm này kiểm tra xem ma trận allocation đã tối ưu chưa. 
    # Nếu đã tối ưu, hàm trả về True và các thông số thuật toán; 
    # nếu chưa, trả về False và các thông số thuật toán.
    def is_optimized(self, allocation):
        # Khởi tạo đối tượng algo_params.
        algo_params = AlgoParams(allocation.shape[0], allocation.shape[1])
        
        # Tính vector u, v từ ma trận allocation.
        self.calculate_uv(allocation, algo_params)
        
        # Tính ma trận delta từ vector u, v.
        self.calculate_delta(algo_params)
        
        # Tìm giá trị delta_max và vị trí tương ứng của nó.
        delta_max, delta_max_pos = self.find_delta_max(algo_params)
        algo_params.delta_max = delta_max
        algo_params.delta_max_pos = delta_max_pos
        
        # Nếu delta_max <= 0, trả về `True
        if delta_max <= 0:
            return True, algo_params
        
        return False, algo_params
    
    # Hàm này sinh ra tất cả các tổ hợp của n phần tử từ mảng đầu vào arr. 
    # Nếu n == 0, hàm trả về một danh sách rỗng. Ngược lại, hàm trả về 
    # tất cả tổ hợp có thể có.
    def _combinations(self, arr, n):
        if n == 0:
            return [[]]
        else:
            return [[x] + tail for x in arr for tail in self._combinations(arr, n - 1)]
        

    # Hàm này tạo ra một danh sách các ma trận với các giá trị NaN thay thế bằng 0.
    def _replace_nan_with_zero(self, matrix, n):
        # Tìm chỉ số của tất cả các giá trị NaN trong ma trận matrix.
        nan_indices = np.argwhere(np.isnan(matrix))

        # Tạo một danh sách để lưu trữ tất cả các ma trận có giá trị NaN thay thế bằng 0.
        matrices = []

        # Sinh ra tất cả các tổ hợp có thể của n chỉ số NaN.
        nan_combinations = self._combinations(nan_indices, n)

        # Thay thế mỗi giá trị NaN bằng 0 trong mỗi tổ hợp và thêm ma trận kết quả vào danh sách.
        for nan_indices in nan_combinations:
            new_matrix = matrix.copy()
            
            for i, j in nan_indices:
                new_matrix[i, j] = 0

            # Nếu ma trận này có chứa chu trình thì bỏ qua.
            if self.does_contains_cycle(new_matrix):
                continue

            matrices.append(new_matrix)

        # Trả về danh sách các ma trận đã thay thế.
        return matrices


    # Hàm này cố gắng thêm số 0 vào ma trận allocation.
    def try_to_add_zero(self, allocation, num_zero):
        # Thay thế num_zero giá trị NaN trong ma trận allocation bằng 0.
        matrices = self._replace_nan_with_zero(allocation, num_zero)
        
        if len(matrices) == 0:
            return None
        
        for matrix in matrices:
            # Kiểm tra xem ma trận đã được tối ưu chưa.
            # Nếu đã tối ưu, trả về ma trận tối ưu.
            ok, algo_params = self.is_optimized(matrix)
            if ok:
                return matrix.copy()
            
            # Nếu chưa tối ưu, tiếp tục cập nhật ma trận dựa trên giá trị delta_max.
            delta_max, delta_max_pos = self.find_delta_max(algo_params)
            new_allocation = self.re_allocate_base_on_delta_max(matrix, algo_params, delta_max_pos, draw=False)
            if algo_params.theta_min == 0:
                # Phương án này có theta_min = 0, ta sẽ bỏ qua, thử tiếp phương án mới
                continue

            # Trả về ma trận đã được cập nhật.
            return matrix.copy()

    # Hàm này giải quyết bài toán bằng cách thực hiện các bước sau:
    def solve(self):
        # Tính ma trận phân bổ ban đầu dựa trên quy tắc góc Tây-Bắc.
        new_allocation = self.north_west_corner_rule()

        print("Phương án xuất phát dứa theo phương pháp góc Tây-Bắc")
        print(self.table_string(new_allocation))
        

        while True:
            # In ra tổng chi phí của ma trận hiện tại.
            print("Tổng chi phí của phương án hiện tại là {}".format(self.total_cost(new_allocation)))
            
            # Kiểm tra xem ma trận hiện tại có suy biến hay không.
            do = self.get_degeneration_order(new_allocation)
            if do > 0:
                # Nếu suy biến, đề xuất một ma trận mới bằng cách thêm 0.
                print("Phương án hiện tại là suy biến")
                print("Đề xuất phương án mới bằng cách bổ sung thêm 0")
                new_allocation = self.try_to_add_zero(new_allocation, do)
                if new_allocation is None:
                    print("Xin lỗi, tôi KHÔNG thể giải được bài toán này")
                    return
                print(self.table_string(new_allocation))
            else:
                print("Phương án hiện tại KHÔNG suy biến")

            self.steps.append(new_allocation.copy())
            allocation = new_allocation

            # Kiểm tra xem ma trận hiện tại đã được tối ưu chưa.
            print("Triển khai tính vector u, v, ma trận delta")
            ok, algo_params = self.is_optimized(new_allocation)
            if ok:
                print("")
                print(self.table_string(new_allocation, algo_params))
                print("Các delta đều không dương, phương án hiện tại đã tối ưu")
                print("Kết quả cuối cùng")
                new_allocation[new_allocation==0] = np.nan
                print(self.table_string(new_allocation))
                print("Tổng chi phí là {}".format(self.total_cost(new_allocation)))
                return
            
            # Nếu chưa tối ưu, cập nhật ma trận dựa trên giá trị delta_max.
            delta_max, delta_max_pos = self.find_delta_max(algo_params)
            print(self.table_string(allocation, algo_params))
            print("delta_max = {} tại ô ({};{})".format(delta_max, delta_max_pos[0]+1, delta_max_pos[1]+1))
            print("Điền số 0 vào ô này, xác định chu trình cập nhật")
            
            new_allocation = self.re_allocate_base_on_delta_max(allocation, algo_params, delta_max_pos)
            if algo_params.theta_min == 0:
                print("theta_min = 0. Xin lỗi, tôi k giải được bài toán này!")
                continue
            
            for cell in algo_params.cycle:
                value = (cell[0]+1, cell[1]+1)
                print(value, end=' --> ')
            print('(ô xuất phát)')
            print("theta_min = {} tại ô ({};{})".format(algo_params.theta_min, algo_params.theta_min_pos[0]+1, algo_params.theta_min_pos[1]+1))

            # Trả về ma trận tối ưu cuối cùng và tổng chi phí tương ứng.
            print("Phương án mới, sau khi cập nhật theo chu trình")
            print(self.table_string(new_allocation))


def parse_vector(str):
    return np.array([int(x.replace(' ', '')) for x in str.split(' ')])

if __name__ == '__main__':
    # Define the supply, demand, and cost matrices
    supply = np.array([50, 70, 60])
    demand = np.array([30, 50, 60, 40])
    cost = np.array([[3, 4, 6, 5],
                    [6, 4, 5, 8],
                    [7, 6, 4, 9]])
    # Input the size of the vectors and the matrix
    supply = parse_vector(input("Nhập vector phát (gồm các số ngăn cách bằng khoảng trắng): a = "))
    demand = parse_vector(input("Nhập vector thu  (gồm các số ngăn cách bằng khoảng trắng): b = "))

    cost = np.zeros((len(supply), len(demand)))

    for i in range(len(supply)):
        cost[i] = parse_vector(input("Nhập hàng thứ {} của ma trận chi phí (gồm các số ngăn cách bằng khoẳng trắng): ".format(i+1)))

    if sum(supply) != sum(demand):
        print("Chương trình chỉ hỗ trợ các bài toán cân bằng thu-phát")
    else:
        # init problem and solve it
        print("Chú ý: ta đếm hàng/cột bắt đầu đếm từ 1")
        p = TransProb(supply, demand, cost)
        p.solve()
