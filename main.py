from chessPieces import *

from tkinter import *

import tkinter.font as tkFont

from tkinter import messagebox

import random

import time

import copy


#象棋列表
list_chess = []


copy_list_chess = []

#当前点击的棋子
click_item = {}

#象棋chessBtn字典
dict_chessBtn = {}



def find_move_location(click_location):
    """
    通过棋盘的位置点击，寻找最近的棋盘可走位置
    :param click_location:
    :return:
    """
    for i in range(len(list_position)):
        for j in range(len(list_position[i])):
            chess_one = list_position[i][j]
            if abs(chess_one[0] - click_location[0])<50 and abs(chess_one[1] - click_location[1])<50:

                #点击的点有子，则不做处理
                for item in list_chess:
                    if chess_one == item.position:
                        return None

                return chess_one

def warn(chess):
    """
    棋子提示警告色后恢复原色
    :param chess:
    :return:
    """
    chess_btn = dict_chessBtn[chess.id]
    bg = chess_btn['bg']
    chess_btn['bg'] = "#CC66FF"
    root.update()
    time.sleep(1)
    chess_btn['bg'] = bg
    dict_chessBtn[chess.id] = chess_btn
    root.update()

def find_index(move_location):
    """
    找寻位置下标
    :param move_location:  从位置找下标
    :return:
    """
    for i in range(len(list_position)):
        for j in range(len(list_position[i])):
            chess_one = list_position[i][j]
            if chess_one == move_location:
                return (i,j)


def simulate_move(chess,position):
    """
    　模拟移动后返回copy列表，如果消灭了子并返回消灭子都权重
    :param chess:  棋子
    :param position:　目标位置
    :return:
    """
    copy_list_chess = copy.deepcopy(list_chess)
    for item in copy_list_chess:
        if item.position == position:
            copy_list_chess.remove(item)
        elif item.position == chess.position:
            # 更新坐标
            item.position = position
            # 更新列表中的下标位置,并重置原属性
            item.pos_in_list = find_index(position)
    return copy_list_chess


def judge_king(copy_list_chess,color):
    """
    判断如果该子走到目标位置，是否被将军
    :param copy_list_chess: 模拟列表
    :param color 移动棋子
    :return:
    """

    # 王位
    king_position = None


    for item in copy_list_chess:
        if color == "black" and item.name == "将":
            king_position = item.position
        elif color == "red" and item.name == "帅":
            king_position = item.position

    for item in [one for one in copy_list_chess if one.color != color]:
        if king_position in item.get_passable_positions(copy_list_chess):
            return False

    return True


def judge_can_move(chess,position):
    """
    判断该位置是否可以移动
    :param chess:  焦点棋子
    :param position:　目标位置
    :return: True 可以移动　　False 不可移动
    """

    # 符合移动条件
    passable_positions = chess.get_passable_positions(list_chess)
    if passable_positions and position in passable_positions:

        #模拟移动
        copy_list_chess = simulate_move(chess, position)

        if judge_king(copy_list_chess,chess.color):
            return True
        else:
            warn(chess)
            return False

    else:
        warn(chess)
        return False


def click_chessboard(event):

    """
    棋盘点击事件
    :param event:
    :return:
    """
    if click_item:
        #移动棋子
        chess = click_item["data"]

        move_location =  find_move_location((event.x, event.y))

        #待移动位置
        if move_location and judge_can_move(chess,move_location):

            #更新列表中棋子的新位置
            refresh_list_chess(chess,move_location)

            # 保存走子状态
            copy_list_chess.append(copy.deepcopy(list_chess))




root = Tk(className = "中国象棋")
root.geometry("800x800")


img_gif = PhotoImage(file = 'image/chess.gif')
label_img = Label(root, image = img_gif)
label_img.bind("<Button-1>", click_chessboard)
label_img.pack()


def remove_data_in_list_chess(old_chess):
    """
    删除被吃掉的子
    :param old_chess: 废弃子
    :return:
    """
    for item in list_chess:
        if old_chess.position == item.position:
            list_chess.remove(item)
            break

def delete(chess):
    """
    删除控件
    :return:
    """
    #清除棋子按钮
    dict_chessBtn[chess.id].place_forget()
    del dict_chessBtn[chess.id]

    # 删除列表中位置
    remove_data_in_list_chess(chess)

def get_best_edible_chess(chess):
    """
    最优可吃子,根据权重判断
    :return:
    """
    passable_positions = chess.get_passable_positions(list_chess)
    edible_chesses = []
    for i in range(len(list_chess)):
        chess_one = list_chess[i]
        #可吃并且不被将军
        copy_list_chess = simulate_move(chess,chess_one.position)
        if chess_one.position in passable_positions and judge_king(copy_list_chess,chess.color):
            edible_chesses.append(chess_one)

    best_chess = None
    for item in edible_chesses:

        if not best_chess:
            best_chess = item
            continue

        if best_chess and item.weight > best_chess.weight:
            best_chess = item

    return best_chess


def choice_best_plan(list_possible):
    """
    从列表中寻找最优走法
    :param list_possible: 可走列表
    :return:
    """

    best_index = None
    best_choice = None

    for i in range(len(list_possible)):
        item = list_possible[i]
        best_edible_chess =get_best_edible_chess(item)
        if best_edible_chess:
            if not best_choice:
                best_choice = best_edible_chess
                best_index = i
            elif best_edible_chess.weight > best_choice.weight:
                best_choice = best_edible_chess
                best_index = i


    if best_choice:
        return (best_index,best_choice.position)
    else:
        # 随机选一个子,和一个随机位置
        random_index = random.randint(0, len(list_possible) - 1)
        random_chess = list_possible[random_index]
        passable_positions = random_chess.get_passable_positions(list_chess)
        random_position = passable_positions[random.randint(0, len(passable_positions) - 1)]
        return (random_index,random_position)




def refresh_list_chess(chess,move_location):
    """
     刷新原列表中该棋子的位置
    :param chess:  原棋子数据
    :param move_location: 新位置
    :return:
    """
    for item in list_chess:
        if chess.position == item.position:
            #更新坐标
            item.position = move_location
            #更新列表中的下标位置,并重置原属性
            item.pos_in_list = find_index(move_location)
            dict_chessBtn[item.id]['bg'] = "#d1b07e"
            dict_chessBtn[item.id].place(x=move_location[0], y=move_location[1])
            #移除当前焦点
            del click_item["data"]

    # 行动的是红子，则下一步黑子行动
    if chess.color == "red":

        # 黑将位置
        list_black_king = [item for item in list_chess if
                           item.color == "black" and item.name == "将"]
        # 红子可走
        enable_red_chesses = [item for item in list_chess if
                              item.color == "red" and item.get_passable_positions(list_chess)]

        # 判断这会黑子是否处于被将军状态
        bool_call_the_general = False

        # 无黑将则提示红方胜利
        if not list_black_king:
            messagebox.askokcancel('消息框', '你赢了！！！')
            return

        # 判断被将军
        for item in enable_red_chesses:
            if list_black_king[0].position in item.get_passable_positions(list_chess):
                bool_call_the_general = True
                break

        enable_black_chesses = [item for item in list_chess if
                                item.color == "black" and item.get_passable_positions(list_chess)]

        # 如果被将军，则遍历可走子位置
        if bool_call_the_general:
            # 循环找解将的方法,如果循环完毕没解决则判定红方胜
            # 寻找目标位置
            # 随机走一步不被将军的位置

            result_item = None
            result_position = None

            for item in enable_black_chesses:
                passable_positions = item.get_passable_positions(list_chess)
                for pos in passable_positions:
                    copy_list_chess = simulate_move(item, pos)
                    if judge_king(copy_list_chess, item.color):
                        result_item = item
                        result_position = pos
                        break
                else:
                    continue

                break

            # 无子可走
            if not result_item:
                messagebox.askokcancel('消息框', '你赢了！！！')
                return
            else:
                # 移动位置有子则删除该子
                for item in list_chess:
                    if result_position == item.position:
                        delete(item)
                        break

                # 更新下标
                result_item.position = result_position
                result_item.pos_in_list = find_index(result_position)
                dict_chessBtn[result_item.id].place(x=result_position[0], y=result_position[1])


        else:

            if enable_black_chesses:

                choice_index = None
                choice_position = None

                # 直到找到一种不被将军的走法
                while True:
                    choice = choice_best_plan(enable_black_chesses)
                    choice_index = choice[0]
                    choice_position = choice[1]
                    copy_list_chess = simulate_move(enable_black_chesses[choice_index], choice_position)
                    if judge_king(copy_list_chess, enable_black_chesses[choice_index].color):
                        break

                # 移动位置有子则删除该子
                for item in list_chess:
                    if choice_position == item.position:
                        delete(item)
                        break

                # 更新下标
                enable_black_chesses[choice_index].position = choice_position
                enable_black_chesses[choice_index].pos_in_list = find_index(choice_position)

                dict_chessBtn[enable_black_chesses[choice_index].id].place(x=choice_position[0],
                                                                           y=choice_position[1])


def click(chess):
    """
    棋子点击
    :param chess:
    :return:
    """
    if click_item:
        # 颜色相同则切换焦点棋子
        if click_item["data"].color == chess.color:

            # 该次点击和上次点击相同
            if click_item["data"].position == chess.position:
                if dict_chessBtn[click_item["data"].id]["bg"] == "yellow":
                    dict_chessBtn[click_item["data"].id]["bg"] = "#d1b07e"
                    del click_item["data"]
                else:
                    dict_chessBtn[click_item["data"].id]["bg"] = "yellow"
                    click_item["data"] = chess

            else:  # 点击变黄色背景　并且标记
                dict_chessBtn[chess.id]["bg"] = "yellow"
                dict_chessBtn[click_item["data"].id]["bg"] = "#d1b07e"
                click_item["data"] = chess

        # 颜色不同
        else:

            if judge_can_move(click_item["data"], chess.position):

                # 首先从列表中删除当前点的子
                delete(chess)

                if chess.name == "将":
                    messagebox.askokcancel('消息框', '你赢了！！！')
                elif chess.name == "帅":
                    messagebox.askokcancel('消息框', '你输了！！！')
                else:
                    # 更新焦点子为当前子的位置
                    refresh_list_chess(click_item["data"], chess.position)

                    # 保存走子状态
                    copy_list_chess.append(copy.deepcopy(list_chess))



    else:

        # 黑色为自动走子,不允许点黑色子
        if chess.color == "black":
            return

        # 点击变黄色背景　并且标记
        dict_chessBtn[chess.id]["bg"] = "yellow"
        click_item["data"] = chess


def init_btn(chess):
    """
        创建棋子对象
    :param chess:　棋子
    :return:
    """
    ft = tkFont.Font(family='微软雅黑', size=20, weight=tkFont.BOLD)
    btn = Button(root, text=chess.name, bg="#d1b07e", fg=chess.color, font=ft,
                                 height="1", width="1", command=lambda : click(chess))
    btn.pack()

    btn.place(x=chess.position[0], y=chess.position[1])


    # 添加到象棋列表
    list_chess.append(chess)
    dict_chessBtn[chess.id] = btn


#***********************************************************
#重置
def reset(list_temp):
    list_chess.clear()
    click_item.clear()
    for item in dict_chessBtn.values():
        item.place_forget()
    dict_chessBtn.clear()
    for item in list_temp:
        init_btn(item)


    copy_list_chess[-1] = copy.deepcopy(list_chess)


#重新开始
def restart():
    list_temp = copy_list_chess[0]
    copy_list_chess.clear()
    copy_list_chess.append(list_temp)
    reset(list_temp)


ft = tkFont.Font(family='微软雅黑', size=12, weight=tkFont.BOLD)
btn_restart = Button(root, text="重新开始", bg="#d1b07e", fg="red", font=ft,
                                 height="1", width="4", command=restart)
btn_restart.pack()
btn_restart.place(x=735, y=430)

#悔棋
def regret_game():
    if len(copy_list_chess) <= 1:
        return

    if len(copy_list_chess) > 1:
        copy_list_chess.pop()
    list_temp = copy_list_chess[-1]
    reset(list_temp)

ft = tkFont.Font(family='微软雅黑', size=12, weight=tkFont.BOLD)
btn_regret_game =Button(root, text="　悔棋　", bg="#d1b07e", fg="black", font=ft,
                                 height="1", width="4", command=regret_game)
btn_regret_game.pack()
btn_regret_game.place(x=735,y=350)
#左黑车
black_left_rook = Rook("black_left_rook","車","black",(0,0),100)
init_btn(black_left_rook)

#右黑车
black_right_rook = Rook("black_right_rook","車","black",(0,8),100)
init_btn(black_right_rook)

#左红车
red_left_rook = Rook("red_left_rook","車","red",(9,0),100)
init_btn(red_left_rook)

#右红车
red_right_rook = Rook("red_right_rook","車","red",(9,8),100)
init_btn(red_right_rook)

#***********************************************************
#左黑马
black_left_knight = Knight("black_left_knight","馬","black",(0,1),80)
init_btn(black_left_knight)

#右黑马
black_right_knight = Knight("black_right_knight","馬","black",(0,7),80)
init_btn(black_right_knight)

#左红马
red_left_knight = Knight("red_left_knight","馬","red",(9,1),80)
init_btn(red_left_knight)

#右红马
red_right_knight = Knight("red_right_knight","馬","red",(9,7),80)
init_btn(red_right_knight)


#***********************************************************
#左黑象
black_left_minister = Minister("black_left_minister","象","black",(0,2),30)
init_btn(black_left_minister)

#右黑象
black_right_minister = Minister("black_right_minister","象","black",(0,6),30)
init_btn(black_right_minister)

#左红相
red_left_minister = Minister("red_left_minister","相","red",(9,2),30)
init_btn(red_left_minister)

#右红相
red_right_minister = Minister("red_right_minister","相","red",(9,6),30)
init_btn(red_right_minister)


#***********************************************************
#左黑士
black_left_guard = Guard("black_left_guard","士","black",(0,3),40)
init_btn(black_left_guard)

#右黑士
black_right_guard = Guard("black_right_guard","士","black",(0,5),40)
init_btn(black_right_guard)


#左红仕
red_left_guard = Guard("red_left_guard","仕","red",(9,3),40)
init_btn(red_left_guard)


#右红仕
red_right_guard = Guard ("red_right_guard","仕","red",(9,5),40)
init_btn(red_right_guard)


#***********************************************************
#黑将
black_king = King("black_king","将","black",(0,4),200)
init_btn(black_king)


#红帅
red_king = King("red_king","帅","red",(9,4),200)
init_btn(red_king)


#***********************************************************
#左黑炮
black_left_gun = Gun("black_left_gun","炮","black",(2,1),90)
init_btn(black_left_gun)

#右黑炮
black_right_gun = Gun("black_right_gun","炮","black",(2,7),90)
init_btn(black_right_gun)

#左红炮
red_left_gun = Gun("red_left_gun","炮","red",(7,1),90)
init_btn(red_left_gun)


#右红炮
red_right_gun = Gun("red_right_gun","炮","red",(7,7),90)
init_btn(red_right_gun)

#***********************************************************
#黑卒１
black_pawn1 = Pawn("black_pawn1","卒","black",(3,0),1)
init_btn(black_pawn1)

#黑卒2
black_pawn2 = Pawn("black_pawn2","卒","black",(3,2),1)
init_btn(black_pawn2)

#黑卒3
black_pawn3 = Pawn("black_pawn3","卒","black",(3,4),1)
init_btn(black_pawn3)

#黑卒4
black_pawn4 = Pawn("black_pawn4","卒","black",(3,6),1)
init_btn(black_pawn4)

#黑卒5
black_pawn5 = Pawn("black_pawn5","卒","black",(3,8),1)
init_btn(black_pawn5)

#红兵１
red_pawn1 = Pawn("red_pawn1","兵","red",(6,0),1)
init_btn(red_pawn1)

#红兵2
red_pawn2 = Pawn("red_pawn2","兵","red",(6,2),1)
init_btn(red_pawn2)

#红兵3
red_pawn3 = Pawn("red_pawn3","兵","red",(6,4),1)
init_btn(red_pawn3)

#红兵4
red_pawn4 = Pawn("red_pawn4","兵","red",(6,6),1)
init_btn(red_pawn4)

#红兵5
red_pawn5 = Pawn("red_pawn5","兵","red",(6,8),1)
init_btn(red_pawn5)

#******************************************



root.update()
copy_list_chess.append(copy.deepcopy(list_chess))
root.mainloop()