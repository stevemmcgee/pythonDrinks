import os

class Directories:
    
    def __init__(self, path):
        self.path = path
    #converts folder to a list of sub folders    
    def get_subfolder_paths(self):
        subfolder_paths = []
        for root, dirs, files in os.walk(self.path):
            for dir in dirs:
                subfolder_paths.append(os.path.join(root, dir))
        return subfolder_paths
       
