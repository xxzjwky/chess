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
    def __init__(self, root,name,color,pos_in_list,fun_position):
        """

        :param root: 全局画布
        :param name: 棋子名称
        :param color: 棋子颜色
        :param position: 棋子坐标
        :param pos_in_list: 该棋子在列表中的位置
        :param fun_position: 该棋子在列表中的位置
        """
        self.name = name
        self.color = color
        self.position = list_position[pos_in_list[0]][pos_in_list[1]]
        self.pos_in_list = pos_in_list
        self.fun_position = fun_position

        ft = tkFont.Font(family='微软雅黑', size=20, weight=tkFont.BOLD)
        self.btn = Button(root,text=name, bg="#d1b07e",fg=color, font=ft,height = "1",width = "1", command=self.click)
        self.btn.pack()
        self.btn.place(x=self.position[0], y=self.position[1])

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

    def get_passable_positions(self):
        """
        获得该棋子可以移动的所有位置
        :return:
        """
        return self.fun_position(self.name,self.color,self.pos_in_list)

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
            if abs(chess_one[0] - click_location[0])<30 and abs(chess_one[1] - click_location[1])<30:

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
#位置都是从画布的左往右pos_in_list

img_gif = PhotoImage(file = 'image/chess.gif')
label_img = Label(root, image = img_gif)
label_img.bind("<Button-1>", showlocation)
label_img.pack()

#左黑车
black_left_rook = Chess(root,"車","black",(0,0),None)

#左黑马
black_left_knight = Chess(root,"馬","black",(0,1),None)

#左黑象
black_left_minister = Chess(root,"象","black",(0,2),None)

#左黑士
black_left_guard = Chess(root,"士","black",(0,3),None)

#黑将
black_king = Chess(root,"将","black",(0,4),None)

#右黑士
black_right_guard = Chess(root,"士","black",(0,5),None)

#右黑象
black_right_minister = Chess(root,"象","black",(0,6),None)

#右黑马
black_right_knight = Chess(root,"馬","black",(0,7),None)

#右黑车
black_right_rook = Chess(root,"車","black",(0,8),None)

#左黑炮
black_left_gun = Chess(root,"炮","black",(2,1),None)

#右黑炮
black_right_gun = Chess(root,"炮","black",(2,7),None)

#黑卒１
black_black_pawn1 = Chess(root,"卒","black",(3,0),None)

#黑卒2
black_black_pawn2 = Chess(root,"卒","black",(3,2),None)

#黑卒3
black_black_pawn3 = Chess(root,"卒","black",(3,4),None)

#黑卒4
black_black_pawn4 = Chess(root,"卒","black",(3,6),None)

#黑卒5
black_black_pawn5 = Chess(root,"卒","black",(3,8),None)


#******************************************
#红兵１
black_red_pawn1 = Chess(root,"兵","red",(6,0),None)

#红兵2
black_red_pawn2 = Chess(root,"兵","red",(6,2),None)

#红兵3
black_red_pawn3 = Chess(root,"兵","red",(6,4),None)

#红兵4
black_red_pawn4 = Chess(root,"兵","red",(6,6),None)

#红兵5
black_red_pawn5 = Chess(root,"兵","red",(6,8),None)

#左红炮
black_red_left_gun = Chess(root,"炮","red",(7,1),None)

#右红炮
black_red_right_gun = Chess(root,"炮","red",(7,7),None)

#左红车
red_left_rook = Chess(root,"車","red",(9,0),None)

#左红马
red_left_knight = Chess(root,"馬","red",(9,1),None)

#左红相
red_left_minister = Chess(root,"相","red",(9,2),None)

#左红仕
red_left_guard = Chess(root,"仕","red",(9,3),None)

#红帅
red_king = Chess(root,"帅","red",(9,4),None)

#右红仕
red_right_guard = Chess(root,"仕","red",(9,5),None)

#右红相
red_right_minister = Chess(root,"相","red",(9,6),None)

#右红马
red_right_knight = Chess(root,"馬","red",(9,7),None)

#右红车
red_right_rook = Chess(root,"車","red",(9,8),None)


root.update()

root.mainloop()

