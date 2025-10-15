from random import choice


class FrozenLake:
    def __init__(self, size=4, slippery=True):
        self.grid = [
            ["S", "F", "F", "F"],
            ["F", "H", "F", "H"],
            ["F", "F", "F", "H"],
            ["H", "F", "F", "G"],
        ]
        self.slippery = slippery
        self.position = (0, 0)
        self.max_index = size - 1

    def reset(self):
        self.grid = [
            ["S", "F", "F", "F"],
            ["F", "H", "F", "H"],
            ["F", "F", "F", "H"],
            ["H", "F", "F", "G"],
        ]
        self.position = (0, 0)

    def step(self, action):
        actual_action = self._get_actual_action(action)

        new_position = self._move(actual_action)

        done = False

        reward = 0

        if new_position == (self.max_index, self.max_index):
            reward = 1
            done = True
        elif self.grid[new_position[0]][new_position[1]] == "H":  # hole
            done = True

        self.position = new_position

        return self.state, reward, done

    def _get_actual_action(self, action):
        if not self.slippery:
            return action

        perpendiculars = {
            0: [1, 3],  # LEFT: can slip DOWN or UP
            1: [0, 2],  # DOWN: can slip LEFT or RIGHT
            2: [1, 3],  # RIGHT: can slip DOWN or UP
            3: [0, 2],  # UP: can slip LEFT or RIGHT
        }

        possible_actions = perpendiculars.get(action) + [action]

        return choice(possible_actions)

    def _move(self, action):
        row, col = self.position

        # 0=LEFT, 1=DOWN, 2=RIGHT, 3=UP
        if action == 0:  # LEFT
            col = max(0, col - 1)
        elif action == 1:  # DOWN
            row = min(self.max_index, row + 1)
        elif action == 2:  # RIGHT
            col = min(self.max_index, col + 1)
        elif action == 3:  # UP
            row = max(0, row - 1)

        return (row, col)

    @property
    def state(self):
        return self.position
