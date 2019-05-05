from tkinter import *

import tkinter.font as tkFont

import time


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
    def __init__(self, root,name,color,pos_in_list):
        """

        :param root: 全局画布
        :param name: 棋子名称
        :param color: 棋子颜色
        :param position: 棋子坐标
        :param pos_in_list: 该棋子在列表中的位置
        :param fun_position: 该棋子在列表中的位置
        """
        self.root = root
        self.name = name
        self.color = color
        self.position = list_position[pos_in_list[0]][pos_in_list[1]]
        self.pos_in_list = pos_in_list

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

            #颜色不同
            else:

                if judge_can_move(click_item["data"],self.position):
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
        pass


def find_move_location(click_location):
    """
    找寻具体移动位置
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
                        # item.delete()
                        # break

                return chess_one

def judge_can_move(chess,position):
    """
    判断该位置是否可以移动
    :param chess:  焦点棋子
    :param position:　目标位置
    :return: True 可以移动　　False 不可移动
    """

    # 符合移动条件
    passable_positions = chess.get_passable_positions()
    if passable_positions and position in passable_positions:

        return True
    else:
        # 显示红色警告后恢复原色
        bg = chess.btn['bg']
        chess.btn['bg'] = "#CC66FF"
        chess.root.update()
        time.sleep(1)
        chess.btn['bg'] = bg
        chess.root.update()
        return False

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


def click_chessboard(event):

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

        #待移动位置
        if move_location and judge_can_move(chess,move_location):

            #更新列表中棋子的新位置
            refresh_list_chess(chess,move_location)

            chess.btn.place(x=move_location[0], y=move_location[1])
            chess.btn['bg'] = "#d1b07e"
            del click_item["data"]


