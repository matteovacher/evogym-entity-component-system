import os 
import json 
import dill 
import numpy as np 
import imageio as io 

from config import Config

from results_manager.results_loader import ResultsLoader
from tools.robot_simulator import RobotSimulator
from tools.controller_operator import ControllerOperator


def render() : 
    
    results_loader = ResultsLoader()
    results_loader.loader()

    config = Config(results_loader.config)

    controller_operator = ControllerOperator()
    robot_simulator = RobotSimulator(config, controller_operator)
    config = Config(results_loader.config)

    id = input("Please indicate the ID of the individual you want to render : ")
    id = int(id)

    video_dir = os.path.join(results_loader.results_dir, 'video')
    os.makedirs(video_dir, exist_ok=True)

    video_mp4_path = os.path.join(video_dir, 'id_{}.mp4'.format(id))
    video_gif_path = os.path.join(video_dir, 'id_{}.gif'.format(id))



    controller = results_loader.controller_registry[id]
    
    robot = np.array(config.body)
    images, fitness = robot_simulator.simulate_render(robot, controller)
        
    print('\n----- Rendering the simulation -----\n')
    io.mimwrite(video_mp4_path, images, fps=30, macro_block_size=1)
    io.mimwrite(video_gif_path, images, fps=30, macro_block_size=1)

    print('\n----- Saved Successfully -----\n')



if __name__ == "__main__" : 
    render()
    
    


