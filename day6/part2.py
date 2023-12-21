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
time = ''.join(times)
time = int(time)
distances = distances.split(':')[1].split()
distance = ''.join(distances)
distance = int(distance)
print(time, distance)
for ms in range(1, time): # for millisecond in time
    mm = ms * (time - ms)
    if mm > distance:
        break # we only need the first ms when we can win the race to calculate the number of ways
n = time - (ms*2) + 1 # +1 milisecond from 0-1 
print(n)



