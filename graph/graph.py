class DOTHI:
    sodinh = 0
    socanh = 0
    type = 0     #kiểu đồ thị, type = 0: vô hướng, type = 1: có hướng
    DS = []
    def ReadDSC(self, filename):
        f1 = open(filename, 'r')
        thongtin = f1.readline()
        ds = thongtin.split()
        self.type = int(ds[0])
        self.sodinh = int(ds[1])
        self.socanh = int(ds[2])
        L = []
        while True:
            data = f1.readline()
            if data == '':
                break
            L1 = data.split()
            L11 = [int(s) for s in L1]
            self.DS.append(L11)
        f1.close()
        return self.DS
    def ExportGraphInfo(self):
        print('Loại đồ thị:', self.type)
        print('Số đỉnh:', self.sodinh)
        print('Số cạnh:', self.socanh)
        print('DS:', self.DS)

if __name__ == '__main__':
    filename = './dsc.txt'
    dt = DOTHI()
    dt.ReadDSC(filename)
    dt.ExportGraphInfo()
