import random
import os
import time

global borw, validp, d_record, AI_board
borw = True
validp = []
d_record = []
AI_board = []

def initial():                              #將矩陣初始化
    global validp
    for i in range(19):
        for j in range(19):
            validp.append((i,j))

def winning(getmcts = True):
    global d_record,  d_recordtmp           
    if getmcts:
        d_recordtmp2 = d_recordtmp
    else:
        d_recordtmp2 = d_record
    final_move =d_recordtmp2[-1]
                    # 橫     # 直     # 右上左下     # 左上右下
    for (i, j) in [(1, 0), (0, 1), (1, 1), (1, -1)]:
        line = 1
        for k in range(4):                            #檢查由方向上負方向的棋子連成的個數
            (i_tmp, j_tmp) = (final_move[0] - (i*(k+1)), final_move[1] - (j*(k+1)))
            try:
                if ((d_recordtmp2.index((i_tmp, j_tmp))+1) % 2) == (len(d_recordtmp2) % 2):
                    line += 1
                else:
                    break
            except:
                break
        for k in range(4):                             #檢查由方向上正方向的棋子連成的個數
            (i_tmp, j_tmp) = (final_move[0] + (i*(k+1)), final_move[1] + (j*(k+1)))
            try:
                if ((d_recordtmp2.index((i_tmp, j_tmp))+1) % 2) == (len(d_recordtmp2) % 2):
                    line += 1
                else:
                    break
            except:
                break
        if line >= 5:                                   #判斷若連成的棋子個數超過5個則贏了
            return True
    return False

def randPlay():
    global validp_tmp, d_recordtmp
    while True:
        if winning():
            return len(d_recordtmp) % 2
        try:
            vpt = random.choice(validp_tmp)                #隨機選擇在剩下棋盤中可以下的地方
        except:
            return -1
        d_recordtmp.append((vpt[0], vpt[1]))
        validp_tmp.remove(vpt)

def MonteCarlo():
    
    print('\n', end='')

    global validp_tmp, d_recordtmp
    score_list = [ [ vp[0], vp[1], 0, 0 ] for vp in validp ]

    for i in range(19):
        for j in range(len(score_list)):
            for k in range(50):

                d_recordtmp = [ dr for dr in d_record ]
                validp_tmp = [ (sl[0], sl[1]) for sl in score_list ]
                vpt = validp_tmp[j]
                d_recordtmp.append(vpt)
                validp_tmp.remove(vpt)

                win = randPlay()
                if win == ((d_recordtmp.index(vpt)+1) % 2):
                    score_list[j][2] += 1
                elif win != -1:
                    score_list[j][2] -= 1
                score_list[j][3] += 1

        score_list = sorted(score_list, reverse = True, key = lambda sl: sl[2] / sl[3])
        length = 1 if (len(score_list) / 3) < 1 else int(len(score_list) / 3)
        score_list = score_list[:length]

        if length == 1:
            break

    return score_list[0]

'''
def AI ():
{
    board 
    maxcount[19][19] = {0}
    for i in range(19)
        for j in range(19)
            board = MonteCarlo():             #對整個棋盤進行蒙地卡羅搜索法
            maxcount[board[0]][board[1]] += 1 

    top_winner[4] = {0}
    for i in range(19)                              #找出經過蒙地卡羅搜索法後，經常勝利的點
        for j in range(19)
            if(maxcount[i][j] > top_winner [0])
                top_winner[0] = maxcount[i][j]
                top_winner[1] = i
                top_winner[2] = j
    return top_winner
}
'''


def main():
    initial()

    global validp, d_record

    while True:
        choice = MonteCarlo()
        os.system("cls")
        color = "black" if len(d_record) % 2 == 0 else "white"
        d_record.append((choice[0], choice[1]))
        validp.remove((choice[0], choice[1]))

        print('\n', end='')
        for j in range(19):
            for i in range(19):
                if (i, j) in d_record:
                    if (d_record.index((i, j))+1) % 2 == 0:
                        print('●', end='')
                    else:
                        print('○', end='')
                elif (i, j) == (0, 0):
                    print('┌ ', end='')
                elif (i, j) == (0, 18):
                    print('└ ', end='')
                elif (i, j) == (18, 0):
                    print('┐ ', end='')
                elif (i, j) == (18, 12):
                    print('┘ ', end='')
                elif i == 0:
                    print('├ ', end='')
                elif i == 18:
                    print('┤ ', end='')
                elif j == 0:
                    print('┬ ', end='')
                elif j == 18:
                    print('┴ ', end='')
                else:
                    print('┼ ', end='')
            print('\n', end='')

        if winning(False):
            if (len(d_record)-1) % 2 == 0:
                print("\nPlayer black win!")
            else:
                print("\nPlayer white win!")
            break



if __name__ == "__main__":
    main()