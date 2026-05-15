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
        print('----- Running with the following systems -----')
        print('\n')




    def start_generation(self, generation) : 
        self.time = time.time()
        print(f'----- Starting generation number {generation} out of {self.config.generations} -----')
        print ('\n')

    def end_generation(self, dict_of_best) : 
        
        passed = time.time() - self.time
        print('----- Results of this generation -----')
        print('\n')
        print(' ID \t fitness ')
        print('====\t=========')
        for key, value in dict_of_best.items() : 
            print(f' {key} \t {value:.3f}')
        print('\n')
        print(f' This Generation took {passed} s.')

    






    




    
        



