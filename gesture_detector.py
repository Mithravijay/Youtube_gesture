import cv2
import mediapipe as mp
import pyautogui
import time

class GestureController:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        self.mp_draw = mp.solutions.drawing_utils
        self.tip_ids = [4, 8, 12, 16, 20]
        self.last_action_time = 0

    def fingers_up(self, hand_landmarks):
        fingers = []
        if hand_landmarks.landmark[self.tip_ids[0]].x < hand_landmarks.landmark[self.tip_ids[0]-1].x:
            fingers.append(1)
        else:
            fingers.append(0)
        for id in range(1, 5):
            if hand_landmarks.landmark[self.tip_ids[id]].y < hand_landmarks.landmark[self.tip_ids[id] - 2].y:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers

    def run(self):
        import webbrowser
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        time.sleep(5)

        cap = cv2.VideoCapture(0)
        while True:
            success, img = cap.read()
            if not success:
                continue
            img = cv2.resize(img, (640, 480))
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            result = self.hands.process(img_rgb)

            if result.multi_hand_landmarks:
                for hand_landmarks in result.multi_hand_landmarks:
                    self.mp_draw.draw_landmarks(img, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                    fingers = self.fingers_up(hand_landmarks)
                    current_time = time.time()
                    if current_time - self.last_action_time > 1:
                        if fingers == [0, 1, 0, 0, 0]:
                            pyautogui.press('space')
                            print("Play/Pause")
                            self.last_action_time = current_time
                        elif fingers == [0, 1, 1, 0, 0]:
                            pyautogui.press('right')
                            print("Forward")
                            self.last_action_time = current_time
                        elif fingers == [1, 1, 1, 1, 1]:
                            pyautogui.press('volumeup')
                            print("Volume Up")
                            self.last_action_time = current_time
                        elif fingers == [0, 0, 0, 0, 0]:
                            pyautogui.press('volumedown')
                            print("Volume Down")
                            self.last_action_time = current_time

            cv2.imshow("Gesture Control", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
