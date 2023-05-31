import math

_ = math.inf


# Dĩ nhiên, khoảng cách từ đỉnh bắt đầu đến chính nó là 0.
# Các khoảng cách từ đỉnh bắt đầu đến các đỉnh khác ta tạm
# cho là dương vô cùng. Ta sẽ cập nhật sau.




def getVsOfUi(G, S, ui):
    ret = []
    for v in S:
        w = G[ui][v]
        if w == _:
            continue
        ret.append(v)
    return ret

def updateMarkOfV(G, ui, v, marks):
    # Trong số của cạnh ui---v
    w = G[ui][v]

    Lui = marks[ui][0]
    newL = Lui + w
    
    Lv = marks[v][0]
    if Lv < newL:
        return marks
    
    marks[v] = (newL, ui)
    return marks

def updateMarks(G, S, ui, marks):
    vs = getVsOfUi(G, S, ui)
    print("all v in S: ", vs)
    for v in vs:
        marks = updateMarkOfV(G, ui, v, marks)
    return marks

def minMarksIdx(S, marks):
    # chỉ lấy các đỉnh trong S
    minL = _
    ret = None
    for v, mark in enumerate(marks):
        # chỉ xét các đỉnh trong S. Nên
        # nếu đỉnh này không nằm trong S
        # thì mình bỏ qua
        if v not in S:
            continue

        if mark[0] >= minL:
            continue
        
        minL = mark[0]
        ret = v
    return ret

def step2(G, S, ui, marks):
    
    # Loại đỉnh hiện tại ra khỏi danh sách S
    S.remove(ui)

    # cập nhật marks
    print("S  = ",S)
    print("ui = ",ui)

    # Cập nhật lại danh sách đánh dấu các đính
    marks = updateMarks(G, S, ui, marks)
    print("marks =", marks)

    # Lấy đỉnh tiếp theo, là đỉnh có giá trị L(v)
    # nhỏ nhất, với v là các đỉnh trong S
    ui = minMarksIdx(S, marks)

    return ui, marks


    # a  b  c  d  e  f  g  h
G = [[0, 4, _, _, _, _, 6, 2], # a
     [4, 0, 5, 6, _, 2, _, 1], # b
     [_, 5, 0, 3, 1, _, _, _], # c
     [_, 6, 3, 0, 5, 5, _, _], # d
     [_, _, 1, 5, 0, 1, _, _], # e
     [_, 2, _, 5, 1, 0, 9, 8], # f
     [6, _, _, _, _, 9, 0, 2], # g
     [2, 1, _, _, _, 8, 2, 0]] # h

def main():
    # số đỉnh 
    n = len(G)

    # Danh sách tất cả các đỉnh
    V = []
    for i in range(n):
        V.append(i)


    # Đỉnh bắt đầu đề cho là đỉnh a, là đỉnh đầu tiên trong V
    ui = 0

    # tạo danh sách S
    S = V.copy()

    # Tạo danh sách đánh dấu các đỉnh. Mỗi đỉnh ta đánh dấu 2 thông tin
    # 1: giá trị L(v)
    # 2: đỉnh cha của đỉnh hiện tại
    marks = []
    for i in range(n):
        marks.append( (_, None) )
    marks[ui]=(0, ui)


    print("V     =", V)
    print("S     =", S)
    print("marks =", marks)

    # Bắt đầu vòng lặp
    i = 0
    while i < n-1:
        print(f'\n----------- {i}----------')
        ui, marks = step2(G, S, ui, marks)
        i += 1

    print("Kết quả cuối cùng:")
    print(marks)

    print(marks[4])

main()