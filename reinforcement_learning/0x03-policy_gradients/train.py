#!/usr/bin/env python3
"""model de ronforcement """
import numpy as np
policy_gradient = __import__('policy_gradient').policy_gradient
policy = __import__('policy_gradient').policy


def train(env, nb_episodes, alpha=0.000045, gamma=0.98, show_result=False):
    """
    ronforcement
    :param env:
    :param nb_episodes:
    :param alpha:
    :param gamma:
    :param show_result:
    """
    weight = np.random.rand(4, 2)
    nA = env.action_space.n
    episode_rewards = []
    for e in range(nb_episodes):
        state = env.reset()[None, :]
        grads = []
        rewards = []
        score = 0

        while True:
            if show_result and not e % 1000:
                env.render()
            probs = policy(state, weight)
            action = np.random.choice(nA, p=probs[0])
            next_state, reward, done, _ = env.step(action)
            next_state = next_state[None, :]

            grad = policy_gradient(state, probs, action)
            grads.append(grad)

            grads.append(grad)
            rewards.append(reward)

            score += reward
            state = next_state

            if done:
                break

        for i in range(len(grads)):
            aux = sum([r * (gamma ** r) for t, r in enumerate(rewards[i:])])
            weight += alpha * grads[i] * aux

        episode_rewards.append(score)
        print("EP: " + str(e) + " Score: " + str(score) + "        ",
              end="\r", flush=False)

    return episode_rewards
