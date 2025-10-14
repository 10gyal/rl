import random
from turtle import update

from ttt import Board

env = Board()

Q = {}
gamma = 1
alpha = 0.00001
epsilon_start = 1
epsilon_end = 0.0001
epsilon_decay_rate = 0.9999999


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

import json

with open("q_table.json", "w") as f:
    # Convert tuple keys to string for JSON serialization
    serializable_Q = {f"{k[0]}_{k[1]}": v for k, v in Q.items()}
    json.dump(serializable_Q, f)


def play_game():
    """Human plays as X (player 0), Agent plays as O (player 1)"""
    env.reset()
    done = False

    while not done:
        print(env)  # Show board
        valid_moves = env.get_valid_moves()

        if env.current_player == 0:  # Human's turn
            action = int(input("Your move (0-8): "))
        else:  # Agent's turn
            action = max(valid_moves, key=lambda a: Q.get((state, a), 0.0))

        state, reward, done, info = env.step(action)

        if done:
            print(env)

    # TODO: Show result
    print("=" * 100)
    print(f"Final status: {info}")


play_game()
