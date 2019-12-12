import argparse

import gym
import numpy as np

from sac import SAC

def main(args):
    """
    Train and save the SAC model, for the halfcheetah problem

    :param args: (ArgumentParser) the input arguments
    """
    env = gym.make("HalfCheetah-v2")

    model = SAC(env=env, ent_coef=0.001)
    
    model.learn(total_timesteps=args.max_timesteps)
    model.save("halfcheetah_model.zip")
    print("Saving model to halfcheetah_model.zip")

    # model.learn(total_timesteps=100)
    # model.load("halfcheetah_model.zip")

    model.evaluate(5)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Train SAC on HalfCheetah")
    parser.add_argument('--max-timesteps', default=1000000, type=int, help="Maximum number of timesteps")
    args = parser.parse_args()
    main(args)
