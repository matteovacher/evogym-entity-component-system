from entity_manager import EntityManager 
from world import World 
from systems.build_system import BuildSystem
from systems.evaluation_system import EvaluationSystem
from systems.tournament_system import TournamentSystem
from config import Config 

from tools.controller_operator import ControllerOperator
from tools.genome_operator import GenomeOperator
from tools.robot_simulator import RobotSimulator
from tools.parallel_tool import ParallelTool
from tools.reporter_tool import ReporterTool


def main() : 
    entity_manager = EntityManager()
    world = World()
    config = Config("configs/config.json")

    controller_operator = ControllerOperator()
    robot_simulator = RobotSimulator(config, controller_operator)
    genome_operator = GenomeOperator(config, robot_simulator)
    parallel_tool = ParallelTool(config)
    reporter_tool = ReporterTool(config)


    build_system = BuildSystem(config, world, entity_manager, genome_operator)
    evaluation_system = EvaluationSystem(entity_manager, controller_operator, config, robot_simulator, reporter_tool, parallel_tool)
    tournament_system = TournamentSystem(entity_manager, config, genome_operator, reporter_tool)

    world.add_builder_system(build_system)
    world.add_step_system(evaluation_system)
    world.add_step_system(tournament_system)

    world.build()

    for generation in range(config.generations) : 
        world.step()

if __name__ == "__main__" : 
    main()


    

    





    
    

