class Board:
    def __init__(self):
        "0: X 1: O"
        self.board = [None] * 9
        self.current_player = 0

    def __repr__(self) -> str:
        board_str = ""
        for i in range(0, 9, 3):
            board_str += str(self.board[i : i + 3])
            board_str += "\n"

        return board_str

    def reset(self):
        self.board = [None] * 9
        self.current_player = 0
        return self.board

    def is_valid_move(self, pos):
        if pos < 0 or pos > 8 or self.board[pos] is not None:
            return False
        else:
            return True

    def get_valid_moves(self):
        return [i for i, _ in enumerate(self.board) if _ is None]

    def make_move(self, pos):
        if not self.is_valid_move(pos):
            raise ValueError(f"Invalid move: {pos}")

        self.board[pos] = self.current_player

        # check game state
        winner = self.check_winner()
        done = winner is not None or self.is_draw()

        # calculate reward
        reward = 0
        if winner == self.current_player:
            reward = 1
        elif winner is not None:
            reward = -1
        else:
            reward = 0

        self.current_player = 0 if self.current_player == 1 else 1

        return self.board, reward, done, {"winner": winner}

    def check_winner(self):
        # check rows
        for i in range(0, 9, 3):
            if (
                self.board[i] == self.board[i + 1] == self.board[i + 2]
                and self.board[i] is not None
            ):
                return self.board[i]

        # check cols
        for i in range(3):
            if (
                self.board[i] == self.board[i + 3] == self.board[i + 6]
                and self.board[i] is not None
            ):
                return self.board[i]

        # check 2 diagonals
        if (
            self.board[0] == self.board[4] == self.board[8]
            and self.board[0] is not None
        ):
            return self.board[0]
        if (
            self.board[2] == self.board[4] == self.board[6]
            and self.board[2] is not None
        ):
            return self.board[2]

        return None

    def is_draw(self):
        return all(i is not None for i in self.board)


# test
b = Board()
print(b)

s, r, d, i = b.make_move(0)
print(b)
print(f"Reward: {r}, Done: {d}, Winner: {i}")


s, r, d, i = b.make_move(1)
print(b)
print(f"Reward: {r}, Done: {d}, Winner: {i}")


s, r, d, i = b.make_move(2)
print(b)
print(f"Reward: {r}, Done: {d}, Winner: {i}")

s, r, d, i = b.make_move(3)
print(b)
print(f"Reward: {r}, Done: {d}, Winner: {i}")

s, r, d, i = b.make_move(4)
print(b)
print(f"Reward: {r}, Done: {d}, Winner: {i}")

s, r, d, i = b.make_move(6)
print(b)
print(f"Reward: {r}, Done: {d}, Winner: {i}")

s, r, d, i = b.make_move(5)
print(b)
print(f"Reward: {r}, Done: {d}, Winner: {i}")

s, r, d, i = b.make_move(8)
print(b)
print(f"Reward: {r}, Done: {d}, Winner: {i}")

s, r, d, i = b.make_move(7)
print(b)
print(f"Reward: {r}, Done: {d}, Winner: {i}")


print("winner: ", b.check_winner())
