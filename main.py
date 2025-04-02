import cv2
import time
from cvzone.HandTrackingModule import HandDetector
from directkeys import PressKey, ReleaseKey, right_pressed, left_pressed

# Initialize detector
detector = HandDetector(detectionCon=0.8, maxHands=1)
cap = cv2.VideoCapture(0)

# Game control variables
current_key = None
last_key_time = 0
debounce_delay = 0.2  # 200ms delay between key changes

# Game window focus reminder
cv2.namedWindow("Hill Climbing Controller")
cv2.putText(cv2.imread('blank.png', 1), "Make sure game window is focused!", (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

while True:
    success, img = cap.read()
    if not success:
        continue

    img = cv2.flip(img, 1)  # Mirror image
    hands, img = detector.findHands(img, draw=True)

    # Create visual feedback areas
    cv2.rectangle(img, (50, 400), (300, 480), (50, 50, 255), cv2.FILLED)
    cv2.rectangle(img, (350, 400), (600, 480), (50, 50, 255), cv2.FILLED)

    current_time = time.time()

    if hands:
        fingers = detector.fingersUp(hands[0])

        # GAS (open hand)
        if sum(fingers) == 5:  # All fingers open
            cv2.putText(img, "GAS", (150, 450), cv2.FONT_HERSHEY_SIMPLEX,
                        1.5, (255, 255, 255), 3)
            if current_key != right_pressed:
                if current_key:
                    ReleaseKey(current_key)
                PressKey(right_pressed)
                current_key = right_pressed
                print("GAS pressed")  # Debug output

        # BRAKE (closed fist)
        elif sum(fingers) == 0:  # No fingers open
            cv2.putText(img, "BRAKE", (450, 450), cv2.FONT_HERSHEY_SIMPLEX,
                        1.5, (255, 255, 255), 3)
            if current_key != left_pressed:
                if current_key:
                    ReleaseKey(current_key)
                PressKey(left_pressed)
                current_key = left_pressed
                print("BRAKE pressed")  # Debug output

        # NEUTRAL (other gestures)
        else:
            if current_key:
                ReleaseKey(current_key)
                current_key = None
                print("Key released")  # Debug output

    # No hands detected - release keys
    elif current_key:
        ReleaseKey(current_key)
        current_key = None
        print("Key released (no hands)")  # Debug output

    cv2.imshow("Hill Climbing Controller", img)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
if current_key:
    ReleaseKey(current_key)
cap.release()
cv2.destroyAllWindows()