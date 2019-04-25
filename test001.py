from tkinter import *


win = Tk(className = "中国象棋")
win.geometry("800x800")
win.update()


def showlocation(event):
    print(event.x,event.y)



img_gif = PhotoImage(file = '/home/tarena/chess1.gif')
label_img = Label(win, image = img_gif)
label_img.bind("<Button-1>", showlocation)
label_img.pack()
win.update()

# img_gif1 = PhotoImage(file='/home/tarena/红车1.gif')
# label_img1 = Label(win, image=img_gif1)
# # label_img.bind("<Button-1>", showlocation)
# label_img1.pack()
# label_img1.place(x=57, y=25)
# win.update()
#
# img_gif2 = PhotoImage(file='/home/tarena/红车1.gif')
# label_img2 = Label(win, image=img_gif1)
# # label_img.bind("<Button-1>", showlocation)
# label_img2.pack()
# label_img2.place(x=57, y=105)
# win.update()

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

for i in range(10):  # 行数
    for j in range(9):
        img_gif1 = PhotoImage(file='/home/tarena/红车1.gif')
        label_img1 = Label(win, image=img_gif1)
        # label_img.bind("<Button-1>", showlocation)
        label_img1.pack()
        label_img1.place(x=list_chess[i][j][0], y=list_chess[i][j][1])
        win.update()


# 进入消息循环
win.mainloop()

