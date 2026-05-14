import math 

from components import * 



class ControllerOperator : 
    activation_function = math.tanh
    output_activation_function = lambda x : x 
    agregation_function = sum()
    response = 1 
    bias = 0 


    def __init__(self) : 
        pass 

    def generate_controller_from_genome(self, genome) : 
        node_evals = []
        for index_of_layer in range(len(genome.nodes.keys())) : 
            if index_of_layer == 0 : 
                input_nodes = [0 for _ in range(len(genome.nodes[index_of_layer]))]
                for node in genome.nodes[index_of_layer] : 
                    input_nodes[node] = node
                previous_layer = index_of_layer
                continue 

            if index_of_layer == len(genome.nodes.keys()) - 1 : 
                output_nodes = [0 for _ in range(len(genome.node[index_of_layer]))]
                for node in genome.nodes[index_of_layer] : 
                    output_nodes[node] = node 

            for node in genome.nodes[index_of_layer] :
                inputs_of_node = []
                for previous_node in previous_layer : 
                    weight = genome.connections[(previous_node, node)]
                    inputs_of_node.append(previous_node, weight)
                node_evals.append((node, self.activation_function, self.agregation_function, self.bias, self.response, inputs_of_node))

        return node_evals, input_nodes, output_nodes
    
    def activate(self, controller, input_values) :
        values = {}
        for key, value in zip(controller.input_nodes, input_values) : 
            values[key] = value
        
        for node, activation_function, agregation_function, bias, response, inputs_of_node in controller.node_evals : 
            node_inputs = []
            for previous_node, weight in inputs_of_node : 
                node_inputs.append(values[previous_node] * weight)
            entering_node = agregation_function(node_inputs)
            values[node] = activation_function(bias + response * entering_node)
        return [self.values[node] for node in controller.output_nodes]
    



        
    

                



