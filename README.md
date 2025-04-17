# 🎮 Interactive Game Using Hand Gestures

A gesture-controlled game interface that replaces traditional keyboard inputs with real-time hand gesture recognition. Built using Python and OpenCV, this project offers a new way to play games like **Chrome Dino** and **Hill Climb Racing**, making gameplay more immersive and accessible.

---

## 📌 Table of Contents

- [Abstract](#abstract)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [How It Works](#how-it-works)
- [How to Run](#how-to-run)
- [Output](#output)
- [Future Work](#future-work)
- [Contributors](#contributors)
- [References](#references)

---

## 📄 Abstract

This project uses hand gestures instead of physical controllers to play simple games. It utilizes real-time webcam input, processes it using computer vision techniques, and maps specific gestures to in-game actions.

**Games Supported**:
- 🦖 Chrome Dino Game  
- 🚗 Hill Climb Racing

The goal is to improve game accessibility and provide an immersive gaming experience through intuitive hand gesture controls.

---

## ✨ Features

- Real-time hand gesture detection via webcam
- Control two games using just your hand (open palm/fist)
- Simulates keyboard inputs (space/right/left keys)
- Uses Python with OpenCV, cvzone, and ctypes
- Visual feedback on detected gestures

---

## 🛠 Tech Stack

- **Language**: Python
- **Libraries**:
  - OpenCV – for capturing webcam video and image processing
  - cvzone – for simplified hand tracking
  - ctypes – for simulating keyboard inputs
- **IDE**: PyCharm
- **Input**: Webcam
- **Output**: Game window (browser or desktop)

---

## ⚙️ How It Works

1. **Start Program**: Initializes the webcam and required libraries.
2. **Hand Detection**: Captures live video and detects hand using `cvzone.HandDetector`.
3. **Gesture Mapping**:
   - ✊ Closed Fist → Jump in Dino, Brake in Hill Climb
   - 🖐️ Open Palm → Idle in Dino, Accelerate in Hill Climb
4. **Automated Input**: Uses `ctypes` to simulate keyboard events.
5. **Visual Feedback**: Graphical indicators like rectangles and text display the detected gesture.

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hand-gesture-game.git
   cd hand-gesture-game
