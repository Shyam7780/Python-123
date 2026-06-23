"""
╔══════════════════════════════════════════════════════════╗
║         LAPTOP VOICE CONTROLLER - Windows               ║
║  Controls: Apps, Volume, Brightness, Mouse, System      ║
╚══════════════════════════════════════════════════════════╝

INSTALL DEPENDENCIES FIRST (run in terminal):
    pip install SpeechRecognition pyaudio pyttsx3 pyautogui psutil screen-brightness-control pycaw comtypes

USAGE:
    python voice_control.py
    Then say "wake up" to activate, "sleep" to deactivate.
"""

import speech_recognition as sr
import pyttsx3
import pyautogui
import subprocess
import os
import sys
import time
import threading
import psutil

# ── Optional imports with graceful fallback ──────────────────────────
try:
    import screen_brightness_control as sbc
    BRIGHTNESS_AVAILABLE = True
except ImportError:
    BRIGHTNESS_AVAILABLE = False
    print("[WARNING] screen-brightness-control not installed. Brightness commands disabled.")

try:
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    VOLUME_CTRL = cast(interface, POINTER(IAudioEndpointVolume))
    VOLUME_AVAILABLE = True
except Exception:
    VOLUME_AVAILABLE = False
    print("[WARNING] pycaw not installed. Using keyboard for volume control.")

pyautogui.FAILSAFE = True  # Move mouse to top-left corner to emergency stop

# ── Text-to-Speech Engine ────────────────────────────────────────────
engine = pyttsx3.init()
engine.setProperty('rate', 165)
engine.setProperty('volume', 0.9)

def speak(text):
    """Speak text aloud and print it."""
    print(f"🤖 Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# ── Speech Recognition ───────────────────────────────────────────────
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8

def listen(timeout=5, phrase_limit=6):
    """Listen for one voice command and return text."""
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_limit)
            text = recognizer.recognize_google(audio).lower().strip()
            print(f"👤 You said: '{text}'")
            return text
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            speak("Internet connection issue. Please check your connection.")
            return ""

# ── Volume Control ───────────────────────────────────────────────────
def set_volume(level):
    """Set volume 0–100."""
    if VOLUME_AVAILABLE:
        vol = max(0.0, min(1.0, level / 100.0))
        VOLUME_CTRL.SetMasterVolumeLevelScalar(vol, None)
    else:
        # Fallback: use keyboard media keys
        pyautogui.hotkey('volumemute') if level == 0 else None
    speak(f"Volume set to {level} percent")

def get_volume():
    if VOLUME_AVAILABLE:
        return int(VOLUME_CTRL.GetMasterVolumeLevelScalar() * 100)
    return -1

def volume_up(amount=10):
    if VOLUME_AVAILABLE:
        current = get_volume()
        set_volume(min(100, current + amount))
    else:
        for _ in range(amount // 2):
            pyautogui.press('volumeup')
        speak("Volume increased")

def volume_down(amount=10):
    if VOLUME_AVAILABLE:
        current = get_volume()
        set_volume(max(0, current - amount))
    else:
        for _ in range(amount // 2):
            pyautogui.press('volumedown')
        speak("Volume decreased")

def mute():
    if VOLUME_AVAILABLE:
        current_mute = VOLUME_CTRL.GetMute()
        VOLUME_CTRL.SetMute(not current_mute, None)
        speak("Muted" if not current_mute else "Unmuted")
    else:
        pyautogui.press('volumemute')
        speak("Toggled mute")

# ── Brightness Control ───────────────────────────────────────────────
def set_brightness(level):
    if BRIGHTNESS_AVAILABLE:
        try:
            sbc.set_brightness(level)
            speak(f"Brightness set to {level} percent")
        except Exception as e:
            speak("Could not change brightness on this display")
    else:
        speak("Brightness control is not available. Please install screen-brightness-control.")

def brightness_up():
    if BRIGHTNESS_AVAILABLE:
        try:
            current = sbc.get_brightness()[0]
            set_brightness(min(100, current + 10))
        except:
            speak("Brightness control failed")
    else:
        speak("Brightness control not available")

def brightness_down():
    if BRIGHTNESS_AVAILABLE:
        try:
            current = sbc.get_brightness()[0]
            set_brightness(max(10, current - 10))
        except:
            speak("Brightness control failed")
    else:
        speak("Brightness control not available")

# ── App Control ──────────────────────────────────────────────────────
APP_MAP = {
    # Browser
    "chrome":       "chrome",
    "google chrome":"chrome",
    "browser":      "chrome",
    "firefox":      "firefox",
    "edge":         "msedge",

    # Office & Productivity
    "notepad":      "notepad",
    "word":         "winword",
    "excel":        "excel",
    "powerpoint":   "powerpnt",
    "calculator":   "calc",
    "paint":        "mspaint",

    # System
    "task manager": "taskmgr",
    "file explorer":"explorer",
    "explorer":     "explorer",
    "control panel":"control",
    "settings":     "ms-settings:",
    "command prompt":"cmd",
    "terminal":     "wt",          # Windows Terminal

    # Media
    "vlc":          "vlc",
    "spotify":      "spotify",
    "youtube":      "https://youtube.com",
    "whatsapp":     "https://web.whatsapp.com",
    "gmail":        "https://gmail.com",
    "google":       "https://google.com",
}

def open_app(app_name):
    app_name = app_name.lower().strip()
    # Find match in APP_MAP
    target = None
    for key, val in APP_MAP.items():
        if key in app_name or app_name in key:
            target = val
            break

    if target is None:
        # Try opening directly as a program name
        target = app_name

    try:
        if target.startswith("http"):
            os.startfile(target)
            speak(f"Opening {app_name}")
        elif target == "ms-settings:":
            subprocess.Popen(["start", "ms-settings:"], shell=True)
            speak("Opening settings")
        else:
            subprocess.Popen(target, shell=True)
            speak(f"Opening {app_name}")
    except Exception as e:
        speak(f"Could not open {app_name}")
        print(f"Error: {e}")

def close_app(app_name):
    """Close app by process name."""
    PROCESS_MAP = {
        "chrome": "chrome.exe",
        "google chrome": "chrome.exe",
        "firefox": "firefox.exe",
        "edge": "msedge.exe",
        "notepad": "notepad.exe",
        "vlc": "vlc.exe",
        "spotify": "Spotify.exe",
        "word": "WINWORD.EXE",
        "excel": "EXCEL.EXE",
        "calculator": "Calculator.exe",
    }
    process_name = None
    for key, val in PROCESS_MAP.items():
        if key in app_name.lower():
            process_name = val
            break

    if process_name:
        try:
            subprocess.call(["taskkill", "/F", "/IM", process_name], 
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            speak(f"Closed {app_name}")
        except:
            speak(f"Could not close {app_name}")
    else:
        speak(f"I don't know how to close {app_name}")

# ── Mouse Control ────────────────────────────────────────────────────
MOUSE_STEP = 100  # pixels per move command

def move_mouse(direction, amount=MOUSE_STEP):
    x, y = pyautogui.position()
    if direction == "up":
        pyautogui.moveTo(x, max(0, y - amount), duration=0.2)
    elif direction == "down":
        pyautogui.moveTo(x, y + amount, duration=0.2)
    elif direction == "left":
        pyautogui.moveTo(max(0, x - amount), y, duration=0.2)
    elif direction == "right":
        pyautogui.moveTo(x + amount, y, duration=0.2)

def click(button="left"):
    if button == "right":
        pyautogui.rightClick()
    elif button == "double":
        pyautogui.doubleClick()
    else:
        pyautogui.click()

def scroll(direction, amount=3):
    if direction == "up":
        pyautogui.scroll(amount)
    else:
        pyautogui.scroll(-amount)

# ── Keyboard Shortcuts ───────────────────────────────────────────────
def take_screenshot():
    path = os.path.join(os.path.expanduser("~"), "Desktop", 
                        f"screenshot_{int(time.time())}.png")
    pyautogui.screenshot(path)
    speak(f"Screenshot saved to Desktop")

def keyboard_shortcut(keys):
    pyautogui.hotkey(*keys)

# ── System Commands ──────────────────────────────────────────────────
def system_info():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    ram_used = ram.used // (1024**3)
    ram_total = ram.total // (1024**3)
    battery = psutil.sensors_battery()
    bat_str = f"Battery is at {int(battery.percent)} percent." if battery else ""
    speak(f"CPU usage is {cpu} percent. RAM: {ram_used} of {ram_total} gigabytes used. {bat_str}")

def shutdown_computer():
    speak("Shutting down in 5 seconds. Say cancel to stop.")
    time.sleep(2)
    # Listen for cancel
    response = listen(timeout=4)
    if "cancel" in response or "stop" in response:
        speak("Shutdown cancelled.")
    else:
        speak("Shutting down now. Goodbye!")
        os.system("shutdown /s /t 3")

def restart_computer():
    speak("Restarting in 5 seconds. Say cancel to stop.")
    time.sleep(2)
    response = listen(timeout=4)
    if "cancel" in response or "stop" in response:
        speak("Restart cancelled.")
    else:
        speak("Restarting now!")
        os.system("shutdown /r /t 3")

def sleep_computer():
    speak("Putting computer to sleep.")
    time.sleep(1)
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def lock_computer():
    speak("Locking the computer.")
    os.system("rundll32.exe user32.dll,LockWorkStation")

# ── Command Parser ───────────────────────────────────────────────────
def parse_command(command):
    """Parse voice command and execute the right action."""

    # ── VOLUME ──────────────────────────────────────
    if any(w in command for w in ["volume up", "increase volume", "louder", "turn up"]):
        amount = 20 if "lot" in command else 10
        volume_up(amount)

    elif any(w in command for w in ["volume down", "decrease volume", "quieter", "turn down", "lower volume"]):
        amount = 20 if "lot" in command else 10
        volume_down(amount)

    elif any(w in command for w in ["mute", "silence", "quiet"]):
        mute()

    elif "set volume" in command:
        # Extract number: "set volume to 50"
        words = command.split()
        for w in words:
            if w.isdigit():
                set_volume(int(w))
                break

    # ── BRIGHTNESS ──────────────────────────────────
    elif any(w in command for w in ["brightness up", "increase brightness", "brighter"]):
        brightness_up()

    elif any(w in command for w in ["brightness down", "decrease brightness", "darker", "dim"]):
        brightness_down()

    elif "set brightness" in command:
        words = command.split()
        for w in words:
            if w.isdigit():
                set_brightness(int(w))
                break

    # ── OPEN APP ─────────────────────────────────────
    elif command.startswith("open "):
        app = command.replace("open ", "").strip()
        open_app(app)

    elif command.startswith("launch "):
        app = command.replace("launch ", "").strip()
        open_app(app)

    # ── CLOSE APP ────────────────────────────────────
    elif command.startswith("close "):
        app = command.replace("close ", "").strip()
        close_app(app)

    # ── MOUSE ────────────────────────────────────────
    elif "move mouse up" in command or "mouse up" in command:
        move_mouse("up")

    elif "move mouse down" in command or "mouse down" in command:
        move_mouse("down")

    elif "move mouse left" in command or "mouse left" in command:
        move_mouse("left")

    elif "move mouse right" in command or "mouse right" in command:
        move_mouse("right")

    elif "right click" in command:
        click("right")
        speak("Right clicked")

    elif "double click" in command:
        click("double")
        speak("Double clicked")

    elif "click" in command:
        click("left")
        speak("Clicked")

    elif "scroll up" in command:
        scroll("up")

    elif "scroll down" in command:
        scroll("down")

    # ── KEYBOARD SHORTCUTS ───────────────────────────
    elif "screenshot" in command or "take screenshot" in command:
        take_screenshot()

    elif "copy" in command:
        keyboard_shortcut(['ctrl', 'c'])
        speak("Copied")

    elif "paste" in command:
        keyboard_shortcut(['ctrl', 'v'])
        speak("Pasted")

    elif "undo" in command:
        keyboard_shortcut(['ctrl', 'z'])
        speak("Undone")

    elif "select all" in command:
        keyboard_shortcut(['ctrl', 'a'])
        speak("Selected all")

    elif "new tab" in command:
        keyboard_shortcut(['ctrl', 't'])
        speak("New tab opened")

    elif "close tab" in command:
        keyboard_shortcut(['ctrl', 'w'])
        speak("Tab closed")

    elif "switch window" in command or "alt tab" in command:
        keyboard_shortcut(['alt', 'tab'])

    elif "minimize" in command:
        keyboard_shortcut(['win', 'd'])
        speak("Minimized all windows")

    elif "maximize" in command:
        keyboard_shortcut(['win', 'up'])
        speak("Maximized window")

    elif "go back" in command:
        keyboard_shortcut(['alt', 'left'])
        speak("Going back")

    elif "refresh" in command:
        keyboard_shortcut(['ctrl', 'r'])
        speak("Refreshed")

    elif "zoom in" in command:
        keyboard_shortcut(['ctrl', '='])
        speak("Zoomed in")

    elif "zoom out" in command:
        keyboard_shortcut(['ctrl', '-'])
        speak("Zoomed out")

    # ── SEARCH ───────────────────────────────────────
    elif command.startswith("search for ") or command.startswith("search "):
        query = command.replace("search for ", "").replace("search ", "").strip()
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        os.startfile(url)
        speak(f"Searching for {query}")

    elif command.startswith("youtube ") or "play on youtube" in command:
        query = command.replace("youtube ", "").replace("play on youtube", "").strip()
        url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        os.startfile(url)
        speak(f"Searching YouTube for {query}")

    # ── SYSTEM ───────────────────────────────────────
    elif any(w in command for w in ["system info", "system status", "how is my computer", "battery"]):
        system_info()

    elif "shutdown" in command or "shut down" in command:
        shutdown_computer()

    elif "restart" in command or "reboot" in command:
        restart_computer()

    elif "sleep" in command and "computer" in command:
        sleep_computer()

    elif "lock" in command and ("computer" in command or "screen" in command):
        lock_computer()

    # ── HELP ─────────────────────────────────────────
    elif "help" in command or "what can you do" in command or "commands" in command:
        speak("""Here are some things I can do:
            Open or close apps like Chrome, Notepad, Spotify.
            Control volume: say volume up, volume down, or mute.
            Control brightness: say brighter or darker.
            Mouse control: say move mouse up, click, right click, scroll down.
            Keyboard: copy, paste, undo, screenshot, new tab.
            Search: say search for something, or YouTube music.
            System: shutdown, restart, lock, sleep computer, system info.""")

    # ── NOT UNDERSTOOD ───────────────────────────────
    else:
        speak(f"Sorry, I didn't understand: {command}. Say help to hear what I can do.")

# ── Main Loop ────────────────────────────────────────────────────────
def main():
    print("=" * 55)
    print("  🎙️  LAPTOP VOICE CONTROLLER")
    print("  Say 'wake up' to activate | 'exit' to quit")
    print("=" * 55)

    speak("Voice controller started. Say wake up to begin.")

    active = False  # Sleeping by default to save resources

    while True:
        try:
            command = listen(timeout=5 if active else 8)

            if not command:
                continue

            # ── Wake word ──
            if not active:
                if any(w in command for w in ["wake up", "hey laptop", "hello laptop", "start listening"]):
                    active = True
                    speak("I'm awake! How can I help you?")
                continue

            # ── Sleep word ──
            if any(w in command for w in ["sleep", "go to sleep", "stop listening", "goodbye"]):
                active = False
                speak("Going to sleep. Say wake up when you need me.")
                continue

            # ── Exit completely ──
            if any(w in command for w in ["exit", "quit", "terminate", "shut yourself"]):
                speak("Goodbye! Voice controller stopped.")
                sys.exit(0)

            # ── Parse and execute ──
            parse_command(command)

        except KeyboardInterrupt:
            speak("Voice controller stopped. Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"[ERROR] {e}")
            time.sleep(0.5)
            continue

if __name__ == "__main__":
    main()