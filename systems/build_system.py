



class BuildSystem : 

    def __init__(self, config, entity_manager, genome_operator, reporter_tool ) :
        self.config = config
        self.entity_manager = entity_manager 
        self.genome_operator = genome_operator
        self.reporter_tool = reporter_tool

    def __str__(self) : 
        return "BuildSystem, create initial population and add their genomes to registry"


    def process(self, registry) : 
        
        for _ in range(self.config.population) : 
            entity_id = self.entity_manager.create_entity()
            connections, nodes = self.genome_operator.generate_first_generation_genome()
            registry.add_genome(entity_id, connections, nodes)
        

        self.reporter_tool.starting()





        
             




        