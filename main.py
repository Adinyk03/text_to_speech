import tkinter as tk
from gtts import gTTS
import subprocess
import time


# Function to convert and save the speech
def convert_and_save_speech():
    text_to_speak = text_entry.get()
    if text_to_speak:
        # Create a gTTS object
        tts = gTTS(text=text_to_speak, lang='en')

        # Generate a unique filename based on the current timestamp
        timestamp = str(int(time.time()))
        audio_filename = f"speech_{timestamp}.mp3"

        # Save the speech to the generated audio file
        tts.save(audio_filename)

        # Play the saved audio using the afplay command
        subprocess.run(["afplay", audio_filename])


# Create a GUI window
window = tk.Tk()
window.title("Text - Speech Converter")

# Label
label = tk.Label(window, text="Text: ")
label.pack()

# Text Entry
text_entry = tk.Entry(window)
text_entry.pack()

# Convert and Save Button
convert_button = tk.Button(window, text="Convert", command=convert_and_save_speech)
convert_button.pack()

# Quit Button
quit_button = tk.Button(window, text="End", command=window.quit)
quit_button.pack()

# Run the GUI application
window.mainloop()

# Close the GUI window
window.destroy()
