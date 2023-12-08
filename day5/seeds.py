import sys
import re
import os
script_path = os.path.dirname(os.path.abspath(__file__))
# rel_file_path = 'input'
rel_file_path = 'example'
file_path = os.path.join(script_path, rel_file_path)

file_desc = open(file_path)
# file = open(sys.argv[1]).read().strip()
file = file_desc.read().strip()


# split text input by empty line
pattern = r"\n\n"
categories = re.split(pattern, file)
seeds = categories[0].split(':')[1]
seeds = [int(x) for x in seeds.split()]

seed_to_soil_map = [x for x in categories if x.startswith('seed-to-soil')][0]
seed_to_soil = seed_to_soil_map.split(':')[1].split('\n')[1:]

categories = categories[1:]
# i think i will do depth-first search

for i in range(len(categories)):
    categories[i] = categories[i].split(':\n')[1]
    # categories[i] = [int(x) for x in categories[i].split('\n')]
    categories[i] = [x for x in categories[i].split('\n')]
    for j in range(len(categories[i])):
        categories[i][j] = [cat for cat in categories[i][j].split()]
        


for i in range(len(seed_to_soil)):
    if seed_to_soil[i]: 
        seed_to_soil[i] = [int(x) for x in seed_to_soil[i].split()]
        
        # identify which maps have a range where our seeds fall on
        destination = seed_to_soil[i][0]
        source = seed_to_soil[i][1]
        range_length = seed_to_soil[i][2]
        for seed in seeds:
            if (source <= seed) and ((source + range_length) >= seed):
                # print(seed, seed_to_soil[i])
                soil_id = (seed - source) + destination
                # print(seed, soil_id) 


    
# print(lines)
file_desc.close()
print(categories)
# print(seeds)
# print(seed_to_soil)

