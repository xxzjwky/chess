from tkinter import *

import tkinter.font as tkFont


#棋盘列表
list_chess = [
    [(57,20),(136,20),(215,20),(294,20),(374,20),(454,20),(532,20),(611,20),(690,20)],
    [(57,100),(136,100),(215,100),(294,100),(374,100),(454,100),(532,100),(611,100),(690,100)],
    [(57,180),(136,180),(215,180),(294,180),(374,180),(454,180),(532,180),(611,180),(690,180)],
    [(57,260),(136,260),(215,260),(294,260),(374,260),(454,260),(532,260),(611,260),(690,260)],
    [(57,340),(136,340),(215,340),(294,340),(374,340),(454,340),(532,340),(611,340),(690,340)],
    [(57,420),(136,420),(215,420),(294,420),(374,420),(454,420),(532,420),(611,420),(690,420)],
    [(57,500),(136,500),(215,500),(294,500),(374,500),(454,500),(532,500),(611,500),(690,500)],
    [(57,580),(136,580),(215,580),(294,580),(374,580),(454,580),(532,580),(611,580),(690,580)],
    [(57,660),(136,660),(215,660),(294,660),(374,660),(454,660),(532,660),(611,660),(690,660)],
    [(57,740),(136,740),(215,740),(294,740),(374,740),(454,740),(532,740),(611,740),(690,740)]
]

click_item = {}


class Chess:
    def __init__(self, root,name,color,position,click_item):
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


#位置都是从画布的左往右

img_gif = PhotoImage(file = 'image/chess.gif')
label_img = Label(root, image = img_gif)
label_img.bind("<Button-1>", showlocation)
label_img.pack()

#左黑车
pos_black_left_rook = list_chess[0][0]
black_left_rook = Chess(root,"車","black",pos_black_left_rook,click_item)


root.update()

root.mainloop()

