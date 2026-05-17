import gymnasium as gym 
import math 
import numpy as np 
import evogym.envs 

from evogym.utils import get_full_connectivity

class RobotSimulator : 
    
    def __init__(self, config, controller_operator) : 
        self.config = config 
        self.controller_operator = controller_operator

    def _get_env(self, robot) : 
        connections = get_full_connectivity(robot)
        env = gym.make(self.config.env_name, body=robot, connections=connections)
        return env.unwrapped
    
    def get_observation_size(self, robot) : 
        env = self._get_env(robot)
        observation, _ = env.reset()
        env.close()
        del env
        return len(observation)

    def simulate(self, id, robot, controller) : 
        env = self._get_env(robot)
        reward = 0  

        observation, _ = env.reset()

        actuators = env.get_actuator_indices("robot")
        inputs_size = math.ceil(math.sqrt(len(observation)))

        finished = False 

        for _ in range (self.config.n_steps) : 
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
        return id, reward, finished 
    
    def _get_env_render(self, robot) : 
        print('----- Here is the simulated robot -----')
        connections = get_full_connectivity(robot)
        env = gym.make(self.config.env_name, body=robot, connections=connections, render_mode="rgb_array")
        return env.unwrapped

    def simulate_render(self, robot, controller) : 
        env = self._get_env_render(robot)
        fitness = 0
        observation, _ = env.reset()

        actuators = env.get_actuator_indices("robot")
        inputs_size = math.ceil(math.sqrt(len(observation)))

        images = []

        for _ in range (self.config.n_steps) : 

            images.append(env.render())

            observation.resize(inputs_size**2)
            all_actions = self.controller_operator.activate(controller, observation)
            action = np.array([all_actions[i] for i in actuators])
            observation, reward, terminated, truncated, _ = env.step(action)

            done = terminated or truncated 
            fitness += reward
            if done : 
                break 

        env.close()
        del env 
        print(f'Individual fitness : {fitness}')
        print('----- End of simulation -----')
        return images, fitness 
        
        