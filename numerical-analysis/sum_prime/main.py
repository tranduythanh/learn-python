import math 

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1 ):
        if n % i == 0:
            return False
    return True

raw_input = input("Input a list of numbers seperated by space: ")
nums = [int(x) for x in raw_input.split()]
sum = 0
for num in nums:
    if isPrime(num):
        sum += num
print(sum)

# st=>start: Start of isPrime(n)
# e=>end: End and return ret
# op1=>operation: i=2
# op2=>operation: ret=False
# op3=>operation: ret=True
# op5=>operation: i=i+1
# sub1=>subroutine: My Subroutine
# cond1=>condition: n<=1
# cond2=>condition: i <= sqrt(1)
# cond3=>condition: n%i == 0
# io=>inputoutput: catch something...
# para=>parallel: parallel tasks

# st->cond1
# cond2(no,bottom)->op3->e
# cond1(yes,right)->op2->e
# cond1(no,bottom)->op1->cond2
# cond2(yes,right)->cond3
# cond3(yes,right)->op2
# cond3(no)->op5(left)->cond2


# st=>start: Start of SumPrime(n)
# e=>end: End
# op1=>operation: sum:=0
# i:=0
# op2=>operation: sum += arr[i]
# op5=>operation: i=i+1
# sub1=>subroutine: arr = [int (x) for x in input().split()]
# sub2=>subroutine: print(sum)
# cond1=>condition: i<len(arr)
# op6=>operation: ok = isPrime(arr[i]) 
# cond2=>condition: ok

# st->sub1->op1->cond1
# cond1(no,right)->sub2->e
# cond1(yes,bottom)->op6->cond2
# cond2(yes,bottom)->op2->op5(left)->cond1
# cond2(no,right)->op5