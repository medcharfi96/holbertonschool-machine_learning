#!/usr/bin/env python3
""" affichage du jeu jouer par un joueur entrainné """
import gym
import h5py
import keras as K
from keras import layers
from keras.optimizers import Adam
import numpy as np
from PIL import Image
from rl.core import Processor
from rl.agents.dqn import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import GreedyQPolicy
create_q_model = __import__('train').create_q_model
AtariProcessor = __import__('train').AtariProcessor


if __name__ == '__main__':
    """
    To run this on calling the method
    """
    env = gym.make('BreakoutNoFrameskip-v4')
    state = env.reset()
    actions = env.action_space.n
    model = K.models.load_model('policy.h5')
    memory = SequentialMemory(limit=1000000, window_length=4)
    policy = GreedyQPolicy()
    process = AtariProcessor()
    dqn = DQNAgent(model=model, nb_actions=actions, memory=memory,
                   policy=policy, processor=process)
    dqn.compile(optimizer=Adam(lr=.00025, clipnorm=1.0), metrics=['mae'])
    dqn.test(env, nb_episodes=10, visualize=True)