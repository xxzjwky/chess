from chess import *


def do_filter(chess_color, passable_positions):
    """
    过滤出真正返回位置
    :param chess_color: 当前棋子颜色
    :param passable_positions:　前判断可走位置
    :return:  过滤出真正返回位置
    """

    for i in range(len(list_chess)):
        chess_one = list_chess[i]
        if chess_one.position in passable_positions and chess_color == chess_one.color:
            passable_positions.remove(chess_one.position)
    return passable_positions


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
        if x - 2 >= 0 and self.judge_block("up", x, y):
            if y - 1 >= 0:
                can_move.append(list_position[x - 2 * i][y - i])
            if y + 1 <= 8:
                can_move.append(list_position[x - 2 * i][y + i])
        # 向右的情况
        if y + 2 <= 8 and self.judge_block("right", x, y):
            if x - 1 >= 0:
                can_move.append(list_position[(x - i)][y + 2 * i])
            if x + 1 <= 9:
                can_move.append(list_position[x + i][y + 2 * i])
        # 向下的情况
        if x + 2 <= 9 and self.judge_block("down", x, y):
            if y - 1 >= 0:
                can_move.append(list_position[x + 2 * i][y - i])
            if y + 1 <= 8:
                can_move.append(list_position[x + 2 * i][y + i])
        # 向左的情况
        if y - 2 >= 0 and self.judge_block("left", x, y):
            if x - 1 >= 0:
                can_move.append(list_position[x - i][y - 2 * i])
            if x + 1 <= 9:
                can_move.append(list_position[x + i][y - 2 * i])
        return do_filter(self.color, can_move)

    def judge_block(self, vector, x, y):
        # 向上的判断
        if vector == "up":
            x -= 1
        # 向右的判断
        if vector == "right":
            y += 1
        # 向下的判断
        if vector == "down":
            x += 1
        # 向左的判断
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
        can_move = []
        x = self.pos_in_list[0]
        y = self.pos_in_list[1]
        if self.color == "red":
            # 象飞上方的判断
            if x - 2 >= 5:
                # 象飞左上
                if y - 2 >= 0 and self.judge_block("leftup", x, y):
                    can_move.append(list_position[x - 2][y - 2])
                # 象飞右上
                if y + 2 <= 8 and self.judge_block("rightup", x, y):
                    can_move.append(list_position[x - 2][y + 2])
            # 象飞下方的判断
            if x + 2 <= 9:
                # 象飞左下
                if y - 2 >= 0 and self.judge_block("leftdwon", x, y):
                    can_move.append(list_position[x + 2][y - 2])
                # 象飞右下
                if y + 2 <= 8 and self.judge_block("rightdown", x, y):
                    can_move.append(list_position[x + 2][y + 2])

        else:
            # 象飞上方的判断
            if x - 2 >= 0:
                # 象飞左上
                if y - 2 >= 0 and self.judge_block("leftup", x, y):
                    can_move.append(list_position[x - 2][y - 2])
                # 象飞右上
                if y + 2 <= 8 and self.judge_block("rightup", x, y):
                    can_move.append(list_position[x - 2][y + 2])
            # 象飞下方的判断
            if x + 2 <= 4:
                # 象飞左下
                if y - 2 >= 0 and self.judge_block("leftdwon", x, y):
                    can_move.append(list_position[x + 2][y - 2])
                # 象飞右下
                if y + 2 <= 8 and self.judge_block("rightdown", x, y):
                    can_move.append(list_position[x + 2][y + 2])

        return do_filter(self.color, can_move)

    def judge_block(self, vector, x, y):
        # 向左上的判断
        if vector == "leftup":
            x -= 1
            y += 1
        # 向右上的判断
        if vector == "rightup":
            x -= 1
            y += 1
        # 向右下的判断
        if vector == "rightdown":
            x += 1
            y += 1
        # 向左下的判断
        if vector == "leftdwon":
            x += 1
            y -= 1
        for s in list_chess:
            if x == s.pos_in_list[0] and y == s.pos_in_list[1]:
                return False
        return True


class Guard(Chess):
    """
     士
    """

    def get_passable_positions(self):
        """
        获得该棋子可以移动的所有位置
        :return:
        """
        can_move = []
        x = self.pos_in_list[0]
        y = self.pos_in_list[1]
        if self.color == "red":
            if x - 1 >= 7:
                if y - 1 >= 3:
                    can_move.append(list_position[x - 1][y - 1])
                if y + 1 <= 5:
                    can_move.append(list_position[x - 1][y + 1])
            if x + 1 <= 9:
                if y - 1 >= 3:
                    can_move.append(list_position[x + 1][y - 1])
                if y + 1 <= 5:
                    can_move.append(list_position[x + 1][y + 1])
        else:
            if x - 1 >= 0:
                if y - 1 >= 3:
                    can_move.append(list_position[x - 1][y - 1])
                if y + 1 <= 5:
                    can_move.append(list_position[x - 1][y + 1])
            if x + 1 <= 2:
                if y - 1 >= 3:
                    can_move.append(list_position[x + 1][y - 1])
                if y + 1 <= 5:
                    can_move.append(list_position[x + 1][y + 1])
        return do_filter(self.color, can_move)


class King(Chess):
    """
     将
    """

    def get_passable_positions(self):
        """
        获得该棋子可以移动的所有位置
        :return:
        """
        can_move = []
        x = self.pos_in_list[0]
        y = self.pos_in_list[1]
        if self.color == "red":
            # 向上的判断
            if x - 1 >= 7:
                can_move.append(list_position[x - 1][y])
            # 向右的判断
            if y + 1 <= 5:
                can_move.append(list_position[x][y + 1])
            # 向下的判断
            if x + 1 <= 9:
                can_move.append(list_position[x + 1][y])
            # 向左的判断
            if y - 1 >= 3:
                can_move.append(list_position[x][y - 1])
        else:
            # 向上的判断
            if x - 1 >= 0:
                can_move.append(list_position[x - 1][y])
            # 向右的判断
            if y + 1 <= 5:
                can_move.append(list_position[x][y + 1])
            # 向下的判断
            if x + 1 <= 2:
                can_move.append(list_position[x + 1][y])
            # 向左的判断
            if y - 1 >= 3:
                can_move.append(list_position[x][y - 1])
        return do_filter(self.color, can_move)


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
        can_move = []
        x = self.pos_in_list[0]
        y = self.pos_in_list[1]
        if self.color == "red":
            if x >= 5:
                can_move.append(list_position[x - 1][y])
            if x <= 4:
                can_move.append(list_position[x - 1][y])
                if y + 1 <= 8:
                    can_move.append(list_position[x][y + 1])
                if y - 1 >= 0:
                    can_move.append(list_position[x][y - 1])
        else:
            if x <= 4:
                can_move.append(list_position[x + 1][y])
            if x >= 5:
                can_move.append(list_position[x + 1][y])
                if y + 1 <= 8:
                    can_move.append(list_position[x][y + 1])
                if y - 1 >= 0:
                    can_move.append(list_position[x][y - 1])
        return do_filter(self.color, can_move)

