import numpy as np 
import math 

from components import * 
from tools.robot_simulator import RobotSimulator


class GenomeOperator :  

    def __init__(self, config, robot_simulator) :
        self.config = config 
        self.robot_simulator = robot_simulator
        self.shape = self._find_shape_of_controller(config)

    def _find_shape_of_controller(self, config) :
        shape = config.controller_inside_shape
        number_of_voxels = len(config.body) * len(config.body[0])
        body = np.array(config.body)
        length_observation = self.robot_simulator.get_observation_size(body)
        inputs_size = math.ceil(math.sqrt(length_observation))
        shape.insert(0, inputs_size)
        shape.append(number_of_voxels)
        return shape 



    def generate_first_generation_genome(self) :
        node = 0 
        nodes = {}
        connections = {}
        for index_of_layer in range(len(self.shape)) :
            nodes_on_layer = []
            for _ in range(self.shape[index_of_layer]) : 
                nodes_on_layer.append(node)
                nodes[index_of_layer] = nodes_on_layer
                node += 1 

        for index_of_layer in range(len(nodes.keys())) : 
            if index_of_layer == 0 :
                previous_layer = nodes[index_of_layer]  
                continue
            for node in nodes[index_of_layer] :
                for previous_node in previous_layer : 
                    weight = np.random.uniform(-1, 1)
                    connections[(previous_node, node)] = weight
            previous_layer = nodes[index_of_layer]

        return connections, nodes
    
    def crossover(self, genome1, genome2) : 
        connections_child1 = {}
        connections_child2 = {}
        nodes = genome1.nodes 

        count = 0 
        for connection in genome1.connections :
            if count % 2 == 0 :  
                connections_child1[connection] = genome1.connections[connection]
                connections_child2[connection] = genome2.connections[connection]
            else : 
                connections_child1[connection] = genome2.connections[connection]
                connections_child2[connection] = genome1.connections[connection]
            count += 1
            
        return connections_child1, connections_child2, nodes

    def mutate(self, genome, sigma) : 
        for connection in genome.connections : 
            genome.connections[connection] += np.random.normal(0, sigma)
        return genome
    

    
        

                




        
        

     
