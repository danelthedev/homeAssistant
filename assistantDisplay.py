import threading
import time
import tkinter as tk
from PIL import Image, ImageTk
import os

from tts import speak_text


class AssistantDisplay:
    def __init__(self, assistant_name='John'):
        # Setup main window
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')

        # Load images
        base_path = 'resources'
        self.images = {
            'silent': self.load_image(os.path.join(base_path, 'silent.png')),
            'talking1': self.load_image(os.path.join(base_path, 'talking1.png')),
            'talking2': self.load_image(os.path.join(base_path, 'talking2.png'))
        }

        # Create label to display images
        self.image_label = tk.Label(self.root, bg='black')
        self.image_label.pack(expand=True, fill=tk.BOTH)

        # Set initial state to silent
        self.set_silent_state()

        # Talking animation variables
        self.is_talking = False
        self.stop_talking_event = threading.Event()

    def load_image(self, path):
        """Load and resize image to fit screen"""
        try:
            image = Image.open(path)
            image = image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
            return ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error loading image {path}: {e}")
            return None

    def set_silent_state(self):
        """Display silent image"""
        self.image_label.configure(image=self.images['silent'])

    def talking_animation(self):
        """Animate talking state"""
        talking_images = [self.images['talking1'], self.images['talking2']]
        index = 0
        while not self.stop_talking_event.is_set():
            self.root.after(0, lambda i=index: self.image_label.configure(image=talking_images[i]))
            index = 1 - index  # Toggle between 0 and 1
            time.sleep(0.3)

    def speak_with_animation(self, text):
        """Speak text with talking animation"""
        # Stop any previous animation
        self.stop_talking_event.set()

        # Reset event for new animation
        self.stop_talking_event = threading.Event()

        # Start talking animation
        animation_thread = threading.Thread(target=self.talking_animation)
        animation_thread.start()

        # Speak text
        speak_text(text)

        # Stop animation
        self.stop_talking_event.set()
        animation_thread.join()

        # Return to silent state
        self.root.after(0, self.set_silent_state)

    def run(self):
        """Start the display loop"""
        self.root.mainloop()
