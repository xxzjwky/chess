from tkinter import *
from chess import Chess,click_chessboard


root = Tk(className = "中国象棋")
root.geometry("800x800")


img_gif = PhotoImage(file = 'image/chess.gif')
label_img = Label(root, image = img_gif)
label_img.bind("<Button-1>", click_chessboard)
label_img.pack()

#左黑车
black_left_rook = Chess(root,"車","black",(0,0))

#左黑马
black_left_knight = Chess(root,"馬","black",(0,1))

#左黑象
black_left_minister = Chess(root,"象","black",(0,2))

#左黑士
black_left_guard = Chess(root,"士","black",(0,3))

#黑将
black_king = Chess(root,"将","black",(0,4))

#右黑士
black_right_guard = Chess(root,"士","black",(0,5))

#右黑象
black_right_minister = Chess(root,"象","black",(0,6))

#右黑马
black_right_knight = Chess(root,"馬","black",(0,7))

#右黑车
black_right_rook = Chess(root,"車","black",(0,8))

#左黑炮
black_left_gun = Chess(root,"炮","black",(2,1))

#右黑炮
black_right_gun = Chess(root,"炮","black",(2,7))

#黑卒１
black_black_pawn1 = Chess(root,"卒","black",(3,0))

#黑卒2
black_black_pawn2 = Chess(root,"卒","black",(3,2))

#黑卒3
black_black_pawn3 = Chess(root,"卒","black",(3,4))

#黑卒4
black_black_pawn4 = Chess(root,"卒","black",(3,6))

#黑卒5
black_black_pawn5 = Chess(root,"卒","black",(3,8))


#******************************************
#红兵１
black_red_pawn1 = Chess(root,"兵","red",(6,0))

#红兵2
black_red_pawn2 = Chess(root,"兵","red",(6,2))

#红兵3
black_red_pawn3 = Chess(root,"兵","red",(6,4))

#红兵4
black_red_pawn4 = Chess(root,"兵","red",(6,6))

#红兵5
black_red_pawn5 = Chess(root,"兵","red",(6,8))

#左红炮
black_red_left_gun = Chess(root,"炮","red",(7,1))

#右红炮
black_red_right_gun = Chess(root,"炮","red",(7,7))

#左红车
red_left_rook = Chess(root,"車","red",(9,0))

#左红马
red_left_knight = Chess(root,"馬","red",(9,1))

#左红相
red_left_minister = Chess(root,"相","red",(9,2))

#左红仕
red_left_guard = Chess(root,"仕","red",(9,3))

#红帅
red_king = Chess(root,"帅","red",(9,4))

#右红仕
red_right_guard = Chess(root,"仕","red",(9,5))

#右红相
red_right_minister = Chess(root,"相","red",(9,6))

#右红马
red_right_knight = Chess(root,"馬","red",(9,7))

#右红车
red_right_rook = Chess(root,"車","red",(9,8))


root.update()

root.mainloop()

