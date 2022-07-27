import os
import json

files = os.listdir()

f = open("val_file.json")
data = json.load(f)
for i in data:
  # print(i[0][0])
  # print(i[0][1])
  # print(i[1][:])

  for n in files:
    if n!="rename.py":
      if n!="val_file.json":
        temp = n.split("_")
        temp[2] = temp[2].split(".")
        
        #print(temp[1]==i[0][0])
        if temp[1]==i[0][0]:
          # print(temp[2][0], i[0][1])
          if temp[2][0]==i[0][1]:
            filename = i[1][:] + ".avi"
            os.rename(n, filename)
            print(temp, i, i[1][:])

f.close


