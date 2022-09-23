import os
import json


# path = "F:\\Download\\A_Programming\\sampleJson"
path = os.getcwd()  # Complate Path Or Folder Path
p = os.listdir(path)  # All File

# Initialization  Start->

dataset_name = list()  # List Of All valid dataset
annotation_objects = {
    'car': {
        "presence": 0,
        "bbox": list()
    },
    'number': {
        "presence": 0,
        "bbox": list()
    },
}

annotation_attributes = {
    'car': {
        "Type": list(),
        "Pose": list(),
        "Model": list(),
        "Make": list(),
        "Color": list(),
    },
    'number': {
        "Difficulty_Score": list(),
        "Value": list(),
        "Occlusion": 0,
    },
}
# Initialization  End <-


for file in p:  # Looping all file in Folder
    if ('formatted' not in file) & ('pos' in file):  # Check Condition
        with open(file) as f:  # Read Each File
            data = json.load(f)
            if len(data['objects']) > 0:  # Not Empty
                dataset_name.append(file)  # File Name

                try:   # Annotation_objects Car (vehicle)
                    box = list()
                    box.append(data['objects'][0]['points']['exterior'][0][0])
                    box.append(data['objects'][0]['points']['exterior'][0][1])
                    box.append(data['objects'][0]['points']['exterior'][1][0])
                    box.append(data['objects'][0]['points']['exterior'][1][1])
                    annotation_objects["car"]['bbox'].append(box)
                    annotation_objects["car"]['presence'] += 1
                except:
                    pass
                try:     # Annotation_objects Number (license_plate)
                    box = list()
                    box.append(data['objects'][1]['points']
                               ['exterior'][0][0])
                    box.append(data['objects'][1]['points']
                               ['exterior'][0][1])
                    box.append(data['objects'][1]['points']
                               ['exterior'][1][0])
                    box.append(data['objects'][1]['points']
                               ['exterior'][1][1])
                    annotation_objects["number"]['bbox'].append(box)
                    annotation_objects["number"]['presence'] += 1
                except:
                    pass
                try:     # Annotation_attributes Car(vehicle)
                    annotation_attributes['car']['Type'].append(
                        data['objects'][0]['tags'][0]['value'])
                    annotation_attributes['car']['Pose'].append(
                        data['objects'][0]['tags'][1]['value'])
                    annotation_attributes['car']['Model'].append(
                        data['objects'][0]['tags'][2]['value'])
                    annotation_attributes['car']['Make'].append(
                        data['objects'][0]['tags'][3]['value'])
                    annotation_attributes['car']['Color'].append(
                        data['objects'][0]['tags'][4]['value'])
                except:
                    pass

                try:    # Annotation_attributes number(license_plate)
                    annotation_attributes['number']['Difficulty_Score'].append(
                        data['objects'][1]['tags'][0]['value'])
                    annotation_attributes['number']['Value'].append(
                        data['objects'][1]['tags'][1]['value'])
                except:
                    pass


formated_combine = {  # Json Structure
    'dataset_name': dataset_name,
    "image_link": "",
    "annotation_type": "image",
    'annotation_objects': annotation_objects,
    'annotation_attributes': annotation_attributes
}

#*Save File As formatted in same folder as Always Writing Mood (Write)#
with open('formatted_combine.png.json', 'w') as w:
    w.write(json.dumps(formated_combine, indent=4))

#*Consol Print (Read)#
with open('formatted_combine.png.json', 'r') as r:
    Pdata = json.loads(r.read())
    print(json.dumps(Pdata, indent=4))
