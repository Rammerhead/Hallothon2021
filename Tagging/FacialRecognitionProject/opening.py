import cv2
import os
import json


names = open("namesofviolators.txt", 'r')

piclist = sorted(os.listdir("Violators"))

cor = {}

for i, line in enumerate(names):
    if line.strip() not in cor:
        cor[line.strip()] = list() 
    cor[line.strip()].append(piclist[i])


with open('data.json', 'w') as f:
    json.dump(cor, f)
