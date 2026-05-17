
class GenomeComponent : 

    def __init__(self, connections, nodes) : 
        self.connections = connections 
        self.nodes = nodes 


class FitnessComponent : 

    def __init__(self, fitness, finished) : 
        self.fitness = fitness 
        self.finished = finished 

class ControllerComponent : 
    def __init__(self, node_evals, input_nodes, output_nodes) : 
        self.node_evals = node_evals  
        self.input_nodes = input_nodes 
        self.output_nodes = output_nodes 



    

