


class EvaluationSystem : 
    def __init__(self, entity_manager, controller_operator, config, robot_simulator) :
        self.entity_manager = entity_manager 
        self.controller_operator = controller_operator
        self.config = config 
        self.robot_simulator = robot_simulator
        
        

    def process(self, registry) : 
        entity_ids = [id for id in registry.get_all_id_with_genome() if self.entity_manager.is_alive(id)]
        body = self.config.body 

        for entity_id in entity_ids : 
            genome = registry.get_genome(entity_id)
            node_evals, input_nodes, output_nodes = self.controller_operator.generate_controller_from_genome(genome)
            registry.add_controller(node_evals, input_nodes, output_nodes)

            controller = registry.get_controller(entity_id)
            fitness, finished = self.robot_simulator.simulate(body, controller)
            registry.add_fitness(entity_id, fitness, finished )



        







