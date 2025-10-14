class Board:
    def __init__(self):
        "0: X 1: O"
        self.board = [None] * 9
        self.current_player = 0

    def __repr__(self) -> str:
        symbols = {None: " ", 0: "X", 1: "O"}
        rows = []
        for i in range(0, 9, 3):
            row = [symbols[self.board[j]] for j in range(i, i + 3)]
            rows.append(" | ".join(row))
        return "\n---------\n".join(rows)

    def reset(self):
        self.board = [None] * 9
        self.current_player = 0
        return self.state

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
        player_str = "X" if self.current_player == 0 else "O"

        # calculate reward
        reward = 0
        if winner == self.current_player:
            reward = 1
        elif winner is not None:
            reward = -1
        else:
            reward = 0

        self.current_player = 0 if self.current_player == 1 else 1

        info = None
        if winner is None:
            if done:
                info = "It's a DRAW!"
            else:
                # map 0 to X and 1 to O for info
                info = f"Next turn: {player_str}"
        else:
            # map 0 to X and 1 to O for info
            info = f"{player_str} WON!"

        return (
            self.state,
            reward,
            done,
            info,
        )

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

    def step(self, action):
        return self.make_move(action)

    @property
    def action_space(self):
        return 9

    @property
    def observation_space(self):
        return 9

    @property
    def state(self):
        return (tuple(self.board), self.current_player)
