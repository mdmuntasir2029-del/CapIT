import os
import sys
import queue
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import tkinter as tk

# 1. Setup the Display (Optimized for 3.2" 320x240 screen)
root = tk.Tk()
root.title("Pi-Caption")
root.attributes('-fullscreen', True)
root.configure(background='black')

label = tk.Label(root, text="Waiting for speech...", font=("Arial", 24), 
                 fg="white", bg="black", wraplength=300, justify="left")
label.pack(expand=True, fill='both', padx=10, pady=10)

# 2. Setup Audio Queue
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

# 3. Load Offline AI Model (Vosk)
# Download model from alphacephei.com/vosk/models
model = Model("model") 
rec = KaldiRecognizer(model, 16000)

def update_transcription():
    while not q.empty():
        data = q.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result.get("text", "")
            if text:
                label.config(text=text)
        else:
            partial = json.loads(rec.PartialResult())
            # Real-time update as you speak
            if partial.get("partial"):
                label.config(text=partial["partial"])
    
    root.after(100, update_transcription)

# 4. Start Listening
with sd.RawInputStream(samplerate=16000, blocksize=8000, device=None,
                       dtype='int16', channels=1, callback=callback):
    update_transcription()
    root.mainloop()
