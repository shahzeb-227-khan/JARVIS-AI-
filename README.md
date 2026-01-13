# **Jarvis AI Assistant**

## **Description**

Jarvis AI Assistant is a **voice-controlled personal assistant** built in Python. It can perform a variety of tasks, such as searching Wikipedia, opening websites, checking the time, launching applications, and playing music from your local playlist. The assistant uses **speech recognition** to understand commands and **text-to-speech** to respond, making interactions natural and hands-free.

It’s perfect for automating daily computer tasks or serving as a virtual companion for productivity.

---

## **Features**

* Voice-based interaction using your microphone.
* Greet the user based on the current time (morning, afternoon, evening).
* Search and summarize topics using **Wikipedia**.
* Perform **Google** and **YouTube** searches.
* Open popular websites like YouTube, Google, LinkedIn, LeetCode, and Stack Overflow.
* Launch applications like **Visual Studio Code** and **Microsoft Word**.
* Play music randomly from a local folder.
* Tell the current time.
* Stop the assistant with a voice command (`stop`).

---

## **Installation**

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/jarvis-ai-assistant.git
cd jarvis-ai-assistant
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies:**

```bash
pip install pyttsx3 speechrecognition wikipedia
```

4. **Optional dependencies for web browsing:**

```bash
pip install pyaudio
```

> **Note:** On Windows, you may need to install **PyAudio** via `.whl` file if `pip install pyaudio` fails.

---

## **Usage**

1. Open the Python file:

```bash
python jarvis_ai.py
```

2. Jarvis will greet you based on the time of day and prompt you for commands.

3. Speak commands like:

* `"Wikipedia Albert Einstein"` → Get a summary from Wikipedia.
* `"Search on Google Python tutorials"` → Open Google with the query.
* `"Search on YouTube lo-fi music"` → Open YouTube with the query.
* `"Open YouTube"` / `"Open Google"` / `"Open LinkedIn"`.
* `"Play music"` → Plays a random song from your music folder.
* `"The time"` → Jarvis tells the current time.
* `"Open code"` → Opens Visual Studio Code.
* `"Stop"` → Ends the assistant.

---

## **Configuration**

Before running, update paths in the script to match your system:

* **Music folder:**

```python
music_dir = "C:\\Users\\YourName\\Music"
```

* **Visual Studio Code path:**

```python
visualcode = "C:\\Path\\To\\VSCode\\Code.exe"
```

* **Microsoft Word path:**

```python
word = "C:\\Path\\To\\Word\\WINWORD.EXE"
```

---

## **Dependencies**

* Python 3.8+
* [pyttsx3](https://pypi.org/project/pyttsx3/) – Text-to-speech engine
* [speechrecognition](https://pypi.org/project/SpeechRecognition/) – For recognizing voice commands
* [wikipedia](https://pypi.org/project/wikipedia/) – Wikipedia API access
* webbrowser (built-in)
* os (built-in)
* datetime (built-in)
* random (built-in)

Optional:

* [PyAudio](https://pypi.org/project/PyAudio/) – For microphone input

---

## **Future Improvements**

* Add **AI-powered responses** using GPT or Gemini API.
* Add GUI for a more interactive experience.
* Integrate with calendar and reminders.
* Enable multi-language support.
* Allow controlling other software like Spotify or browser tabs.

---

## **License**

This project is licensed under the **MIT License**.

---

If you want, I can also **create a super polished GitHub-ready version** of this README with **badges, screenshots, and example usage**, so it looks professional on your repository.

Do you want me to do that?
