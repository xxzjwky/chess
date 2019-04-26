from tkinter import *

import tkinter.font as tkFont


#棋盘列表
list_chess = [
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

click_item = {}


class Chess:
    def __init__(self, root,name,color,position):
        """

        :param root: 全局画布
        :param name: 棋子名称
        :param color: 棋子颜色
        :param position: 棋子位置
        """

        self.click_item = click_item
        self.color = color


        ft = tkFont.Font(family='微软雅黑', size=20, weight=tkFont.BOLD)
        self.btn = Button(root,text=name, bg="#d1b07e",fg=color, font=ft,height = "1",width = "1", command=self.click)
        self.btn.pack()
        self.btn.place(x=position[0], y=position[1])
    def click(self):
        #点击变黄色背景　并且标记
        self.btn['bg']="yellow"
        self.click_item["data"]= self
        # print("您刚才通过点击打招呼触发了我:大家好，我是badao！")


root = Tk(className = "中国象棋")
root.geometry("800x800")

def showlocation(event):
    print(event.x,event.y)
    print(click_item)
    if click_item:
        chess = click_item["data"]
        chess.btn.place(x=event.x, y=event.y)
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
pos_black_left_rook = list_chess[0][0]
black_left_rook = Chess(root,"車","black",pos_black_left_rook)

#左黑马
pos_black_left_knight = list_chess[0][1]
black_left_knight = Chess(root,"馬","black",pos_black_left_knight)

#左黑象
pos_black_left_minister = list_chess[0][2]
black_left_minister = Chess(root,"象","black",pos_black_left_minister)

#左黑士
pos_black_left_guard = list_chess[0][3]
black_left_guard = Chess(root,"士","black",pos_black_left_guard)

#黑将
pos_black_king = list_chess[0][4]
black_king = Chess(root,"将","black",pos_black_king)

#右黑士
pos_black_right_guard = list_chess[0][5]
black_right_guard = Chess(root,"士","black",pos_black_right_guard)

#右黑象
pos_black_right_minister = list_chess[0][6]
black_right_minister = Chess(root,"象","black",pos_black_right_minister)

#右黑马
pos_black_right_knight = list_chess[0][7]
black_right_knight = Chess(root,"馬","black",pos_black_right_knight)

#右黑车
pos_black_right_rook = list_chess[0][8]
black_right_rook = Chess(root,"車","black",pos_black_right_rook)

#左黑炮
pos_black_left_gun = list_chess[2][1]
black_left_gun = Chess(root,"炮","black",pos_black_left_gun)

#右黑炮
pos_black_right_gun = list_chess[2][7]
black_right_gun = Chess(root,"炮","black",pos_black_right_gun)

#黑卒１
pos_black_pawn1 = list_chess[3][0]
black_black_pawn1 = Chess(root,"卒","black",pos_black_pawn1)

#黑卒2
pos_black_pawn2 = list_chess[3][2]
black_black_pawn2 = Chess(root,"卒","black",pos_black_pawn2)

#黑卒3
pos_black_pawn3 = list_chess[3][4]
black_black_pawn3 = Chess(root,"卒","black",pos_black_pawn3)

#黑卒4
pos_black_pawn4 = list_chess[3][6]
black_black_pawn4 = Chess(root,"卒","black",pos_black_pawn4)

#黑卒5
pos_black_pawn5 = list_chess[3][8]
black_black_pawn5 = Chess(root,"卒","black",pos_black_pawn5)


#******************************************
#红兵１
pos_red_pawn1 = list_chess[6][0]
black_red_pawn1 = Chess(root,"兵","red",pos_red_pawn1)

#红兵2
pos_red_pawn2 = list_chess[6][2]
black_red_pawn2 = Chess(root,"兵","red",pos_red_pawn2)

#红兵3
pos_red_pawn3 = list_chess[6][4]
black_red_pawn3 = Chess(root,"兵","red",pos_red_pawn3)

#红兵4
pos_red_pawn4 = list_chess[6][6]
black_red_pawn4 = Chess(root,"兵","red",pos_red_pawn4)

#红兵5
pos_red_pawn5 = list_chess[6][8]
black_red_pawn5 = Chess(root,"兵","red",pos_red_pawn5)

#左红炮
pos_red_left_gun = list_chess[7][1]
black_red_left_gun = Chess(root,"炮","red",pos_red_left_gun)

#右红炮
pos_red_right_gun = list_chess[7][7]
black_red_right_gun = Chess(root,"炮","red",pos_red_right_gun)

#左红车
pos_red_left_rook = list_chess[9][0]
red_left_rook = Chess(root,"車","red",pos_red_left_rook)

#左红马
pos_red_left_knight = list_chess[9][1]
red_left_knight = Chess(root,"馬","red",pos_red_left_knight)

#左红相
pos_red_left_minister = list_chess[9][2]
red_left_minister = Chess(root,"相","red",pos_red_left_minister)

#左红仕
pos_red_left_guard = list_chess[9][3]
red_left_guard = Chess(root,"仕","red",pos_red_left_guard)

#红帅
pos_red_king = list_chess[9][4]
red_king = Chess(root,"帅","red",pos_red_king)

#右红仕
pos_red_right_guard = list_chess[9][5]
red_right_guard = Chess(root,"仕","red",pos_red_right_guard)

#右红相
pos_red_right_minister = list_chess[9][6]
red_right_minister = Chess(root,"相","red",pos_red_right_minister)

#右红马
pos_red_right_knight = list_chess[9][7]
red_right_knight = Chess(root,"馬","red",pos_red_right_knight)

#右红车
pos_red_right_rook = list_chess[9][8]
red_right_rook = Chess(root,"車","red",pos_red_right_rook)


root.update()

root.mainloop()

