from tkinter import *

import tkinter.font as tkFont


#棋盘列表
list_position = [
    [(62,25), (140,25), (220,25), (300,25), (379,25), (459,25), (538,25), (617,25), (695,25)],
    [(62,100),(140,100),(220,100),(300,100),(379,100),(459,100),(538,100),(617,100),(695,100)],
    [(62,180),(140,180),(220,180),(300,180),(379,180),(459,180),(538,180),(617,180),(695,180)],
    [(62,260),(140,260),(220,260),(300,260),(379,260),(459,260),(538,260),(617,260),(695,260)],
    [(62,340),(140,340),(220,340),(300,340),(379,340),(459,340),(538,340),(617,340),(695,340)],
    [(62,420),(140,420),(220,420),(300,420),(379,420),(459,420),(538,420),(617,420),(695,420)],
    [(62,500),(140,500),(220,500),(300,500),(379,500),(459,500),(538,500),(617,500),(695,500)],
    [(62,580),(140,580),(220,580),(300,580),(379,580),(459,580),(538,580),(617,580),(695,580)],
    [(62,660),(140,660),(220,660),(300,660),(379,660),(459,660),(538,660),(617,660),(695,660)],
    [(62,740),(140,740),(220,740),(300,740),(379,740),(459,740),(538,740),(617,740),(695,740)]
]

#象棋列表
list_chess = []

#当前点击的棋子
click_item = {}


class Chess:
    def __init__(self, root,name,color,position):
        """

        :param root: 全局画布
        :param name: 棋子名称
        :param color: 棋子颜色
        :param position: 棋子位置
        """
        self.color = color
        self.position = position

        ft = tkFont.Font(family='微软雅黑', size=20, weight=tkFont.BOLD)
        self.btn = Button(root,text=name, bg="#d1b07e",fg=color, font=ft,height = "1",width = "1", command=self.click)
        self.btn.pack()
        self.btn.place(x=position[0], y=position[1])

        #添加到象棋列表
        list_chess.append(self)
    def click(self):

        #连续点子
        if click_item:
            #颜色相同则切换焦点棋子
            if click_item["data"].color == self.color:

                #该次点击和上次点击相同
                if click_item["data"].position == self.position :
                    if click_item["data"].btn["bg"] == "yellow":
                        click_item["data"].btn['bg'] = "#d1b07e"
                        del click_item["data"]
                    else:
                        click_item["data"].btn['bg'] = "yellow"
                        click_item["data"] = self

                else: # 点击变黄色背景　并且标记
                    self.btn['bg'] = "yellow"
                    click_item["data"].btn['bg'] = "#d1b07e"
                    click_item["data"]= self
            #颜色不同暂时消灭该子
            else:

                #更新当前棋子位置
                refresh_list_chess(click_item["data"],self.position)

                #获得目标子坐标给焦点子
                click_item["data"].btn['bg'] = "#d1b07e"
                click_item["data"].btn.place(x=self.position[0], y=self.position[1])
                del click_item["data"]
                self.delete()
        else:
            # 点击变黄色背景　并且标记
            self.btn['bg'] = "yellow"
            click_item["data"] = self

    def delete(self):
        """
        删除控件
        :return:
        """
        self.btn.place_forget()
        #删除列表中位置
        remove_data_in_list_chess(self)


root = Tk(className = "中国象棋")
root.geometry("800x800")

def find_move_location(click_location):
    """
    找寻具体移动位置
    :param click_location:
    :return:
    """
    for i in range(len(list_position)):
        for j in range(len(list_position[i])):
            chess_one = list_position[i][j]
            if abs(chess_one[0] - click_location[0])<40 and abs(chess_one[1] - click_location[1])<40:

                #点击的点有子，则不做处理
                for item in list_chess:
                    if chess_one == item.position:
                        return None
                        # item.delete()
                        # break

                return chess_one

def refresh_list_chess(chess,move_location):
    """
    刷新原来位置
    :param chess:  原棋子数据
    :param move_location: 新位置
    :return:
    """
    for item in list_chess:
        if chess.position == item.position:
            chess.position = move_location
            break

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


def showlocation(event):
    """
    棋盘点击事件
    :param event:
    :return:
    """

    # print(len(list_chess))
    # print(click_item)
    # print(event.x,event.y)
    if click_item:
        #移动棋子
        chess = click_item["data"]

        move_location =  find_move_location((event.x, event.y))

        if move_location:
            #更新列表中棋子的新位置
            refresh_list_chess(chess,move_location)

            chess.btn.place(x=move_location[0], y=move_location[1])
            chess.btn['bg'] = "#d1b07e"
            del click_item["data"]


#  車      馬         象        士      将     炮    兵/卒
# rook   knight   minister   guard   king　  gun   Pawn
#位置都是从画布的左往右

img_gif = PhotoImage(file = 'image/chess.gif')
label_img = Label(root, image = img_gif)
label_img.bind("<Button-1>", showlocation)
label_img.pack()

#左黑车
pos_black_left_rook = list_position[0][0]
black_left_rook = Chess(root,"車","black",pos_black_left_rook)

#左黑马
pos_black_left_knight = list_position[0][1]
black_left_knight = Chess(root,"馬","black",pos_black_left_knight)

#左黑象
pos_black_left_minister = list_position[0][2]
black_left_minister = Chess(root,"象","black",pos_black_left_minister)

#左黑士
pos_black_left_guard = list_position[0][3]
black_left_guard = Chess(root,"士","black",pos_black_left_guard)

#黑将
pos_black_king = list_position[0][4]
black_king = Chess(root,"将","black",pos_black_king)

#右黑士
pos_black_right_guard = list_position[0][5]
black_right_guard = Chess(root,"士","black",pos_black_right_guard)

#右黑象
pos_black_right_minister = list_position[0][6]
black_right_minister = Chess(root,"象","black",pos_black_right_minister)

#右黑马
pos_black_right_knight = list_position[0][7]
black_right_knight = Chess(root,"馬","black",pos_black_right_knight)

#右黑车
pos_black_right_rook = list_position[0][8]
black_right_rook = Chess(root,"車","black",pos_black_right_rook)

#左黑炮
pos_black_left_gun = list_position[2][1]
black_left_gun = Chess(root,"炮","black",pos_black_left_gun)

#右黑炮
pos_black_right_gun = list_position[2][7]
black_right_gun = Chess(root,"炮","black",pos_black_right_gun)

#黑卒１
pos_black_pawn1 = list_position[3][0]
black_black_pawn1 = Chess(root,"卒","black",pos_black_pawn1)

#黑卒2
pos_black_pawn2 = list_position[3][2]
black_black_pawn2 = Chess(root,"卒","black",pos_black_pawn2)

#黑卒3
pos_black_pawn3 = list_position[3][4]
black_black_pawn3 = Chess(root,"卒","black",pos_black_pawn3)

#黑卒4
pos_black_pawn4 = list_position[3][6]
black_black_pawn4 = Chess(root,"卒","black",pos_black_pawn4)

#黑卒5
pos_black_pawn5 = list_position[3][8]
black_black_pawn5 = Chess(root,"卒","black",pos_black_pawn5)


#******************************************
#红兵１
pos_red_pawn1 = list_position[6][0]
black_red_pawn1 = Chess(root,"兵","red",pos_red_pawn1)

#红兵2
pos_red_pawn2 = list_position[6][2]
black_red_pawn2 = Chess(root,"兵","red",pos_red_pawn2)

#红兵3
pos_red_pawn3 = list_position[6][4]
black_red_pawn3 = Chess(root,"兵","red",pos_red_pawn3)

#红兵4
pos_red_pawn4 = list_position[6][6]
black_red_pawn4 = Chess(root,"兵","red",pos_red_pawn4)

#红兵5
pos_red_pawn5 = list_position[6][8]
black_red_pawn5 = Chess(root,"兵","red",pos_red_pawn5)

#左红炮
pos_red_left_gun = list_position[7][1]
black_red_left_gun = Chess(root,"炮","red",pos_red_left_gun)

#右红炮
pos_red_right_gun = list_position[7][7]
black_red_right_gun = Chess(root,"炮","red",pos_red_right_gun)

#左红车
pos_red_left_rook = list_position[9][0]
red_left_rook = Chess(root,"車","red",pos_red_left_rook)

#左红马
pos_red_left_knight = list_position[9][1]
red_left_knight = Chess(root,"馬","red",pos_red_left_knight)

#左红相
pos_red_left_minister = list_position[9][2]
red_left_minister = Chess(root,"相","red",pos_red_left_minister)

#左红仕
pos_red_left_guard = list_position[9][3]
red_left_guard = Chess(root,"仕","red",pos_red_left_guard)

#红帅
pos_red_king = list_position[9][4]
red_king = Chess(root,"帅","red",pos_red_king)

#右红仕
pos_red_right_guard = list_position[9][5]
red_right_guard = Chess(root,"仕","red",pos_red_right_guard)

#右红相
pos_red_right_minister = list_position[9][6]
red_right_minister = Chess(root,"相","red",pos_red_right_minister)

#右红马
pos_red_right_knight = list_position[9][7]
red_right_knight = Chess(root,"馬","red",pos_red_right_knight)

#右红车
pos_red_right_rook = list_position[9][8]
red_right_rook = Chess(root,"車","red",pos_red_right_rook)


root.update()

root.mainloop()

