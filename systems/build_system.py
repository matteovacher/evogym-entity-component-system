from registry import ComponentRegistry 



class BuildSystem : 

    def __init__(self, config, entity_manager, genome_operator) :
        self.config = config
        self.entity_manager = entity_manager 
        self.genome_operator = genome_operator


    def process(self, registry) : 
        
        for _ in range(self.config.population) : 
            entity_id = self.entity_manager.create_entity()
            connections, nodes = self.genome_operator.generate_first_generation_genome()
            self.registry.add_genome(entity_id, connections, nodes)
            




        
             




        