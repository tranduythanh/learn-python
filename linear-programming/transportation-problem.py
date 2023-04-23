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


    def north_west_corner_rule(self):
        _supply = self.supply.copy()
        _demand = self.demand.copy()
        allocation = np.zeros((len(_supply), len(_demand)))

        i, j = 0, 0
        while i < len(_supply) and j < len(_demand):
            if _supply[i] < _demand[j]:
                allocation[i, j] = _supply[i]
                _demand[j] -= _supply[i]
                i += 1
            else:
                allocation[i, j] = _demand[j]
                _supply[i] -= _demand[j]
                j += 1
        
        allocation[allocation==0] = np.nan
        return allocation


    def _calculate_v_by_ui(self, allocation, algo_params, i):
        j_set = self._nan_indice(algo_params.v)
        for j in j_set:
            cell = allocation[i][j]
            if np.isnan(cell):
                continue
            if cell >= 0 and np.isnan(algo_params.v[j]):
                algo_params.v[j] = self.cost[i, j] - algo_params.u[i]
                self._calculate_u_by_vj(allocation, algo_params, j)


    def _calculate_u_by_vj(self, allocation, algo_params, j):
        i_set = self._nan_indice(algo_params.u)
        for i in i_set:
            cell = allocation[i][j]
            if np.isnan(cell):
                continue
            if cell > 0:
                algo_params.u[i] = self.cost[i, j] - algo_params.v[j]
                self._calculate_v_by_ui(allocation, algo_params, i)


    def calculate_uv(self, allocation, algo_params):
        self._calculate_v_by_ui(allocation, algo_params, 0)


    def calculate_delta(self, algo_params):
        for i in range(self.cost.shape[0]):
            for j in range(self.cost.shape[1]):
                algo_params.delta[i,j] = algo_params.u[i]+algo_params.v[j]-self.cost[i,j]


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


    def _get_next_cell_in_row(self, current_cell, _list):
        for e in _list:
            if e[0] == current_cell[0]:
                return e
        return None
    
    
    def _get_next_cell_in_col(self, current_cell, _list):
        for e in _list:
            if e[1] == current_cell[1]:
                return e
        return None
    

    def _parse_cyle(self, A, start_cell):
        pos = np.where(~np.isnan(A))
        _list = []
        for i in range(len(pos[0])):
            _list.append((pos[0][i], pos[1][i]))
        cycle = [start_cell]

        while True:
            _list = [x for x in _list if x != cycle[-1]]
            next_cell = self._get_next_cell_in_col(cycle[-1], _list)
            if next_cell is None:
                break
            cycle.append(next_cell)

            _list = [x for x in _list if x != cycle[-1]]
            next_cell = self._get_next_cell_in_row(cycle[-1], _list)
            if next_cell is None:
                break
            cycle.append(next_cell)
        cycle_mat = np.empty(A.shape)
        for i in range(len(cycle)):
            if i%2 == 0:
                cycle_mat[cycle[i][0], cycle[i][1]] = 1
            else:
                cycle_mat[cycle[i][0], cycle[i][1]] = -1

        return cycle, cycle_mat
    

    def _get_non_nan_cell_positions(self, matrix):
        # Get the indices of all non-NaN values in the matrix
        non_nan_indices = np.argwhere(~np.isnan(matrix))

        # Create a list to store all non-NaN positions
        non_nan_positions = []

        # Add each non-NaN position to the list
        for i, j in non_nan_indices:
            non_nan_positions.append((i, j))

        return non_nan_positions
    

    def detect_cycle(self, allocation, start_cell):
        A = allocation.copy()
        A = self._remove_lonely_rc(A)
        cycle, cycle_mat = self._parse_cyle(A, start_cell)
        return cycle, cycle_mat


    def does_contains_cycle(self, matrix):
        poss = self._get_non_nan_cell_positions(matrix)
        for pos in poss:
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


    def find_theta_min(self, matrix, cycle):
        positions = []
        for i in range(len(cycle)):
            if i%2==1:
                positions.append(cycle[i])
        
        # Create a masked matrix where non-selected positions are set to NaN
        mask = np.ones(matrix.shape, dtype=bool)
        mask[tuple(zip(*positions))] = False
        masked_matrix = np.where(mask, np.nan, matrix)

        # Find the minimum value and its index
        min_value = np.nanmin(masked_matrix)
        min_indices = np.where(masked_matrix == min_value)

        # Sort the indices by up-left order
        sorted_indices = sorted(zip(*min_indices), key=lambda x: x[0]+x[1])

        # Convert the indices to 2D coordinates
        sorted_positions = [(r, c) for r, c in sorted_indices]

        return min_value, sorted_positions


    def find_delta_max(self, algo_params):
        max_index = np.argmax(algo_params.delta)
        max_row = max_index // 4
        max_col = max_index % algo_params.delta.shape[1]
        delta_max = np.nanmax(algo_params.delta)
        return delta_max, (max_row, max_col)


    def get_degeneration_order(self, allocation):
        num_non_nan = len(np.argwhere(~np.isnan(allocation)))
        return sum(allocation.shape)-1 - num_non_nan


    def re_allocate_base_on_delta_max(self, allocation, algo_params, delta_max_pos, draw=True):
        # print('Ta điền 0 vào ô này, sau đó xác định chu trình:')
        allocation[delta_max_pos[0], delta_max_pos[1]] = 0
        cycle, cycle_mat = self.detect_cycle(allocation, start_cell=delta_max_pos)
        algo_params.cycle = cycle
        algo_params.cycle_mat = cycle_mat

        if draw:
            self.draw_cycle(allocation, algo_params)

        theta_min, theta_min_poss = self.find_theta_min(allocation, algo_params.cycle)
        algo_params.theta_min = theta_min
        algo_params.theta_min_pos = theta_min_poss[0]
        
        _allocation = allocation + theta_min*algo_params.cycle_mat
        _allocation[_allocation==0] = np.nan
        return _allocation.copy()


    def is_optimized(self, allocation):
        algo_params = AlgoParams(allocation.shape[0], allocation.shape[1])
        # calculate vector u, v
        self.calculate_uv(allocation, algo_params)
        
        # calculate matrix delta
        self.calculate_delta(algo_params)
        
        # check max value in matrix delta and its position 
        delta_max, delta_max_pos = self.find_delta_max(algo_params)
        algo_params.delta_max = delta_max
        algo_params.delta_max_pos = delta_max_pos
        
        if delta_max <= 0:
            return True, algo_params
        
        return False, algo_params
    

    def _combinations(self, arr, n):
        # Generate all combinations of n elements from the input array
        if n == 0:
            return [[]]
        else:
            return [[x] + tail for x in arr for tail in self._combinations(arr, n - 1)]
        

    def _replace_nan_with_zero(self, matrix, n):
        # Get the indices of all NaN values in the matrix
        nan_indices = np.argwhere(np.isnan(matrix))

        # Create a list to store all matrices with NaN replaced by 0
        matrices = []

        # Generate all possible combinations of n NaN indices
        nan_combinations = self._combinations(nan_indices, n)

        # Replace each NaN value with 0 in each combination and add the resulting matrix to the list
        for nan_indices in nan_combinations:
            new_matrix = matrix.copy()
            
            for i, j in nan_indices:
                new_matrix[i, j] = 0

            # remove invalid allocation
            if self.does_contains_cycle(new_matrix):
                continue

            matrices.append(new_matrix)

        return matrices


    def try_to_add_zero(self, allocation, num_zero):
        matrices = self._replace_nan_with_zero(allocation, num_zero)
        
        if len(matrices) == 0:
            return None
        
        for matrix in matrices:
            ok, algo_params = self.is_optimized(matrix)
            if ok:
                return matrix.copy()
            
            # reallocating based on theta_max
            delta_max, delta_max_pos = self.find_delta_max(algo_params)
            new_allocation = self.re_allocate_base_on_delta_max(matrix, algo_params, delta_max_pos, draw=False)
            if algo_params.theta_min == 0:
                # phương án này có theta_min = 0, ta sẽ bỏ qua, thử tiếp phương án mới
                continue
            return matrix.copy()


    def solve(self):
        new_allocation = self.north_west_corner_rule()

        print("Phương án xuất phát dứa theo phương pháp góc Tây-Bắc")
        print(self.table_string(new_allocation))
        

        while True:
            print("Tổng chi phí của phương án hiện tại là {}".format(self.total_cost(new_allocation)))
            do = self.get_degeneration_order(new_allocation)
            if do > 0:
                print("Phương án hiện tại là suy biến")
                print("Đề xuất phương án mới bằng cách bổ sung thêm 0")
                new_allocation = self.try_to_add_zero(new_allocation, do)
                if new_allocation is None:
                    print("Xin lỗi, tôi KHÔNG thể giải được bài toán này")
                    return
                print(self.table_string(new_allocation))
            else:
                print("Phương án hiện tại KHÔNG suy biến")

            # save step
            self.steps.append(new_allocation.copy())
            allocation = new_allocation

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
            
            # reallocating based on thta_max
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
