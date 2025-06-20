# Gesture-Controlled YouTube Navigation 🎥🖐️

A Python application that allows users to control YouTube playback using hand gestures detected through a webcam. It uses **MediaPipe** for hand tracking, **OpenCV** for camera input, **PyAutoGUI** for simulating keyboard controls, and **Tkinter** for the GUI.

## 🚀 Features

- Hands-free control of YouTube playback
- Real-time gesture recognition using webcam
- GUI to start and stop detection
- Automatically opens a YouTube video
- Cross-platform compatible (Windows/Linux/Mac)

## ✋ Supported Gestures

| Gesture             | Action        |
|---------------------|---------------|
| Index finger up     | Play/Pause    |
| Index + Middle up   | Forward       |
| All fingers up      | Volume Up     |
| Fist (no fingers)   | Volume Down   |

## 🧱 Project Structure

```
gesture_youtube_control/
├── main.py               # App entry point
├── gui.py                # GUI for gesture control
├── gesture_detector.py   # MediaPipe and gesture logic
└── requirements.txt      # Required libraries
```

## Installation

1. Clone the repo:
```bash
git clone https://github.com/your-username/gesture_youtube_control.git
cd gesture_youtube_control
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

## Demo

https://github.com/your-username/gesture_youtube_control/assets/demo.mp4 *(Add a demo video of your gesture control in action)*

## Tech Stack

- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- Tkinter

## Future Work

- Add support for custom gesture training with ML
- Include voice + gesture hybrid control
- Log gesture history and generate analytics

## License

MIT License

---

Built by Mithra V
