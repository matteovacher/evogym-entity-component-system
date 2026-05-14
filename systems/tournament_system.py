import random as rd 
import numpy as np 

class TournamentSystem : 

    def __init__(self, entity_manager, config) : 
        self.entity_manager = entity_manager
        self.config = config 



    def process(self, registry) : 
        entity_ids = [id for id in registry.get_all_id_with_fitness() if self.entity_manager.is_alive(id)]
        new_pop_counter = 0
        number_of_winner = self.config.winner 
        number_in_tournament = self.config.tournament_number 
        max_population = self.config.population 

        parents_ids = []

        while new_pop_counter <  max_population : 

            if 
            tournament_ids = rd.sample(entity_ids, number_in_tournament)
            fitness = np.array([registry.get_fitness(id) for id in tournament_ids])
            ids_of_sorted = np.argsort(fitness)
            taken = 0 
            
            for taken in range(number_of_winner) : 
                parents_ids.append(ids_of_sorted[number_in_tournament-1-taken])








            

        
