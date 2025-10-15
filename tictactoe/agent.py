import random
from turtle import update

from ttt import Board

env = Board()

Q = {}
gamma = 1
alpha = 0.005  # lr
epsilon_start = 1
epsilon_end = 0.1
epsilon_decay_rate = 0.99995


def get_action(state, epsilon, valid_actions):
    if random.random() < epsilon:
        return random.choice(valid_actions)
    else:
        return max(valid_actions, key=lambda a: Q.get((state, a), 0.0))


def update_Q(state, action, reward, next_state, done, valid_actions):
    if done:
        target = reward
    else:
        target = reward + (-1) * gamma * max(
            Q.get((next_state, a), 0.0) for a in valid_actions
        )
    Q[(state, action)] = Q.get((state, action), 0.0) + alpha * (
        target - Q.get((state, action), 0.0)
    )


def train(num_episodes):
    epsilon = epsilon_start
    for episode in range(num_episodes):
        if episode % 100 == 0:
            print("=" * 100)
            print(f"Episode {episode}")
            print(f"Epsilon = {epsilon}")
        state = env.reset()
        done = False

        while not done:
            valid_actions = env.get_valid_moves()

            action = get_action(state, epsilon, valid_actions)

            next_state, reward, done, info = env.step(action)

            update_Q(state, action, reward, next_state, done, env.get_valid_moves())

            state = next_state

        epsilon = max(epsilon_end, epsilon * epsilon_decay_rate)

    return Q


Q = train(100000)


def play_game():
    """Human plays as X (player 0), Agent plays as O (player 1)"""
    env.reset()
    done = False
    state = env.state
    human_player = input("Would you like to play as X or O? ").strip().lower()
    if human_player == "x":
        human_player = 0
    else:
        human_player = 1
    while not done:
        print(env)  # Show board
        print("=" * 100)
        valid_moves = env.get_valid_moves()

        if env.current_player == human_player:  # Human's turn
            while True:
                action = int(input("Your move (0-8): "))
                if action not in valid_moves:
                    print("Invalid move, try again!")
                else:
                    break

        else:  # Agent's turn
            action = max(valid_moves, key=lambda a: Q.get((state, a), 0.0))

        state, reward, done, info = env.step(action)

        if done:
            print(env)
            print("=" * 100)

        print("=" * 100)
        if reward:
            if env.current_player != human_player:
                print(f"You won!")
            else:
                print(f"You lost!")
        else:
            print(f"{info}")


while True:
    play_game()
    keep_playing = input("Keep playing? (yes/no): ").strip().lower()
    if keep_playing not in ("yes", "y"):
        print("Thanks for playing!")
        break
