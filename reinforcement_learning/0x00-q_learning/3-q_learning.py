#!/usr/bin/env python3
import numpy as np


def train(env, Q, episodes=5000, max_steps=100, alpha=0.1,
          gamma=0.99, epsilon=1, min_epsilon=0.1, epsilon_decay=0.05):
    RP_ep = []
    init_epsilon = epsilon
    for epd in range(episodes):
        current_state = env.reset()
        done = False

        tot_rewards = 0

        for i in range(max_steps):
            if np.random.uniform(0, 1) < epsilon:
                action = np.random.randint(0, Q.shape[1])

            else:
                action = np.argmax(Q[current_state])
            etp_suiv, reward, done, _ = env.step(action)

            if done is True and reward == 0:
                reward = -1

            Q[current_state, action] = (1 - epsilon) * \
                                       Q[current_state, action] + \
                                       alpha * \
                                       (reward + gamma * max(Q[etp_suiv]))
            tot_rewards = tot_rewards + reward
            if done is True:
                break
            current_state = etp_suiv
        epsilon = min_epsilon + (init_epsilon - min_epsilon) * \
                  np.exp(-epsilon_decay * epd)
        RP_ep.append(tot_rewards)
    return Q, RP_ep
