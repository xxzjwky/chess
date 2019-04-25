import tkinter

win = tkinter.Tk()
win.title("鼠标单击事件")
win.geometry("800x600+600+100")

#<Button-1>单击鼠标左键
#<Button-2>鼠标中键
#<Button-3>鼠标右键
#<Double-Button-1>单击鼠标左键双击
#<Double-Button-2>鼠标中键双击
#<Double-Button-3>鼠标右键双击
#<Triple-Button-1>鼠标左键三击
def func(event):
    print(event.x,event.y)#打印x,y坐标
button1=tkinter.Button(win,text="left mouse button")
button2=tkinter.Label(win,text="left mouse button")
#bind  给控件绑定事件
button1.bind("<Button-1>",func)
button2.bind("<Button-1>",func)
button1.pack()
button2.pack()

win.mainloop()