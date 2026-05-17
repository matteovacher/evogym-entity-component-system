import os 
import json 
import dill 

class ResultsLoader : 
    def __init__(self) : 
        pass 

    def loader(self) : 
        path = input('From which folder do you want to get the results : ')
        number = input('From which experiment ID do you want to get the results : ')
        local_dir =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        results_dir = os.path.join(local_dir, 'results', '{}'.format(path), 'id_{}'.format(number))
        self.__setattr__('results_dir', results_dir)
        json_dir  = os.path.join(results_dir, 'json')
        pkl_dir = os.path.join(results_dir, 'pkl')

        file = 'config.json'
        json_dir_file = os.path.join(json_dir, file)
        with open(json_dir_file, 'r') as f : 
            if file.endswith('.json') :
                file = file.removesuffix('.json')
            data_config = json.load(f)
            self.__setattr__(file, data_config)

        for file in os.listdir(pkl_dir) : 
            file_dir = os.path.join(pkl_dir, file)
            with open(file_dir, 'rb') as f : 
                if file.endswith('.pkl') :
                    file = file.removesuffix('.pkl')
                loaded_object = dill.load(f)
                self.__setattr__(file, loaded_object)


            