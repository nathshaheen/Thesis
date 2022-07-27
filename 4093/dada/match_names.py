import os

camera_videos = os.listdir("camera_videos")
gazemap_videos = os.listdir("gazemap_videos")

for i in range(len(camera_videos)):
    camera_videos[i] = camera_videos[i].split(".")[0]

for i in range(len(gazemap_videos)):
    gazemap_videos[i] = gazemap_videos[i].split(".")[0]

matches = []
for i in camera_videos:
    for n in gazemap_videos:
        if i == n:
            matches.append(i)

print(len(camera_videos), len(gazemap_videos), len(matches))
