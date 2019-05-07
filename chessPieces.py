from chess import *

class Rook(Chess):
    """
     车
    """
    def get_passable_positions(self):
        """
        获得该棋子可以移动的所有位置
        :return:
        """
        pass

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

        i = 1
        # 一格代表的像素
        # 直接安格子存放，打印时计算像素
        # 向上的情况
        if x - 2 >= 0:
            if y - 1 >= 0:
                can_move.append(list_position[x - 2 * i][y - i])
            if y + 1 <= 7:
                can_move.append(list_position[x - 2 * i][y + i])
        # 向右的情况
        if y + 2 <= 7:
            if x - 1 >= 0:
                can_move.append(list_position[(x - i)][y + 2 * i])
            if x + 1 <= 6:
                can_move.append(list_position[x + i][y + 2 * i])
        # 向下的情况
        if x + 2 <= 6:
            if y - 1 >= 0:
                can_move.append(list_position[x + 2 * i][y - i])
            if y + 1 <= 7:
                can_move.append(list_position[x + 2 * i][y + i])
        # 向左的情况
        if y - 2 >= 0:
            if x - 1 >= 0:
                can_move.append(list_position[x - i][y - 2 * i])
            if x + 1 <= 6:
                can_move.append(list_position[x + i][y - 2 * i])
        return can_move

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