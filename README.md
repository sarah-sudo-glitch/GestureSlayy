GestureSlayy - AI-Powered Gesture Control System
Touch-free control for your computer using hand gestures

GestureSlayy is a computer vision–based gesture control system developed using Python, OpenCV, and MediaPipe. The project enables users to interact with their computer through real-time hand gestures captured using a webcam, reducing dependence on traditional input devices such as a keyboard and mouse.

✨ Features
Gesture	Action
👈 Left hand swipe	Navigate to previous slide (PowerPoint)
👉 Right hand swipe	Navigate to next slide (PowerPoint)
☝️ Upward gesture	Scroll up (PDF/Web)
👇 Downward gesture	Scroll down (PDF/Web)
🤏 Pinch (Thumb + Index)	Volume control – distance-based adjustment
✋ Custom predefined gesture	Play/Pause media

🏗️ How It Works
text
Webcam Input → MediaPipe Hand Tracking → Gesture Recognition → System Action
Hand Detection – MediaPipe extracts 21 hand landmarks in real-time
Gesture Analysis – Custom logic interprets finger positions and movements
Action Execution – PyAutoGUI and system libraries trigger the corresponding controls

Webcam Input
      ↓
MediaPipe Hand Tracking
      ↓
Gesture Recognition
      ↓
System Action Execution



🛠️ Tech Stack
Technology	Purpose
Python 3.8+	Core programming language
OpenCV	Webcam capture and video frame processing
MediaPipe	High-fidelity hand landmark detection
PyAutoGUI	Mouse/keyboard automation & screen control
NumPy	Distance calculations and coordinate mapping
OS/System libs	Volume control and media playback commands


📦 Installation
Prerequisites
Python 3.8 or higher

Webcam

pip package manager

Steps
bash
# 1. Clone the repository
git clone https://github.com/sarah-sudo-glitch/GestureSlayy.git
cd GestureSlayy

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
requirements.txt:

text
opencv-python>=4.5.0
mediapipe>=0.9.0
pyautogui>=0.9.53
numpy>=1.21.0


🚀 Usage
Basic Run
bash
python main.py


Control Guide
Action	Hand Gesture
PowerPoint Previous	Move hand left
PowerPoint Next	Move hand right
Scroll Up	Move hand up
Scroll Down	Move hand down
Volume Up	Increase thumb-index distance
Volume Down	Decrease thumb-index distance
Play/Pause	Show predefined gesture
Press q to quit the application.

📁 Project Structure
text
GestureSlayy/
├── lear_ges.py    #working of the project 
├── requirements.txt     # Dependencies
├── README.md            # This file


🧠 Implementation Highlights
Real-time processing – Optimized pipeline for smooth 30 FPS performance

Landmark-based geometry – Uses MediaPipe's 21-point hand model for precise tracking

Distance-based volume control – Continuous mapping of finger distance to system volume

Swipe detection – Directional movement analysis for slide/scrolling navigation




🔮 Future Enhancements
Add custom gesture training mode
Support for multi-hand gestures
On-screen gesture feedback overlay
Mouse cursor control with fingertip tracking
Improved stability with temporal smoothing
Voice + gesture hybrid commands


🙏 Acknowledgments
MediaPipe – Hand tracking solution
OpenCV – Computer vision library
PyAutoGUI – Automation library



# GestureSlayy
