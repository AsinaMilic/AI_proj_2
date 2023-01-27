import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

language = "sr"


def play():
    text_from_user = myText.get("1.0", "end-1c")
    if text_from_user == "":
        messagebox.showerror("Error", "Please enter some text.")
        return

    output = gTTS(text=text_from_user, lang=language, slow=False)
    output.save("tts_audio.mp3")
    os.system("tts_audio.mp3")


root = tk.Tk()
root.bg = "yellow"
root.title("Serbian Text to Speech")
root.resizable(width=False, height=False)

inputValue = tk.StringVar()
myText = tk.Text(root, width=70, height=15, bg="white", fg="orange", font=("verdana", 16))
myText.config(highlightbackground="black", highlightcolor="black", highlightthickness=1)
myText.grid(row=0, column=0)

playButton = tk.Button(root, text="Play", bg="green", width=8, height=2, font=("Arial", 12, "bold"), fg='white',
                       command=play)
playButton.grid(row=1)

root.mainloop()
