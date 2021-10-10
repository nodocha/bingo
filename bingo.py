
# coding: UTF-8
import numpy as np
import random
import copy

# ビンゴのボール作る
y1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
y2 = list(range(10, 76, 1))
bingo_ball = y1+y2
# bingo_ball=np.vectorize(str)(bingo_ball)

# ビンゴカード作る
b = ['01', '02', '03', '04', '05', '06',
     '07', '08', '09', 10, 11, 12, 13, 14, 15]
i = list(range(16, 31, 1))
n = list(range(31, 46, 1))
g = list(range(46, 61, 1))
o = list(range(61, 76, 1))
bingo_card = [random.sample(b, 5), random.sample(i, 5), random.sample(
    n, 5), random.sample(g, 5), random.sample(o, 5)]
bingo_card = np.array(bingo_card).T.tolist()
bingo_card[2][2] = 'FREE'
bingo_card = np.vectorize(str)(bingo_card)


# ランダムでボールを取り出してビンゴカードに穴を開ける
for ball in range(75):
    b_ball = random.choice(bingo_ball)
    print('ball['+str(ball+1)+']:'+str(int(b_ball)))
    bingo_ball.remove(b_ball)

    for i, row in enumerate(bingo_card):
        for j, column in enumerate(row):
            if bingo_card[i][j] == str(b_ball):
                bingo_card[i][j] = '('+str(bingo_card[i][j])+')'

# ビンゴとリーチのカウント用にビンゴカードを複製
    bc_count = copy.copy(bingo_card)
    bc_count[2][2] = '(100)'

# ビンゴカード表示用にビンゴカードを複製
    bc_output = copy.copy(bingo_card)

# ビンゴカードを見やすいように整形し表示する
    for x, row2 in enumerate(bc_output):
        for y, column2 in enumerate(row2):
            bc_output[x][y] = bc_output[x][y].center(4)
    for a in bc_output:
        print(*a)

# ビンゴとリーチの数カウント
    total_bingo = 0
    total_reach = 0
    naname1 = 0
    naname2 = 0
    for count_i in range(5):
        tate = 0
        yoko = 0

        for count_j in range(5):
            if bc_count[count_j][count_i].startswith('('):
                tate = tate+1

            if bc_count[count_i][count_j].startswith('('):
                yoko = yoko+1

            if count_i == count_j and bc_count[count_i][count_j].startswith('('):
                naname1 = naname1+1

            if count_i+count_j == 4 and bc_count[count_i][count_j].startswith('('):
                naname2 = naname2+1

            if count_j == 4:
                if tate == 5:
                    total_bingo = total_bingo+1
                elif tate == 4:
                    total_reach = total_reach+1

                if yoko == 5:
                    total_bingo = total_bingo+1
                elif yoko == 4:
                    total_reach = total_reach+1

            if count_i == 4 and count_j == 4:
                if naname1 == 5:
                    total_bingo = total_bingo+1
                elif naname1 == 4:
                    total_reach = total_reach+1

                if naname2 == 5:
                    total_bingo = total_bingo+1
                elif naname2 == 4:
                    total_reach = total_reach+1

    print()
    print('REACH: '+str(total_reach))
    print('BINGO: '+str(total_bingo))
    print('--------------------')
