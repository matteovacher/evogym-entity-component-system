import gymnasium as gym 
import math 
import numpy as np 
import evogym.envs 

from tools.controller_operator import ControllerOperator

from evogym.utils import get_full_connectivity

from components import * 

class RobotSimulator : 
    
    def __init__(self, env_name, n_steps, controller_operator) : 
        self.env_name = env_name 
        self.n_steps = n_steps
        self.controller_operator = controller_operator

    def _get_env(self, robot) : 
        connections = get_full_connectivity(robot)
        env = gym.make(self.env_name, body=robot, connections=connections)
        return env
    
    def get_observation_size(self, robot) : 
        env = self._get_env(self, robot)
        observation, _ = env.reset()
        env.close()
        del env
        return len(observation)

    def simulate(self, robot, controller) : 
        env = self._get_env(self, robot)
        reward = 0  

        observation, _ = env.reset()

        actuators = env.get_actuator_indices("robot")
        inputs_size = math.ceil(math.sqrt(len(observation)))

        finished = False 

        for _ in range (self.n_steps) : 
            observation.resize(inputs_size**2)
            all_actions = self.controller_operator.activate(controller, observation)
            action = np.array([all_actions[i] for i in actuators])
            observation, step_reward, terminated, truncated, _ = env.step(action)

            reward += step_reward

            done = terminated or truncated 

            if done : 
                finished = True 
                break 

        env.close()
        del env 
        return reward, finished 

