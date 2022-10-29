import numpy as np

import math

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
        hang_str = input(
            "Nhập các số của hàng {0} cách nhau bởi khoảng trắng: ".format(i))
        hang = [float(x) for x in hang_str.split()]
        ma_tran[i] = hang

    return ma_tran


def bai1():
    ma_tran= nhap_ma_tran()

    print(ma_tran)

    kich_thuoc = ma_tran.shape
    so_hang = kich_thuoc[0]
    so_cot = kich_thuoc[1]

    # tạo ma trận con có cùng số cột, nhưng số hàng chỉ có 1 nửa
    ma_tran_con = np.zeros((so_hang//2,so_cot))

    # sao chép từng hàng chẵn của ma_tran vào ma_tran_con
    for i in range(so_hang):
        if i%2==1:
            ma_tran_con[i//2] = ma_tran[i]

    print(ma_tran_con)


def bai2():
    m = np.random.rand(5,5)

    print("Ma trận ngẫu nhiên: ", m)

    so_hang = m.shape[0]

    tong = 0
    for i in range(so_hang):
        tong = tong + m[i][i]

    print("Tổng các số trên đường chéo chính: ", tong)


def bai3():
    a = (2**2+5)/( 2 * (np.sqrt(2)+1) )
    print(a)


def bai4():
    x = float(input("Nhập x = "))
    a = (np.cbrt(np.tan(x)) + 1) / (np.sin(x)**2 + 1)
    print(a)


def bai5():
    x = float(input("Nhập số x = "))
    a = (2**np.sin(x) + np.log(2*x-3)) / (np.cos(np.pi/x) - np.cbrt(x))
    print(a)


def ucln(a, b):
    kq = 1
    for i in range(2, min(a, b)+1):
        if  a%i!=0 or b%i!=0:
            continue
        kq = i
    return kq


def bai6():
    n = int(input("Nhập số lượng số nguyên dương n = "))
    if n < 1 :
        print("Ủa, a lô!!! Nhập cái gì có nghĩa đi pa, mắc cái giống j vậy -_-")
        return
    day_n_so = []
    for i in range(n):
        str = input("Nhập số nguyên dương thứ {0}: ".format(i+1))
        snd = int(str)
        if snd < 0:
            print("Vcl, wtf, đã bảo là nhập số nguyên dương mà -_-")
            return
        day_n_so.append(snd)

    kq = day_n_so[0]
    for i in range(1, n):
        kq = ucln(kq, day_n_so[i])
        if kq == 1:
            print(kq)
            return
    print(kq)


def bai7():
    a = -1+np.sqrt(5)
    b = 1+np.sqrt(5)
    c = 2/a
    d = -2/b
    e = 1 - np.sqrt(5)/5
    f = -1 - np.sqrt(5)/5

    n = int(input("Nhập số tự nhiên n = "))
    kq = e*(c**n)/a + f*(d**n)/b
    print(kq)


def bai8():
    x = float(input("Nhập số x = "))
    a = np.cbrt(np.sin(x))
    b = np.log(x) + 2**x
    c = np.tan(x)
    kq = a + b/c
    print(kq)

def f(x):
    if x < 1:
        return x
    if x == 1:
        return 0
    return np.exp(x)

def bai9():
    x = float(input("Nhập số x = "))
    print(f(x))


def do_lon_vector(v):
    return np.sqrt(v[0]**2+v[1]**2)


def bai10():
    cac_diem = []
    for i in range(3):
        str = input("Nhập tọa độ điểm thứ {0}: ".format(i+1))
        toa_do_diem = [float(x) for x in (str.strip().split())]
        toa_do_diem = np.array(toa_do_diem)
        cac_diem.append(toa_do_diem)

    cac_diem = np.array(cac_diem)

    diemA = cac_diem[0]
    diemB = cac_diem[1]
    diemC = cac_diem[2]

    vtcpAB = diemB-diemA
    vtcpBA = -vtcpAB
    vtcpBC = diemC-diemB
    vtcpCB = -vtcpBC
    vtcpCA = diemA-diemC
    vtcpAC = -vtcpCA


    cos_goc_ABC = vtcpBA.dot(vtcpBC)/(do_lon_vector(vtcpBA)*do_lon_vector(vtcpBC))
    cos_goc_BCA = vtcpCB.dot(vtcpCA)/(do_lon_vector(vtcpCB)*do_lon_vector(vtcpCA))
    cos_goc_BAC = vtcpAB.dot(vtcpAC)/(do_lon_vector(vtcpAB)*do_lon_vector(vtcpAC))

    goc_ABC = np.arccos(cos_goc_ABC)
    goc_BCA = np.arccos(cos_goc_BCA)
    goc_BAC = np.arccos(cos_goc_BAC)

    print(np.degrees(goc_ABC), np.degrees(goc_BCA), np.degrees(goc_BAC))



if __name__ == "__main__":
    x = int(input("chọn bài tập bằng cách nhập số từ 1 tới 10: "))
    if x == 1:
        bai1()
    if x == 2:
        bai2()
    if x == 3:
        bai3()
    if x == 4:
        bai4()
    if x == 5:
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
    if x < 1 or x > 10:
        print("không có bài tập phù hợp")
