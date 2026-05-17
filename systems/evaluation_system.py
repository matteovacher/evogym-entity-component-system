import numpy as np 



class EvaluationSystem : 
    def __init__(self, entity_manager, controller_operator, config, robot_simulator, reporter_tool, parallel_tool) :
        self.entity_manager = entity_manager 
        self.controller_operator = controller_operator
        self.config = config 
        self.robot_simulator = robot_simulator
        self.reporter_tool = reporter_tool 
        self.parallel_tool = parallel_tool 
        self.generation = 1
    
    def __str__(self) : 
        return "EvaluationSystem, evaluate al individuals in the current population and add their fitness to registry"
        
        

    # def process(self, registry) : 
    #     entity_ids = [id for id in registry.get_all_id_with_genome() if self.entity_manager.is_alive(id)]
    #     body = self.config.body 
    #     fitnesses = [] 

    #     for entity_id in entity_ids : 
    #         genome = registry.get_genome(entity_id)
    #         node_evals, input_nodes, output_nodes = self.controller_operator.generate_controller_from_genome(genome)
    #         registry.add_controller(node_evals, input_nodes, output_nodes)

            
    #         controller = registry.get_controller(entity_id)
    #         fitness, finished = self.robot_simulator.simulate(body, controller)
    #         fitnesses.append(fitness)
    #         registry.add_fitness(entity_id, fitness, finished )

    #     fitnesses = np.array(fitnesses)
    #     arg_sorted_fitnesses = np.argsort(fitnesses)
    #     dict_of_best = {}
    #     number_of_reported_individuals = self.config.number_of_reported_individuals
    #     for taken in range(number_of_reported_individuals) : 
    #         id = arg_sorted_fitnesses[number_of_reported_individuals - 1 - taken]
    #         dict_of_best[id] = registry.get_fitness(id)[0]
        
    #     self.reporter_tool.end_generation(dict_of_best)


    def process(self, registry) : 

        self.reporter_tool.start_generation(self.generation)
        self.generation += 1

        entity_ids = [id for id in registry.get_all_id_with_genome() if self.entity_manager.is_alive(id)]

        for entity_id in entity_ids : 
            genome = registry.get_genome(entity_id)
            node_evals, input_nodes, output_nodes = self.controller_operator.generate_controller_from_genome(genome)
            registry.add_controller(entity_id, node_evals, input_nodes, output_nodes)

        controllers = [registry.get_controller(entity_id) for entity_id in entity_ids]
        body = self.config.body 
        bodies = [np.array(body) for _ in range(len(entity_ids))] 

        function = self.robot_simulator.simulate
        chunk = list(zip(entity_ids, bodies, controllers))

        results = self.parallel_tool.run(function, chunk)
        fitnesses = []
        ids = []
        for entity_id, fitness, finished in results : 
            ids.append(entity_id)
            fitnesses.append(fitness)
            registry.add_fitness(entity_id, fitness, finished)

        fitnesses = np.array(fitnesses)
        arg_sorted_fitnesses = np.argsort(fitnesses)
        bests = []
        number_of_reported_individuals = self.config.number_of_reported_individuals
        for taken in range(number_of_reported_individuals) : 
            id = arg_sorted_fitnesses[len(entity_ids) - 1 - taken]
            bests.append((ids[id], fitnesses[id]))
            
        
        self.reporter_tool.bests(bests)

            
        








                    



        







