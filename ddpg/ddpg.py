# This implementation is based on codes of Jongmin Lee & Byeong-jun Lee
import time
import random
import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp
from tqdm import tqdm
import pickle


class Actor(tf.keras.layers.Layer):

    def __init__(self, obs_shape, action_dim):
        super(Actor, self).__init__()
        assert NotImplementedError
    
    # @tf.function
    def call(self, inputs, **kwargs):
        assert NotImplementedError

    def step(self, obs, deterministic=False):
        assert NotImplementedError


class VNetwork(tf.keras.layers.Layer):

    def __init__(self, obs_shape, output_dim=1):
        super(VNetwork, self).__init__()
        assert NotImplementedError
    
    # @tf.function
    def call(self, inputs, **kwargs):
        assert NotImplementedError


class QNetwork(tf.keras.layers.Layer):

    def __init__(self, obs_shape):        
        super(QNetwork, self).__init__()
        assert NotImplementedError    
    
    # @tf.function
    def call(self, inputs, **kwargs):
        assert NotImplementedError    


class DDPG(ActorCriticRLAlgorithm):

    def __init__(self, env, ent_coef='auto', seed=0):
        super(DDPG, self).__init__()
        assert NotImplementedError    
    
    def update_target(self):
        assert NotImplementedError    
        # for target, source in zip(self.target_params, self.source_params):
        #     target.set_weights( (1 - self.tau) * target.get_weights() + self.tau * source.get_weights() ) 
                    
    # @tf.function
    def train(self, obs, action, reward, next_obs, done):
        # Casting from float64 to float32
        assert NotImplementedError    

    def learn(self, total_timesteps, log_interval=2, seed=0, callback=None, verbose=1):
        assert NotImplementedError

    def predict(self, obs, deterministic=False):
        obs_rank = len(obs.shape)
        if len(obs.shape) == 1:
            obs = np.array([obs])
        assert len(obs.shape) == 2
        
        action = self.actor.step(obs)
        
        if obs_rank == 1:
            return action[0], None
        else:
            return action, None

    def get_parameters(self):
        parameters = []
        weights = self.get_weights()
        for idx, variable in enumerate(self.trainable_variables):
            weight = weights[idx]
            parameters.append((variable.name, weight))
        return parameters

    def load_parameters(self, parameters, exact_match=False):
        assert len(parameters) == len(self.weights)
        weights = []
        for variable, parameter in zip(self.weights, parameters):
            name, value = parameter
            if exact_match:
                assert name == variable.name
            weights.append(value)
        self.set_weights(weights)

    def save(self, filepath):
        parameters = self.get_parameters()
        with open(filepath, 'wb') as f:
            pickle.dump(parameters, f, protocol=pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load(filepath, env, seed=0):
        with open(filepath, 'rb') as f:
            parameters = pickle.load(f)

        model = DDPG(env, seed=seed)
        model.load_parameters(parameters)
        return model

        