import tkinter as tk
import time
from PIL import Image, ImageTk  #importing Pillow modules 


#Main Window
root=tk.Tk()
root.title("Photo Slide Album")
root.geometry("900x600")

#List of Image Path
image_paths=[
    r"C:\Users\pc\Downloads\Feem\img1.jpg",
    r"C:\Users\pc\Downloads\Feem\img2.jpg",
    r"C:\Users\pc\Downloads\Feem\img3.jpg",
    r"C:\Users\pc\Downloads\Feem\img4.jpg"
]

img_size=(700, 700)
images=[]

for path in image_paths:
    img=Image.open(path)
    img=img.resize(img_size)
    images.append(img)   #adding each image in the list 
    

#Convert PIL images into tkinter compatible image
photo_images=[]
for img in images:
    photo=ImageTk.PhotoImage(img)
    photo_images.append(photo)
    
#Lable widget to keep photo 
image_label=tk.Label(root)
image_label.pack(pady=20)


#Slideshow function

def start_Slideshow():
    for photo in photo_images:
        image_label.config(image=photo)
        image_label.image=photo
        root.update()
        time.sleep(2)
        
#button
play_button=tk.Button(
    root,
    text="Play the slideshow.",
    font=("Arial", 14),
    command=start_Slideshow
)

play_button.pack(pady=10)

root.mainloop()  #to keep the window open 