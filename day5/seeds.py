import sys
import re
import os
script_path = os.path.dirname(os.path.abspath(__file__))
rel_file_path = 'input'
# rel_file_path = 'example'
file_path = os.path.join(script_path, rel_file_path)

file_desc = open(file_path)
# file = open(sys.argv[1]).read().strip()
file = file_desc.read().strip()


# split text input by empty line
pattern = r"\n\n"
categories = re.split(pattern, file)

# parse text to create seeds array
seeds = categories[0].split(':')[1]
seeds = [int(x) for x in seeds.split()]


categories = categories[1:]
# i think i will do depth-first search


# convert categories into a 3d array that we can follow
for i in range(len(categories)):
    categories[i] = categories[i].split(':\n')[1]
    # categories[i] = [int(x) for x in categories[i].split('\n')]
    categories[i] = [cat for cat in categories[i].split('\n')]
    for j in range(len(categories[i])):
        categories[i][j] = [int(x) for x in categories[i][j].split()]

locations = []
# now search
for seed in seeds:
    source  = seed
    for i in range(len(categories)):
        matched = False
        for j in range(len(categories[i])):
            # destination range start
            dest_start = categories[i][j][0]
            # source range start
            source_start = categories[i][j][1]
            # the length of the range
            range_length = categories[i][j][2]
            if source >= source_start and (source_start + range_length) >= source:
                matched = True
                dest_id  = (source - source_start) + dest_start
                source = dest_id
                break
    locations.append(dest_id)
    # print(seed, dest_id)

file_desc.close()
# print(categories)
# print(locations)
print(min(locations))

# print(seeds)

