from random import choice, random
from fl import FrozenLake


class QLearningAgent:
    def __init__(self, n_actions=4, alpha=0.1, gamma=0.99, epsilon=1.0):
        self.q_table = {}
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor
        self.epsilon = epsilon  # exploration rate
        self.n_actions = n_actions

    def get_q_value(self, state, action):
        # Return Q(s,a), initialize to 0 if not seen
        return self.q_table.get((state, action), 0.0)

    def choose_action(self, state):
        # Epsilon-greedy action selection
        action = choice([0, 1, 2, 3])
        if random() < self.epsilon:
            return action
        else:
            return max([0, 1, 2, 3], key=lambda a: self.q_table.get((state, a), 0.0))

    def update(self, state, action, reward, next_state, done):
        # Q-learning update rule
        current_q = self.get_q_value(state, action)
        max_next_q = max(self.get_q_value(next_state, a) for a in range(self.n_actions))
        target = reward + self.gamma * max_next_q if not done else reward

        self.q_table[(state, action)] = current_q + self.alpha * (target - current_q)


def train(
    env: FrozenLake,
    agent: QLearningAgent,
    n_episodes=10000,
    epsilon_decay=0.995,
    epsilon_min=0.01,
):
    rewards_history = []
    for episode in range(n_episodes):
        state = env.reset()
        total_reward = 0
        done = False

        while not done:
            # 1. Choose action
            action = agent.choose_action(state)
            # 2. Take action in environment
            next_state, reward, done = env.step(action)
            # 3. Update Q-table
            agent.update(state, action, reward, next_state, done)
            # 4. Update state
            state = next_state
            total_reward += reward

        # Decay epsilon
        agent.epsilon = max(epsilon_min, agent.epsilon * epsilon_decay)

        rewards_history.append(total_reward)

        # Print progress every 1000 episodes
        if (episode + 1) % 1000 == 0:
            recent_success = sum(rewards_history[-100:]) / 100
            print(
                f"Episode {episode+1}, Success rate: {recent_success:.2%}, Epsilon: {agent.epsilon:.3f}"
            )

    return rewards_history


FL = FrozenLake()
Agent = QLearningAgent(n_actions=4, alpha=0.2, gamma=0.99, epsilon=1)
train(env=FL, agent=Agent, n_episodes=100000, epsilon_decay=0.995, epsilon_min=0.01)
