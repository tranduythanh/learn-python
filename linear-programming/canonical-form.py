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
        print('Linear programming problem:')
        data = self.read_file(file_name)
        n = len(data) - 2
        max_variable_index = self.find_max_variable_index(data)
        self.parse_coeff_C(data[0], max_variable_index)
        self.Objective = data[0][-1]
        A = data[1:n + 1]
        self.parse_data(A, max_variable_index)

    def read_file(self, file_name):
        with open(file_name, 'r') as f:
            data = [line.split() for line in f]
            for line in data:
                print(' '.join(line))
        return data

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


    def var_index(self, mono):
        pattern = r'x(\d+)'
        result = re.search(pattern, mono)
        if result is None or result == '':
            return None
        digits = int(result.group(1))
        return int(digits)
    
    def parse_coeff_index(self, mono):
        index = self.var_index(mono)
        if index is None:
            return None
        coeff = float(mono.split('x')[0].replace('*', ''))
        return index, coeff


    def parse_coeff_C(self, row, max_variable_index):
        coeff_C1 = [c for c in row[:-2] if c != '+']
        coeff_C_dict = {}
        for s in coeff_C1:
            index, coeff = self.parse_coeff_index(s)
            coeff_C_dict[index] = coeff
        self.Coeff_C = [coeff_C_dict.get(i, 0) for i in range(1, max_variable_index + 1)]

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

    def canonical_form(self):
        print('Canonical form:')
        A_CT = np.array(self.Coeff_A, dtype=float)
        B_CT = np.array(self.Coeff_B, dtype=float)
        C_CT = np.array(self.Coeff_C, dtype=float)
        A_CT, C_CT = self.generate_canonical_coefficients(A_CT, C_CT)
        self.print_objective_function(C_CT)
        self.print_constraints(A_CT, B_CT)
        self.print_variable_constraints(len(C_CT))

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