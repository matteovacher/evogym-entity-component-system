from components import * 

class ComponentRegistry : 

    def __init__(self) : 
        self.genome_registry = {}
        self.fitness_registry = {}
        self.controller_registry = {}

    # ADDER METHODS
    def add_genome(self, entity_id, connections, nodes) : 
        self.genome_registry[entity_id] = GenomeComponent(connections, nodes)
    
    def add_fitness(self, entity_id, fitness, finished) : 
        self.fitness_registry[entity_id] = FitnessComponent(fitness, finished)

    def add_controller(self, entity_id, node_evals, input_nodes, output_nodes) : 
        self.controller_registry[entity_id] = ControllerComponent(node_evals, input_nodes, output_nodes)
    
    # GETTER METHODS
    def get_genome(self, entity_id) : 
        return self.genome_registry[entity_id]

    def get_fitness(self, entity_id) : 
        return self.fitness_registry[entity_id]
    
    def get_controller(self, entity_id) : 
        return self.controller_registry[entity_id]
    
    # CHECKER METHODS 
    def has_genome(self, entity_id) : 
        return entity_id in self.genome_registry
    
    def has_fitness(self, entity_id) : 
        return entity_id in self.fitness_registry
    
    def has_controller(self, entity_id) :
        return entity_id in self.controller_registry 

    
    # ADVANCED GETTER METHODS 
    def get_all_id_with_genome(self) : 
        return self.genome_registry.keys()
    
    def get_all_id_with_fitness(self) : 
        return self.fitness_registry.keys()
    
    def get_all_with_controller(self) : 
        return self.controller_registry.keys()
    
    # MODIFIERS, please give an object 
    def modify_genome(self, entity_id, genome) : 
        self.genome_registry[entity_id] = genome
        
    def modify_fitness(self, entity_id, fitness) : 
        self.fitness_registry[entity_id] = fitness 
    
    def modify_controller(self, entity_id, controller) : 
        self.controller_registry[entity_id] = controller
    
    # CLEARER METHODS 
    def clear_all_except_genome(self) : 
        self.fitness_registry.clear()

    def clear_genome(self) : 
        self.genome_registry.clear()

    def clear_fitness(self) : 
        self.fitness_registry.clear()

    def clear_controller(self) : 
        self.controller_registry.clear()

    