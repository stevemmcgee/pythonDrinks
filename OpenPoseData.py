import json
import os
import time

list_of_dicts ={}

class OpenPoseData:
    
    def __init__(self, directory):
        self.directory = directory
        
        #Define KeyPoints
        self.keypoints = ['Nose', 'Neck', 'RShoulder', 'RElbow', 'RWrist',
                          'LShoulder', 'LElbow', 'LWrist', 'MidHip', 'RHip',
                          'RKnee', 'RAnkle', 'LHip', 'LKnee', 'LAnkle', 'REye',
                          'LEye', 'REar', 'LEar', 'LBigToe', 'LSmallToe',
                          'LHeel', 'RBigToe', 'RSmallToe', 'RHeel',]
    
    #Puts JSON files into a Dictionary and Adds to a List
    def extract_data(self):
        data = {}
        file_count=0
        for file_name in os.listdir(self.directory):
            
            if file_name.endswith('.json'):
                with open(os.path.join(self.directory, file_name), 'r') as f:
                    json_data = json.load(f)
                    print(json_data)
                    for person in json_data['people']:
                        keypoint_data = person['pose_keypoints_2d']
                        for i in range(len(keypoint_data)):
                            if i % 3 == 0:
                                keypoint = self.keypoints[i // 3]
                                #print(keypoint)
                                if keypoint not in data:
                                    data[keypoint] = []
                                    #print(data[keypoint])
                                    
                                data[keypoint]=(keypoint_data[i], keypoint_data[i+1])
                                print(keypoint,data[keypoint], sep=': ' )
                                #print(file_name)
                                file_name.split('_')
                                #time.sleep(1)


            #Creates dictionary with Name of file prior to first "_" and a correlating number of the file in the folder
            list_of_dicts[file_name.split('_')[0] +' '+ str(file_count)]=data
            file_count+=1   
            
        print(list_of_dicts)         
        return list_of_dicts