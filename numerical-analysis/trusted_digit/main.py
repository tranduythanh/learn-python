number_str = input("Input a float number: ")
omega = 0.5
delta_a = 0.0003
maxlength = len(number_str)
number = float(number_str)
left_comma = int(number)
rest = number - left_comma
ret = str(left_comma)+"."
k=-1
maxlength = maxlength - len(ret) - 1

while maxlength>0:
    digit = int(rest*10)
    maxlength -= 1

    if delta_a > omega * 10**(k):
        break

    ret = ret + str(digit)
    k -= 1
    rest = rest*10-digit

print(ret)


# op2=>operation: omega = 0.5
# delta_a = 0.0003
# number_str = input('Input a float number: ')
# maxlength = len(number_str)
# number = float(number_str)
# left_comma = int(number)
# rest = (number - left_comma)
# ret = (str(left_comma) + '.')
# k = (- 1)
# maxlength = (maxlength - len(ret)) - 1
# cond23=>condition: while (maxlength > 0)
# op49=>operation: digit = int(rest*10)
# maxlength = maxlength-1
# cond25=>condition: delta_a > omega*(10**k)
# op64=>operation: ret = (ret + str(digit))
# k = k-1
# rest = (rest*10)-digit
# sub72=>subroutine: print(ret)

# op2->cond23     
# cond23(yes,bottom)->op49
# cond23(no,right)->sub72
# op49->cond25
# cond25(yes,right)->sub72
# cond25(no,left)->op64
# op64(top)->cond23
