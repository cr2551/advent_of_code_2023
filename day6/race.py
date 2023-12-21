# file path
import os
scipt_path = os.path.dirname(os.path.abspath(__file__))
fname = 'input'
# fname = 'example'
fp = os.path.join(scipt_path, fname)

with open(fp, 'r') as f:
    text = f.read()
times, distances = text.splitlines()
times = times.split(':')[1].split()
distances = distances.split(':')[1].split()

mult = 1
races = list(zip(times, distances))
for race in races:
    time = int(race[0])
    dist = int(race[1])
    for ms in range(1, int(time)): # for millisecond in time
        mm = ms * (time - ms)
        if mm > dist:
            break # we only need the first ms when we can win the race to calculate the number of ways
    n = time - (ms*2) + 1 # +1 milisecond from 0-1 
    # print(n)
    if n != 0:
        mult *= n


print(races)
print(mult)

