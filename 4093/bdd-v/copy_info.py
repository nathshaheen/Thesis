import os
import shutil

video_names = os.listdir("videos")
info_names = os.listdir("bdd100k_info/bdd100k/info/100k/val")

print(len(video_names), len(info_names))

for v in video_names:
	print(v)
	for i in info_names:
		print(i)
		if v.split(".")[0]==i.split(".")[0]:
			print("Copying: "+"bdd100k_info/bdd100k/info/100k/val/"+i+" to "+"info")
			shutil.copyfile("bdd100k_info/bdd100k/info/100k/val/"+i,"info/"+i)
			break
			

