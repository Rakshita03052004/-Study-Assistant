# -Study-Assistant
A Raspberry Pi-based study monitoring system with posture detection, eye tracking, break reminders, and session logging.
Inspiration
Students tend to get carried away and distracted easily while studying. This problem is common with all children and especially children with ADHD (Attention-Deficit/Hyperactivity Disorder). When they go unmonitored, children are prone to pretend to be studying or doing other activities. Many sleeps during their study session. To overcome the problem of children going unsupervised we have come up with the idea of "Study Assistant". The concept is to monitor the child during the study session and nurture them with the care that they require to be motivated and noticed.
In today’s world of constant distractions and easy access to entertainment, students struggle to stay focused during study sessions. Many experience:
- Sleepiness or dozing off
- Poor posture causing neck/back pain
- Lack of hydration or breaks
- No parental supervision or motivation

**Study Assistant** was built to tackle all of these issues, especially for students with ADHD or focus-related difficulties.

---

## Features

- 👁️ **Real-time Eye Tracking** to detect drowsiness
- 🧍 **Posture Detection** with alerts when slouching
- ⏱️ **Study Timer & Session Logging** in Excel
- 💧 **Hydration & Sedentary Break Reminders**
- 🔊 **Audio Alerts** with PyGame & pyttsx3
- 📺 Output via **20x4 LCD Display**
- 🧠 Built using **Python, OpenCV, dlib, MediaPipe, and Raspberry Pi**

---

## Technologies Used

| Component       | Usage                         |
|----------------|-------------------------------|
| `cv2` (OpenCV) | Face & eye detection          |
| `dlib`         | Facial landmark detection     |
| `pyttsx3`      | Text-to-speech alerting       |
| `pygame`       | Audio alarms/sounds           |
| `picamera2`    | Raspberry Pi camera handling  |
| `LCD 20x4`     | Real-time status display      |
| `Python`       | Core programming language     |


---

## 🎓 How It Works

1. **Camera** tracks the user's face and eyes in real time.
2. If **eyes are closed** for too long → voice & sound **alert**.
3. **Posture** is monitored using MediaPipe (future scope).
4. Study **duration** is recorded.
5. LCD screen shows current status (Active, Alert, Break Time).
6. Reminders are given for **water breaks** and **sedentary breaks**.
   
<img width="1161" height="712" alt="image" src="https://github.com/user-attachments/assets/2e4779de-c0f2-414d-b9aa-6fad4194e931" />

<img width="728" height="456" alt="image" src="https://github.com/user-attachments/assets/2ee6f1c3-c4df-4e10-9b7f-7664085f2194" />

<img width="800" height="738" alt="image" src="https://github.com/user-attachments/assets/742c318e-701e-459a-a639-6f1edbc32bbb" />



   

 Future Scope
	•	📱 Mobile/Web App for data visualization
	•	🗣️ AI Voice Assistant to interact with student
	•	📊 Visual analytics of daily study patterns
	•	🖥️ Bigger display or smart mirror integration

---

 References
	•	OpenCV Python Docs
	•	Raspberry Pi Camera Docs
	•	PyGame
	•	dlib Face Detection
