import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
import time

# =========================
# SETTINGS
# =========================

MODE_SUBWAY = 1
MODE_HILL = 2

game_mode = MODE_SUBWAY

cooldown = 0.7
last_action = time.time()

prev_x = 0
prev_y = 0

# =========================
# CAMERA
# =========================

cap = cv2.VideoCapture(0)

# =========================
# SKIN COLOR RANGE
# =========================

lower_skin = np.array([0,20,70])
upper_skin = np.array([20,255,255])

# =========================
# AUTO FOCUS GAME WINDOW
# =========================

def focus_game():

    windows = gw.getAllTitles()

    for w in windows:

        if "Subway" in w or "Hill" in w:

            try:
                game = gw.getWindowsWithTitle(w)[0]
                game.activate()
                print("Focused window:", w)
                time.sleep(1)
                return
            except:
                pass

    print("Game window not found")

# Focus once at start
focus_game()

# =========================
# FPS
# =========================

pTime = 0

# =========================
# MAIN LOOP
# =========================

while True:

    ret, frame = cap.read()

    frame = cv2.flip(frame,1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    mask = cv2.GaussianBlur(mask,(5,5),0)

    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:

        c = max(contours,key=cv2.contourArea)

        area = cv2.contourArea(c)

        if area > 5000:

            x,y,w,h = cv2.boundingRect(c)

            cx = x + w//2
            cy = y + h//2

            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

            cv2.circle(frame,(cx,cy),5,(255,0,0),-1)

            now = time.time()

            if now - last_action > cooldown:

                dx = cx - prev_x
                dy = cy - prev_y

                # =================
                # SUBWAY MODE
                # =================

                if game_mode == MODE_SUBWAY:

                    if abs(dx) > abs(dy):

                        if dx > 40:
                            pyautogui.press("right")
                            print("RIGHT")

                        elif dx < -40:
                            pyautogui.press("left")
                            print("LEFT")

                    else:

                        if dy < -40:
                            pyautogui.press("up")
                            print("JUMP")

                        elif dy > 40:
                            pyautogui.press("down")
                            print("SLIDE")

                # =================
                # HILL MODE
                # =================

                elif game_mode == MODE_HILL:

                    if dx > 40:
                        pyautogui.keyDown("right")
                        pyautogui.keyUp("left")
                        print("ACCELERATE")

                    elif dx < -40:
                        pyautogui.keyDown("left")
                        pyautogui.keyUp("right")
                        print("BRAKE")

                last_action = now

            prev_x = cx
            prev_y = cy

    # =========================
    # FPS DISPLAY
    # =========================

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(frame,f"FPS: {int(fps)}",(1050,40),
                cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)

    # =========================
    # UI TEXT
    # =========================

    if game_mode == MODE_SUBWAY:
        mode = "Mode: Subway Surfers"
    else:
        mode = "Mode: Hill Climb Racing"

    cv2.putText(frame,mode,(20,40),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.putText(frame,"Press 1 = Subway",(20,80),
                cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)

    cv2.putText(frame,"Press 2 = Hill Climb",(20,110),
                cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)

    cv2.imshow("AI Gesture Game Controller",frame)
    cv2.imshow("Mask",mask)

    key = cv2.waitKey(1)

    if key == ord('1'):
        game_mode = MODE_SUBWAY

    if key == ord('2'):
        game_mode = MODE_HILL

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()