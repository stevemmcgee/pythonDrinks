import tkinter as tk
from PIL import Image, ImageTk
import requests

class ImageFrame(tk.Frame):
    def __init__(self, parent, url):
        tk.Frame.__init__(self, parent)
        
        # Download image from URL
        response = requests.get(url)
        img_data = response.content
        print('Image Retrieved: '+ response.status_code.__str__())
        
        # Convert image to Tkinter PhotoImage
        img = Image.open(Image.io.BytesIO(img_data))
        photo = ImageTk.PhotoImage(img)
        
        # Create label widget and add to frame
        label = tk.Label(self, image=photo)
        label.image = photo  # Keep a reference to the image to prevent garbage collection
        label.grid(row=0, column=0)