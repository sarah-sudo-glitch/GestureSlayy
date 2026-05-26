import cv2
import pyautogui
import time
import math
import mediapipe as mp
import osascript



mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)


prev_x, prev_y = 0, 0
movement_ignore = 0.05

last_action = None
last_scrol = 0
sl_delay = 0.5

gesture = "NONE"
last_gesture = None


while True:
    success, frame = cap.read()

    if not success:
        break

    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    result = hands.process(rgb)

    direction = "STABLE"

    if result.multi_hand_landmarks:

        hand = result.multi_hand_landmarks[0]

        lm = hand.landmark

        curr_x = lm[9].x
        curr_y = lm[9].y

        cur_time = time.time()

        
        if prev_x != 0 and prev_y != 0:

            dx = curr_x - prev_x
            dy = curr_y - prev_y

            if abs(dx) > abs(dy):

                if dx > movement_ignore:
                    direction = "RIGHT"

                elif dx < -movement_ignore:
                    direction = "LEFT"

            else:

                if dy > movement_ignore:
                    direction = "DOWN"

                elif dy < -movement_ignore:
                    direction = "UP"

        if direction == "RIGHT" and last_action != "RIGHT":

            pyautogui.press("right")
            last_action = "RIGHT"

        elif direction == "LEFT" and last_action != "LEFT":

            pyautogui.press("left")
            last_action = "LEFT"


        if direction == "UP" and cur_time - last_scrol > sl_delay:

            pyautogui.scroll(300)
            last_scrol = cur_time

        elif direction == "DOWN" and cur_time - last_scrol > sl_delay:

            pyautogui.scroll(-300)
            last_scrol = cur_time


       
        x1, y1 = lm[4].x, lm[4].y
        x2, y2 = lm[8].x, lm[8].y

        distance = math.hypot(
            x2 - x1,
            y2 - y1
        )
        vol = int(distance * 100)

        if vol > 100:
           vol = 100

        if vol < 0:
          vol = 0

        osascript.osascript(
           f"set volume output volume {vol}"
        )


        
        fingers = []

        
        fingers.append(
            1 if lm[4].x > lm[3].x else 0
        )

       
        fingers.append(
            1 if lm[8].y < lm[6].y else 0
        )

        
        fingers.append(
            1 if lm[12].y < lm[10].y else 0
        )

       
        fingers.append(
            1 if lm[16].y < lm[14].y else 0
        )

      
        fingers.append(
            1 if lm[20].y < lm[18].y else 0
        )

        count = sum(fingers)


        
        if count == 5 and last_gesture != "PAUSE":

            gesture = "PAUSE"
            pyautogui.press("space")
            last_gesture = "PAUSE"

        elif count == 0 and last_gesture != "PLAY":

            gesture = "PLAY"
            pyautogui.press("space")
            last_gesture = "PLAY"

        elif count != 0 and count != 5:

            last_gesture = None


        if direction == "STABLE":
            last_action = None

        prev_x, prev_y = curr_x, curr_y

        mp_draw.draw_landmarks(
            frame,
            hand,
            mp_hands.HAND_CONNECTIONS
        )


    cv2.putText(
        frame,
        direction,
        (40,60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0,255,0),
        3
    )

    cv2.putText(
        frame,
        gesture,
        (40,110),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255,0,0),
        3
    )

    cv2.imshow(
        "GestureSlayy",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()