import os
import shutil

video_names = os.listdir("videos")
info_names = os.listdir("info")

print(len(video_names), len(info_names))

count = 0
for v in video_names:
	for i in info_names:
		if v.split(".")[0]==i.split(".")[0]:
			count += 1
			break		

print(count)

