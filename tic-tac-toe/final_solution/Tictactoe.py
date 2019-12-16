# -*- coding: utf-8 -*-
import time


class Board:
    """Class allowing to play Tic-Tac-Toe. It looks quite long but illustrate the classical behavior of a game, giving methods you can find in some other games (such as chess for example)"""

    _X = "X"
    _O = "O"
    _E = "."  # empty

    def __init__(self):
        self._nextPlayer = self._X

        self._board = []
        for x in range(3):
            self._board.append([self._E] * 3)

        self._alignments = []
        for x in range(3):
            a = []
            amirror = []
            for y in range(3):
                a.append((x, y))
                amirror.append((y, x))
            self._alignments.append(a)
            self._alignments.append(amirror)
        self._alignments.append([(0, 0), (1, 1), (2, 2)])
        self._alignments.append([(2, 0), (1, 1), (0, 2)])

        self._stack = []  # Used to keep track of push/pop moves

    def _get_an_alignment(self):
        for a in self._alignments:
            if (
                (self._board[a[0][0]][a[0][1]] != self._E)
                and (self._board[a[0][0]][a[0][1]] == self._board[a[1][0]][a[1][1]])
                and (self._board[a[0][0]][a[0][1]] == self._board[a[2][0]][a[2][1]])
            ):
                return self._board[a[0][0]][a[0][1]]
        return None

    def _has_an_alignment(self):
        return self._get_an_alignment() is not None

    def _at_least_one_empty_cell(self):
        for x in range(3):
            for y in range(3):
                if self._board[x][y] == self._E:
                    return True
        return False

    def is_game_over(self):
        """Test if the game is over"""
        if self._has_an_alignment():
            return True
        if self._at_least_one_empty_cell():
            return False
        return True

    def result(self):
        """Return the winner of the game"""
        return self._get_an_alignment()

    def push(self, move):
        """Allows to push a move to be able to unplay it later."""
        [player, x, y] = move
        assert player == self._nextPlayer
        self._stack.append(move)
        self._board[x][y] = player
        if self._nextPlayer == self._X:
            self._nextPlayer = self._O
        else:
            self._nextPlayer = self._X

    def pop(self):
        """Pop a move previously played. Allows to put back the board
           in the same state as before playing."""
        move = self._stack.pop()
        [player, x, y] = move
        self._nextPlayer = player
        self._board[x][y] = self._E

    def is_end(self):
        # Vertical win
        for i in range(0, 3):
            if (
                self._board[0][i] != "."
                and self._board[0][i] == self._board[1][i]
                and self._board[1][i] == self._board[2][i]
            ):
                return self._board[0][i]

        # Horizontal win
        for i in range(0, 3):
            if self._board[i] == ["X", "X", "X"]:
                return "X"
            elif self._board[i] == ["O", "O", "O"]:
                return "O"

        # Main diagonal win
        if (
            self._board[0][0] != "."
            and self._board[0][0] == self._board[1][1]
            and self._board[0][0] == self._board[2][2]
        ):
            return self._board[0][0]

        # Second diagonal win
        if (
            self._board[0][2] != "."
            and self._board[0][2] == self._board[1][1]
            and self._board[0][2] == self._board[2][0]
        ):
            return self._board[0][2]

        # Is whole board full?
        for i in range(0, 3):
            for j in range(0, 3):
                # There's an empty field, we continue the game
                if self._board[i][j] == ".":
                    return None

        # It's a tie!
        return "."

    # Player 'O' is max, in this case AI
    def max(self):

        # Possible values for maxv are:
        # -1 - loss
        # 0  - a tie
        # 1  - win

        # We're initially setting it to -2 as worse than the worst case:
        maxv = -2

        px = None
        py = None

        result = self.is_end()

        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 0  - a tie
        # 1  - win
        if result == "X":
            return (-1, 0, 0)
        elif result == "O":
            return (1, 0, 0)
        elif result == ".":
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self._board[i][j] == ".":
                    # On the empty field player 'O' makes a move and calls Min
                    # That's one branch of the game tree.
                    self._board[i][j] = "O"
                    (m, min_i, min_j) = self.min()
                    # Fixing the maxv value if needed
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    # Setting back the field to empty
                    self._board[i][j] = "."
        return (maxv, px, py)

    # Player 'X' is min, in this case human
    def min(self):

        # Possible values for minv are:
        # -1 - win
        # 0  - a tie
        # 1  - loss

        # We're initially setting it to 2 as worse than the worst case:
        minv = 2

        qx = None
        qy = None

        result = self.is_end()

        if result == "X":
            return (-1, 0, 0)
        elif result == "O":
            return (1, 0, 0)
        elif result == ".":
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self._board[i][j] == ".":
                    self._board[i][j] = "X"
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self._board[i][j] = "."

        return (minv, qx, qy)

    # Determines if the made move is a legal move
    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self._board[px][py] != ".":
            return False
        else:
            return True

    def legal_moves(self):
        """An important function : it allows to return all the possible moves
           for the current board"""
        moves = []
        # If it's player's turn
        if self._nextPlayer == "X":

            while True:

                start = time.time()
                (m, qx, qy) = self.min()
                end = time.time()
                print("Evaluation time: {}s".format(round(end - start, 7)))
                print("Recommended move: X = {}, Y = {}".format(qx, qy))

                px = int(input("Insert the X coordinate: "))
                py = int(input("Insert the Y coordinate: "))

                (qx, qy) = (px, py)

                if self.is_valid(px, py):
                    self._board[qx][qy] = "X"
                    self._nextPlayer = "O"
                    moves.append([self._nextPlayer, px, py])
                    break
                else:
                    print("The move is not valid! Try again.")

        # If it's AI's turn
        else:
            (m, px, py) = self.max()
            self._board[px][py] = "O"
            self._nextPlayer = "X"
            moves.append([self._nextPlayer, px, py])
        return moves

    def _piece2str(self, c):
        if c == self._O:
            return "O"
        elif c == self._X:
            return "X"
        else:
            return "."

    def __str__(self):
        toreturn = ""
        for l in self._board:
            for c in l:
                toreturn += self._piece2str(c)
            toreturn += "\n"
        toreturn += (
            "Next player: " + ("X" if self._nextPlayer == self._X else "O") + "\n"
        )
        return toreturn

    __repr__ = __str__
