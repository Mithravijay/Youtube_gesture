import cv2
import mediapipe as mp
import pyautogui
import webbrowser
import time

# Step 1: Open YouTube
webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # You can change this link
time.sleep(5)  # Wait for the browser to load

# Step 2: Set up MediaPipe and OpenCV
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.75)
mp_draw = mp.solutions.drawing_utils

tip_ids = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky

cap = cv2.VideoCapture(0)
last_action_time = 0

# Helper to detect which fingers are up
def fingers_up(hand_landmarks):
    fingers = []

    # Thumb
    if hand_landmarks.landmark[tip_ids[0]].x < hand_landmarks.landmark[tip_ids[0]-1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    for id in range(1, 5):
        if hand_landmarks.landmark[tip_ids[id]].y < hand_landmarks.landmark[tip_ids[id]-2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

# Step 3: Main loop
while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingers = fingers_up(hand_landmarks)

            current_time = time.time()
            if current_time - last_action_time > 1:  # Cooldown

                if fingers == [0, 1, 0, 0, 0]:
                    pyautogui.press('space')
                    print("Play/Pause")
                    last_action_time = current_time

                elif fingers == [0, 1, 1, 0, 0]:
                    pyautogui.press('right')
                    print("Forward")
                    last_action_time = current_time

                elif fingers == [1, 1, 1, 1, 1]:
                    pyautogui.press('volumeup')
                    print("Volume Up")
                    last_action_time = current_time

                elif fingers == [0, 0, 0, 0, 0]:
                    pyautogui.press('volumedown')
                    print("Volume Down")
                    last_action_time = current_time

    cv2.imshow("Gesture-Controlled YouTube", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
