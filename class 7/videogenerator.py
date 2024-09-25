import cv2
import os
from PIL import Image


os.chdir("class 7/images")

mean_width=0
mean_height=0

num_of_images = len(os.listdir("."))
print(num_of_images)
print(os.listdir("."))

for i in os.listdir("."):
    img=Image.open(os.path.join(i))
    width,height=img.size
    mean_width += width
    mean_height += height

    mean_height //= num_of_images
    mean_width //= num_of_images

    print(mean_width,mean_height)

    for i in os.listdir("."):
        if i.endswith('.png') or i.endswith('.jpg')or i.endswith('.jpeg'):
            img = Image.open(os.path.join(i))
            img_resized = img.resize((mean_width,mean_height),Image.Resampling.LANCZOS)
            img_resized.save(i,'JPEG',quality=96)
        print(img_resized.size)

    def videoGenerator():
        video_name = "MyFirstVideo.avi"
        images = []
        for i in os.listdir("."):
            if i.endswith(".png") or i.endswith(".jpg")or i.endswith(".jpeg"):
                images.append(i)
        print(images)
        frame = cv2.imread(os.path.join(".",images[0]))
        height,width,layers= frame.shape

        video = cv2.VideoWriter(video_name,0,1,(width,height))
        for image in images:
            video.write(cv2.imread(os.path.join(".",image)))

        video.release()