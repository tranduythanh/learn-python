class DoThi:
    # Số đỉnh
    soDinh = 0

    # Số cạnh
    soCanh = 0

    # khai báo thuộc tính type để lưu kiểu đồ thị
    # - type = 0: đồ thị vô hướng
    # - type = 1: đồ thị có hướng
    type = 0   
    
    # khai báo thuộc tính DS để lưu trữ danh sách cạnh sau này
    DS = []    
    
    # khai báo thuộc tính MTK để lưu trữ ma trận kề sau này
    MTK = []   

    def ReadDSC(self, filename):
        # mở file 
        f1 = open(filename, 'r')

        # đọc dòng đầu tiên
        thongtin = f1.readline()

        # bẻ dòng đầu tiên ra thành 1 list, 
        # "khoảng trắng" chỗ nào thì bẻ ngay chỗ đó
        ds = thongtin.split()

        # Số đầu tiên chính là kiểu đồ thị
        self.type = int(ds[0])

        # Số thứ 2 là số đỉnh của đồ thị
        self.soDinh = int(ds[1])

        # Số thứ 3 là số cạnh của đồ thị
        self.soCanh = int(ds[2])
        
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

            # tieps tục bẻ dòng thành 1 list, 
            # "khoảng trắng" chỗ nào thì bẻ chỗ đó
            L1 = data.split()

            # Duyệt bằng for và chuyển đổi lần lượt 
            # từng phần tử từ kiểu string sang int
            L11 = [int(s) for s in L1]

            # Nhét cái danh sách này vào DS
            self.DS.append(L11)
        
        # đọc file xong nhớ gọi dòng này để đóng file lại
        f1.close()

        # trả ra danh sách cạnh đã đọc được
        return self.DS

    def ExportGraphInfo(self):
        print('Loại đồ thị:', self.type)
        print('Số đỉnh:', self.soDinh)
        print('Số cạnh:', self.soCanh)
        print('DS:', self.DS)

if __name__ == '__main__':
    filename = './dsc.txt'
    dt = DoThi()
    dt.ReadDSC(filename)
    dt.ExportGraphInfo()
