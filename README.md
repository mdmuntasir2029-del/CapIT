# 👂 CappIT: Offline Real-Time Subtitles
A handheld accessibility device for the hearing impaired. No Wi-Fi. No Cloud. Just speech-to-text.

## 📺 Try the Online Simulation
I've built a functional web prototype so you can see how it works before I build the hardware!
👉 **(https://github.com/mdmuntasir2029-de)**

## 💡 Why this matters
Hearing aids are expensive and often struggle in noisy rooms. This project uses an offline **Vosk AI engine** on a Raspberry Pi 4 to provide zero-latency captions on a high-contrast 3.2" screen. It’s designed to be portable, private, and 100% independent of the internet.

## 🛠️ Implementation Plan
1. **Frontend:** Custom Python GUI (Tkinter) optimized for the Waveshare 320x240 display.
2. **Backend:** Vosk-API running a Kaldi-based neural network for speech recognition.
3. **Hardware:** Compact "sandwich" design with the LCD HAT mounted directly on the Pi 4.

## 📝 Grant Request
I am requesting **$120** to cover the components listed in `BOM.csv`. This will allow me to transition from a web simulation to a physical, life-changing tool.
