# coding: UTF-8
import numpy as np
import random
import copy

# ビンゴカード作成関数
def make_bingo_card():
    b = ['01', '02', '03', '04', '05', '06',
         '07', '08', '09']+list(range(10, 16, 1))
    i = list(range(16, 31, 1))
    n = list(range(31, 46, 1))
    g = list(range(46, 61, 1))
    o = list(range(61, 76, 1))
    bingo_card = [random.sample(b, 5), random.sample(i, 5), random.sample(
        n, 5), random.sample(g, 5), random.sample(o, 5)]
    bingo_card = np.array(bingo_card).T.tolist()
    bingo_card[2][2] = '(  )'
    bingo_card = np.vectorize(str)(bingo_card)

    return bingo_card


# ビンゴカードを表示する関数
def print_bingo_card(bingo_card):
    for i, row in enumerate(bingo_card):
        for j, column in enumerate(row):
            if i == 2 and j == 2:
                print('FREE', end="")
            else:
                print(bingo_card[i][j].center(4), end="")
        print()

# ビンゴとリーチ数を数える関数
def count_bingo_reach(x, total_bingo, total_reach):
    if x == 5:
        total_bingo = total_bingo+1

    elif x == 4:
        total_reach = total_reach+1

    return total_bingo, total_reach


# ビンゴのボール作る
bingo_ball = ['01', '02', '03', '04', '05', '06',
              '07', '08', '09']+list(range(10, 76, 1))

# ビンゴカード作る
bingo_card = make_bingo_card()


# ランダムでボールを取り出してビンゴカードに穴を開ける
for ball in range(75):
    b_ball = random.choice(bingo_ball)
    print('ball['+str(ball+1)+']:'+str(int(b_ball)))
    bingo_ball.remove(b_ball)

    for i, row in enumerate(bingo_card):
        for j, column in enumerate(row):
            if bingo_card[i][j] == str(b_ball):
                bingo_card[i][j] = '('+str(bingo_card[i][j])+')'

    # ビンゴカードを表示する
    print_bingo_card(bingo_card)

    # ビンゴとリーチの数カウント
    total_bingo = 0
    total_reach = 0
    naname1 = 0
    naname2 = 0
    for count_i in range(5):
        tate = 0
        yoko = 0

        for count_j in range(5):
            if bingo_card[count_j][count_i].startswith('('):
                tate = tate+1

            if bingo_card[count_i][count_j].startswith('('):
                yoko = yoko+1

            if count_i == count_j and bingo_card[count_i][count_j].startswith('('):
                naname1 = naname1+1

            if count_i+count_j == 4 and bingo_card[count_i][count_j].startswith('('):
                naname2 = naname2+1

        total_bingo, total_reach = count_bingo_reach(
            tate, total_bingo, total_reach)

        total_bingo, total_reach = count_bingo_reach(
            yoko, total_bingo, total_reach)

    total_bingo, total_reach = count_bingo_reach(
        naname1, total_bingo, total_reach)

    total_bingo, total_reach = count_bingo_reach(
        naname2, total_bingo, total_reach)

    print()
    print('REACH: '+str(total_reach))
    print('BINGO: '+str(total_bingo))
    print('--------------------')
