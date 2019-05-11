from chessPieces import *


root = Tk(className = "中国象棋")
root.geometry("800x800")


img_gif = PhotoImage(file = 'image/chess.gif')
label_img = Label(root, image = img_gif)
label_img.bind("<Button-1>", click_chessboard)
label_img.pack()

#***********************************************************
#左黑车
black_left_rook = Rook(root,"車","black",(0,0),100)
#右黑车
black_right_rook = Rook(root,"車","black",(0,8),100)
#左红车
red_left_rook = Rook(root,"車","red",(9,0),100)
#右红车
red_right_rook = Rook(root,"車","red",(9,8),100)

#***********************************************************
#左黑马
black_left_knight = Knight(root,"馬","black",(0,1),80)
#右黑马
black_right_knight = Knight(root,"馬","black",(0,7),80)
#左红马
red_left_knight = Knight(root,"馬","red",(9,1),80)
#右红马
red_right_knight = Knight(root,"馬","red",(9,7),80)

#***********************************************************
#左黑象
black_left_minister = Minister(root,"象","black",(0,2),30)
#右黑象
black_right_minister = Minister(root,"象","black",(0,6),30)
#左红相
red_left_minister = Minister(root,"相","red",(9,2),30)
#右红相
red_right_minister = Minister(root,"相","red",(9,6),30)

#***********************************************************
#左黑士
black_left_guard = Guard(root,"士","black",(0,3),40)
#右黑士
black_right_guard = Guard(root,"士","black",(0,5),40)
#左红仕
red_left_guard = Guard(root,"仕","red",(9,3),40)
#右红仕
red_right_guard = Guard (root,"仕","red",(9,5),40)
#***********************************************************
#黑将
black_king = King(root,"将","black",(0,4),200)
#红帅
red_king = King(root,"帅","red",(9,4),200)
#***********************************************************
#左黑炮
black_left_gun = Gun(root,"炮","black",(2,1),90)
#右黑炮
black_right_gun = Gun(root,"炮","black",(2,7),90)
#左红炮
red_left_gun = Gun(root,"炮","red",(7,1),90)
#右红炮
red_right_gun = Gun(root,"炮","red",(7,7),90)
#***********************************************************
#黑卒１
black_pawn1 = Pawn(root,"卒","black",(3,0),1)

#黑卒2
black_pawn2 = Pawn(root,"卒","black",(3,2),1)

#黑卒3
black_pawn3 = Pawn(root,"卒","black",(3,4),1)

#黑卒4
black_pawn4 = Pawn(root,"卒","black",(3,6),1)

#黑卒5
black_pawn5 = Pawn(root,"卒","black",(3,8),1)

#红兵１
red_pawn1 = Pawn(root,"兵","red",(6,0),1)

#红兵2
red_pawn2 = Pawn(root,"兵","red",(6,2),1)

#红兵3
red_pawn3 = Pawn(root,"兵","red",(6,4),1)

#红兵4
red_pawn4 = Pawn(root,"兵","red",(6,6),1)

#红兵5
red_pawn5 = Pawn(root,"兵","red",(6,8),1)

#******************************************

root.update()

root.mainloop()

