import time 


class ReporterTool : 

    def __init__(self, config) : 
        self.config = config
        self.time = time.time()


    def starting(self) : 
        print('\n')
        print('----- Running with the following config -----')
        print('\n')
        print(self.config)
        print('\n')




    def end_generation(self) : 
        passed = time.time() - self.time
        print(f' This Generation took {passed:.3f} s.')
        print ('\n')

    def start_generation(self, generation) : 
        
        self.time = time.time()
        print(f'----- Starting generation number {generation} out of {self.config.generations} -----\n')
        
        print('\n')

    def bests(self, bests) : 
        print('----- Bests of this generation -----')
        print('\t ID \t fitness ')
        print('\t====\t=========')
        for id, fitness in bests : 
            print(f'\t {id} \t {fitness:.3f}')
        
        print('\n')

    






    




    
        



