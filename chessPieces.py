from chess import *

class Rook(Chess):

    def collect_move_positions(self,can_move,vector):

        vector_list = []

        for item in list_chess:
            if vector == "up":
                if item.pos_in_list[1] == self.pos_in_list[1] and item.pos_in_list[0] < self.pos_in_list[0]:
                    vector_list.append(item)
            elif vector == "down":
                if item.pos_in_list[1] == self.pos_in_list[1] and item.pos_in_list[0] > self.pos_in_list[0]:
                    vector_list.append(item)
            elif vector == "left":
                if item.pos_in_list[0] == self.pos_in_list[0] and item.pos_in_list[1] < self.pos_in_list[1]:
                    vector_list.append(item)
            elif vector == "right":
                if item.pos_in_list[0] == self.pos_in_list[0] and item.pos_in_list[1] > self.pos_in_list[1]:
                    vector_list.append(item)

        #找边界子
        bond_chess = None
        for item in vector_list:
            if not bond_chess:
                bond_chess = item
            else:
                if vector == "up":
                    if item.pos_in_list[0] > bond_chess.pos_in_list[0]:
                        bond_chess = item
                elif vector == "down":
                    if item.pos_in_list[0] < bond_chess.pos_in_list[0]:
                        bond_chess = item
                elif vector == "left":
                    if item.pos_in_list[1] > bond_chess.pos_in_list[1]:
                        bond_chess = item
                elif vector == "right":
                    if item.pos_in_list[1] < bond_chess.pos_in_list[1]:
                        bond_chess = item

        #界限
        position_bound = None
        if vector == "up":
            if bond_chess:
                position_bound = bond_chess.pos_in_list[0]
            else:
                position_bound = 0
        elif vector == "down":
            if bond_chess:
                position_bound = bond_chess.pos_in_list[0]
            else:
                position_bound = 9

        elif vector == "left":
            if bond_chess:
                position_bound = bond_chess.pos_in_list[1]
            else:
                position_bound = 0
        elif vector == "right":
            if bond_chess:
                position_bound = bond_chess.pos_in_list[1]
            else:
                position_bound = 8


        # 添加中间元素包含边界子的列表
        if vector == "up":
            for c in range(self.pos_in_list[0] - 1, position_bound - 1, -1):
                can_move.append(list_position[c][self.pos_in_list[1]])
        elif vector == "down":
            for c in range(self.pos_in_list[0]+1, position_bound +1):
                can_move.append(list_position[c][self.pos_in_list[1]])
        elif vector == "left":
            for c in range(self.pos_in_list[1] - 1, position_bound - 1, -1):
                can_move.append(list_position[self.pos_in_list[0]][c])
        elif vector == "right":
            for c in range(self.pos_in_list[1]+1, position_bound +1):
                can_move.append(list_position[self.pos_in_list[0]][c])


        # 如果边界与本子颜色相同从列表中去掉
        if bond_chess and bond_chess.color == self.color:
            can_move.remove(list_position[bond_chess.pos_in_list[0]][bond_chess.pos_in_list[1]])



    """
     车
    """
    def get_passable_positions(self):
        """
        获得该棋子可以移动的所有位置
        :return:
        """
        can_move = []

        self.collect_move_positions(can_move,"up")
        self.collect_move_positions(can_move, "down")
        self.collect_move_positions(can_move, "left")
        self.collect_move_positions(can_move, "right")

        print(can_move)
        return can_move

class Knight(Chess):
    """
     马
    """
    def get_passable_positions(self):
        """
        获得该棋子可以移动的所有位置
        :return:
        """
        can_move = []

        x = self.pos_in_list[0]
        y = self.pos_in_list[1]
        # 一格代表的像素
        # 直接安格子存放，打印时计算像素
        i = 1
        # 向上的情况
        if x - 2 >= 0 and self.judge_block("up",x,y):
            if y - 1 >= 0:
                can_move.append(list_position[x - 2 * i][y - i])
            if y + 1 <= 8:
                can_move.append(list_position[x - 2 * i][y + i])
        # 向右的情况
        if y + 2 <= 8 and self.judge_block("right",x,y):
            if x - 1 >= 0:
                can_move.append(list_position[(x - i)][y + 2 * i])
            if x + 1 <= 9:
                can_move.append(list_position[x + i][y + 2 * i])
        # 向下的情况
        if x + 2 <= 9 and self.judge_block("down",x,y):
            if y - 1 >= 0:
                can_move.append(list_position[x + 2 * i][y - i])
            if y + 1 <= 8:
                can_move.append(list_position[x + 2 * i][y + i])
        # 向左的情况
        if y - 2 >= 0 and self.judge_block("left",x,y):
            if x - 1 >= 0:
                can_move.append(list_position[x - i][y - 2 * i])
            if x + 1 <= 9:
                can_move.append(list_position[x + i][y - 2 * i])
        return can_move

    def judge_block(self,vector,x,y):
        #向上的判断
        if vector == "up":
            x -= 1
        #向右的判断
        if vector == "right":
            y += 1
        if vector == "down":
            x += 1
        if vector == "left":
            y -= 1
        for s in list_chess:
            if x == s.pos_in_list[0] and y == s.pos_in_list[1]:
                return False
        return True


class Minister(Chess):
    """
     相
    """
    def get_passable_positions(self):
        """
        获得该棋子可以移动的所有位置
        :return:
        """
        pass

class Guard(Chess):
    """
     士
    """
    def get_passable_positions(self):
        """
        获得该棋子可以移动的所有位置
        :return:
        """
        pass

class King(Chess):
    """
     将
    """
    def get_passable_positions(self):
        """
        获得该棋子可以移动的所有位置
        :return:
        """
        pass

class Gun(Chess):
    """
     炮
    """
    def get_passable_positions(self):
        """
        获得该棋子可以移动的所有位置
        :return:
        """
        pass


class Pawn(Chess):
    """
     兵
    """
    def get_passable_positions(self):
        """
        获得该棋子可以移动的所有位置
        :return:
        """
        pass