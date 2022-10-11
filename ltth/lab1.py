import math

def bai4():
    v1 = [int(x) for x in input('nhập vector v1 vào đây: ').split()]
    v2 = [int(x) for x in input('nhập vector v2 vào đây: ').split()]
    v = [v1[i] + v2[i] for i in range(len(v1))]
    print(v)


def bai5():
    d = {}
    for i in range(3):
        ten, mssv = input("nhập tên và mssv, phân cách bằng dấu ',': ").split(',')
        d[ten]=mssv
    print("-------------------")
    print("danh sách sinh viên")
    for ten, mssv in d.items():
        print('-', ten, mssv)


def y(x):
    if x < 0:
        return 0
    if x < 1:
        return x
    if x < 2:
        return 2-x
    return 22


def bai6():
    print('y(-1)=', y(-1))
    print('y(0) =', y(0))
    print('y(1) =', y(1))
    print('y(2) =', y(2))
    print('y(3) =', y(3))


def tong1ToiN(n):
    tong = 0
    for i in range(n+1):
        tong+=i
    return tong


def bai7():
    print("tổng [1,2]", tong1ToiN(5))
    print("tổng [1,7]", tong1ToiN(5))
    print("tổng [1,10]", tong1ToiN(5))
    print("tổng [1,11]", tong1ToiN(5))


def tich1TrenX(n):
    tich = 1
    for i in range(n+1):
        tich *= (1.0/i)
    return tich


def bai8():
    print("tích 1/x với N=1", tich1TrenX(1))
    print("tích 1/x với N=2", tich1TrenX(2))
    print("tích 1/x với N=3", tich1TrenX(3))
    print("tích 1/x với N=4", tich1TrenX(4))
    print("tích 1/x với N=7", tich1TrenX(7))

def giaiThua(n):
    tich = 1
    for i in range(1, n+1):
        tich *= i
    return tich


def bai9():
    print("1! = ", giaiThua(1))
    print("3! = ", giaiThua(3))
    print("6! = ", giaiThua(6))


def bai10():
    a, b, c = input('nhập 3 hệ số cách nhau bằng khoảng trắng: ').split()
    a = float(a)
    b = float(b)
    c = float(c)
    if a == 0:
        if b == 0:
            print('pt sai roi cung')
        else:
            print('x=', -c/b)
    else:
        delta = b**2-4*a*c
        if delta < 0:
            print('k ra nghiem thuc dau')
        else:
            x1 = (-b-math.sqrt(delta))/(2*a)
            x2 = (-b+math.sqrt(delta))/(2*a)
            print('x1=', x1)
            print('x2=', x2)

if __name__ == "__main__":
    x = int(input("chọn bài tập bằng cách nhập số từ 4 tới 10: "))
    if x == 4:
        bai4()
    if x ==5:
        bai5()
    if x == 6:
        bai6()
    if x == 7:
        bai7()
    if x == 8:
        bai8()
    if x == 9:
        bai9()
    if x == 10:
        bai10()
    if x < 4 or x > 10:
        print("không có bài tập phù hợp")