import random as rd 
import numpy as np 



class TournamentSystem : 

    def __init__(self, entity_manager, config, genome_operator, reporter_tool) : 
        self.entity_manager = entity_manager
        self.config = config 
        self.genome_operator = genome_operator
        self.reporter_tool = reporter_tool 
        self.generation = 1
    
    def __str__(self) : 
        return "TournamentSystem, tournament is the selection process happening for this simulation, then we mutate the crossover of individuals"



    def process(self, registry) : 
        entity_ids = [id for id in registry.get_all_id_with_fitness() if self.entity_manager.is_alive(id)]
        new_pop_counter = 0
        number_of_winner = self.config.winner 
        number_in_tournament = self.config.tournament_number 
        max_population = self.config.population 

        parents_ids = []
        children_entity_ids = []

        self.reporter_tool.start_generation(self.generation)
        self.generation += 1 

        while len(children_entity_ids) <  max_population : 
            
            if len(parents_ids) >= 2 : 
                parent1 = parents_ids.pop()
                parent2 = parents_ids.pop()
                connections_child1, connections_child2, nodes = self.genome_operator.crossover(parent1, parent2)
                
                child_id1 = self.entity_manager.create_entity()
                children_entity_ids.append(child_id1)
                registry.add_genome(child_id1, connections_child1, nodes)
                

                if new_pop_counter == max_population : 
                    break 
                else : 
                    child_id2 = self.entity_manager.create_entity()
                    children_entity_ids.append(child_id2)
                    registry.add_genome(child_id2, connections_child2, nodes)
                
            tournament_ids = rd.sample(entity_ids, number_in_tournament)
            fitness = np.array([registry.get_fitness(id) for id in tournament_ids])
            ids_of_sorted = np.argsort(fitness)
            taken = 0 
            
            for taken in range(number_of_winner) : 
                parents_ids.insert(0, ids_of_sorted[number_in_tournament-1-taken])

        sigma = self.config.sigma_mutate 
        for child_entity_id in children_entity_ids :
            genome = registry.get_genome(child_entity_id)
            registry.modify_genome(child_entity_id, self.genome_operator.mutate(genome, sigma))
        


        for entity_id in entity_ids : 
            self.entity_manager.destroy_entity(entity_id)








            

        
