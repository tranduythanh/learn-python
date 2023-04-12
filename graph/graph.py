#============================================================
#Tao mot lop chua thong tin do thi
class DOTHI:
    sodinh = 0
    socanh = 0

    # khai báo thuộc tính type để lưu kiểu đồ thị
    # - type = 0: đồ thị vô hướng
    # - type = 1: đồ thị có hướng
    type = 0

    # khai báo thuộc tính DS để lưu trữ danh sách cạnh sau này
    DS = []

    # khai báo thuộc tính MTK để lưu trữ ma trận kề sau này
    MTKe = []
    
    # Khởi tạo giá trị đầu cho các thuộc tính của DOTHI
    def __int__(self):
        self.sodinh = 0
        self.socanh = 0
        self.type = 0
        self.DS = []

    
    def DocDS_TuFile(self, TenFile):
        # mở file
        f1 = open(TenFile, 'r')

        # đọc dòng đầu tiên
        thongtin = f1.readline()

        # bẻ dòng đầu tiên ra thành 1 list, 
        # "khoảng trắng" chỗ nào thì bẻ ngay chỗ đó
        ds = thongtin.split()

        # Số đầu tiên chính là kiểu đồ thị
        self.type = int(ds[0])
        
        # Số thứ 2 là số đỉnh của đồ thị
        self.sodinh = int(ds[1])
        
        # Số thứ 3 là số cạnh của đồ thị
        self.socanh = int(ds[2])

        # Khởi tạo biến L là list rỗng 
        # để xài trong while ngay bên dưới
        L = []
        
        while True:
            # lần lượt đọc dòng tiếp theo
            data = f1.readline()

            # nếu đó là dòng trống trơn, thì tức 
            # là đọc đến cuối file rồi, dẹp nghỉ
            if data == '':
                break

            # tiếp tục bẻ dòng thành 1 list, 
            # "khoảng trắng" chỗ nào thì bẻ chỗ đó
            L1 = data.split()

            # Duyệt bằng for và chuyển đổi lần lượt 
            # từng phần tử từ kiểu string sang int
            L11 = [int(s) for s in L1]

            # Nhét cái danh sách này vào DS
            self.DS.append(L11)

        # đọc file xong nhớ gọi dòng này để đóng file lại
        f1.close()

        return self.DS
    
    #Xuat thong tin do thi
    def XuatThongTin_DT(self):
        print("Loai do thi:", self.type)
        print("So dinh:", self.sodinh)
        print("So canh:", self.socanh)
        print("DS:", self.DS)
    
    def ChuyenDSCanh_to_MTKe(self):
        for i in range(self.sodinh):
            L = []
            for j in range(self.sodinh):
                L.append(0)
            self.MTKe.append(L)
        for canh in self.DS:
            dinhdau = canh[0]
            dinhcuoi = canh[1]
            self.MTKe[dinhdau-1][dinhcuoi-1] = 1
            if self.type == 0:
                self.MTKe[dinhcuoi-1][dinhdau-1] = 1
        
        return self.MTKe
#+++++++++++++++++++++++++++++++++++++++++++++++++++++


def MAIN():
    TenFile_DSCanh = 'dsc.txt'
    dt = DOTHI()
    dt.DocDS_TuFile(TenFile_DSCanh)
    dt.XuatThongTin_DT()

    dt.ChuyenDSCanh_to_MTKe()
    print(dt.MTKe)

MAIN()