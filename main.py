import os
import openai
import tkinter as tk
import urllib.request
from PIL import Image, ImageTk
from io import BytesIO

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.url_label = tk.Label(self, text="Enter what you wanna generate:")
        self.url_label.pack()

        self.url_entry = tk.Entry(self)
        self.url_entry.pack()

        self.submit_button = tk.Button(self, text="Submit request", command=self.show_image)
        self.submit_button.pack()

    def show_image(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

        response = openai.Image.create(
            prompt= self.url_entry.get(),
            n=1,
            size="1024x1024"
        )

        url = response['data'][0]['url']
        try:
            image_data = urllib.request.urlopen(url).read()
            image_buffer = BytesIO(image_data)

            image = Image.open(image_buffer)
            image.show()
        except:
            print("Error loading image from URL")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
