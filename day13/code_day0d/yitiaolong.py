import random

def qipan(pan):
    '''展示棋盘'''
    for hang in range(3):
        lie = hang * 3
        print("{}   {}   {}".format(pan[lie], pan[lie + 1], pan[lie + 2]))


def win(pan):
    '''判断是否胜利'''
    winls = ["012", "345", "678", "036", "147", "258", "048", "246"]
    for win in winls:
        i = 0
        j = 0
        for intex_ in win:
            if pan[int(intex_)] == "O":
                i += 1
            if pan[int(intex_)] == "X":
                j += 1
        if i == 3:
            return True
        elif j == 3:
            return False
    return


def computer_zhineng(pan):
    '''机器人智能'''
    winls = ["012", "345", "678", "036", "147", "258", "048", "246"]
    yin = ""
    for win in winls:
        i = 0
        for intex_ in win:
            if pan[int(intex_)] == "X":
                i += 1
            elif pan[int(intex_)] != "O":
                yin = int(intex_)
            else:
                i -= 1
        if i == 2:
            return yin
    for win in winls:
        i = 0
        for intex_ in win:
            if pan[int(intex_)] == "O":
                i += 1
            elif pan[int(intex_)] != "X":
                yin = intex_
            else:
                i -= 1
        if i == 2:
            return int(yin)
    return None


def computer_xiaqi(pan):
    '''机器人下棋'''
    li = ["4", "0", "2", "6", "8", "1", "3", "5", "7"]
    if computer_zhineng(pan) != None:
        a = computer_zhineng(pan)
        return a
    else:
        for l in li:
            if pan[int(l)] != "O" and pan[int(l)] != "X":
                return int(l)


def bisai(pan):
    '''比赛开始'''
    qipan(pan)

    person = int(input("请下子(输入棋盘上的数字)"))
    pan[person] = "O"
    j = 0
    if win(pan) == True:
        return True
    elif win(pan) == False:
        return False
    for i in range(9):
        if pan[i] != str(i):
            j += 1
    if j == 9:
        return None
    '''
    机器人下棋
    '''
    xia = computer_xiaqi(pan)
    pan[xia] = "X"
    j = 0
    if win(pan) == True:
        return True
    elif win(pan) == False:
        return False
    for i in range(9):
        if pan[i] != str(i):
            j += 1
    if j == 9:
        return None
    return bisai(pan)


def main():
    pan = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    num = random.randint(1, 2)
    if num == 2:
        pan[computer_xiaqi(pan)] = "X"
    if bisai(pan) == True:
        print("真厉害你赢了")
    elif bisai(pan) == False:
        print("GAME OVER")
    else:
        print("平局")


main()