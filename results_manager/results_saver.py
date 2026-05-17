import os 
import json 
import dill 


class ResultsSaver :

    def __init__(self) : 
        self.path = None 
        self.number = None 
        self.abs_path_results = None
        self.save = None   

    def add_results_path(self) : 
        save = input("Do you want to save the results of this simulation ? \n \t [y] / [n] \n \t")
        if save == "y" : 
            self.save = True 
            path = input("Where do you want to store these data (please indicate the desired folder in results) : ")
            number = input("In order to classify the results, please indicate the experiment ID : ")
            self.path = path 
            self.number = number
            local_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            results_dir = os.path.join(local_dir, "results")
            self.abs_path_results = os.path.join(results_dir, '{}'.format(path), 'id_{}'.format(number))
            json_dir = os.path.join(self.abs_path_results, 'json')
            pkl_dir = os.path.join(self.abs_path_results, 'pkl')
            os.makedirs(json_dir, exist_ok=True)
            os.makedirs(pkl_dir, exist_ok=True) 

        else : 
            self.save = False 
        print('\n\n')
    
    def save_results(self, registry, config) :
        if self.save == True : 
            save_config_path = os.path.join(self.abs_path_results, 'json', 'config.json')
            with open(save_config_path, 'w') as f : 
                json.dump(config.__dict__, f, indent = 4)

            for name, component_registry in registry.__dict__.items() :
                component_path = os.path.join(self.abs_path_results, 'pkl', '{}.pkl'.format(name))
                with open(component_path, 'wb') as f : 
                    dill.dump(component_registry, f)


            print('\n----- Saved Successfully -----\n\n')

        
            
            

        
