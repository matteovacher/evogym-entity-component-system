import json 
import os 

class Config : 
    def __init__(self, config_path) : 
        self.local_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_path = os.path.join(self.local_dir, config_path)

        with open(self.config_path) as f : 
            config = json.load(f)
    
        for key, value in config.items() : 
            setattr(self, key, value)

        

