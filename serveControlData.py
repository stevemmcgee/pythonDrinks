import time
import os
import psutil
from Directories import Directories
from OpenPoseData import OpenPoseData

#process individual dictionaries
def process_data(dict):
    pass
    #print(dict)   
    
#get time at Start of processing and display
start_time=time.localtime()


#list all subfolders where JSON files are 
ds = Directories('C:\\Users\\smcge\\pythonTemp')
subfolder_paths = ds.get_subfolder_paths()
#print(subfolder_paths)

#create list of only folders containing JSON
folder_list=[]
for folder in subfolder_paths:
    if folder.endswith('JSON'):
        folder_list.append(folder)
#print(folder_list)

for folder in folder_list:
    #print(folder)

    op=OpenPoseData(folder)
    
    # Get all data into a dictionary
    file_data_dict ={}
    file_data_dict = op.extract_data()
    
    process_data(file_data_dict)
    file_data_dict.clear()

#get time at end of Processing    
end_time=time.localtime()

#display processing Time End
print('Start Time: '+str(start_time.tm_hour)+':'+str(start_time.tm_min)) 
print('End Time: '+str(end_time.tm_hour)+':'+str(end_time.tm_min)) 

# Getting % usage of virtual_memory ( 3rd field)
print('RAM memory % used:', psutil.virtual_memory()[2])
# Getting usage of virtual_memory in GB ( 4th field)
print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)  