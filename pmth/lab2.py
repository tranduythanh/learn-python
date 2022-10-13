import numpy as np

def nhap_ma_tran():
    # Nhập kích thước ma trận từ bàn phím
    str = input("Nhập kích thước ma trận: ").strip()
    kich_thuoc = [int(x) for x in str.split()]
    print(kich_thuoc)
    so_hang = kich_thuoc[0]
    so_cot = kich_thuoc[1]

    # khởi tạo ma trận toàn số 0
    ma_tran = np.zeros(kich_thuoc)

    # Nhập vào từng hàng
    for i in range(so_hang):
        hang_str = input("Nhập các số của hàng {0} cách nhau bởi khoảng trắng: ".format(i))
        hang = [float (x) for x in hang_str.split()]
        ma_tran[i]=hang

    return ma_tran

def bai2():
    # tính tổng từng hàng của ma trận
    ma_tran = nhap_ma_tran()
    print(np.sum(ma_tran, axis=1))

def bai3():
    # Xuất ma trận con
    ma_tran=nhap_ma_tran()
    if ma_tran.shape[0] < 3 or ma_tran.shape[1] < 3:
        print("kích thước ma trận không hợp lệ")
    else:
        print(ma_tran[0:3,1:3])

def bai4():
    str1 = input('nhập vector v1 = (a1, a2, a3) vào đây: ')
    v1 = np.array([int(x) for x in str1.split()])

    str2 = input('nhập vector v2 = (b1, b2, b3) vào đây: ')
    v2 = np.array([int(x) for x in str2.split()])

    v = np.sum(v1 * v2)
    print(v)


def bai5():
    x = float(input("Nhập số x = "))
    b = (np.tan(x)+1)**(1/3)/(np.sin(x)**2+1)
    print(b)


def bai6():
    x = float(input("Nhập số x = "))
    b = (np.exp2(np.sin(x)) + np.log(2*x-3))/(np.cos(np.pi / x) - x**(1/3))
    print(b)


def bai7():
    str1 = input("Nhập 3 hệ số của đường thằng d1 = a1*x + b1*y + c1: ")
    str2 = input("Nhập 3 hệ số của đường thằng d2 = a2*x + b2*y + c2: ")

    he_so_d1 = np.array([float(x) for x in str1.strip().split()])
    he_so_d2 = np.array([float(x) for x in str2.strip().split()])

    vtpt1 = he_so_d1[:2]
    vtpt2 = he_so_d2[:2]

    cos_d1_d2 = np.sum(vtpt1*vtpt2) / (np.sqrt(np.sum(vtpt1**2)) * np.sqrt(np.sum(vtpt2**2)))

    goc_d1_d2 = np.arccos(cos_d1_d2)

    print("góc giữa 2 đường thẳng theo grad: ", goc_d1_d2)
    print("góc giữa 2 đường thẳng theo độ  : ", np.degrees(goc_d1_d2))

def tich1TrenX(n):
    tich = 1
    for i in range(n+1):
        tich *= (1.0/i)
    return tich

if __name__ == "__main__":
    x = int(input("chọn bài tập bằng cách nhập số từ 2 tới 7: "))
    if x == 2:
        bai2()
    if x == 3:
        bai3()
    if x == 4:
        bai4()
    if x ==5:
        bai5()
    if x == 6:
        bai6()
    if x == 7:
        bai7()
    if x < 2 or x > 7:
        print("không có bài tập phù hợp")
