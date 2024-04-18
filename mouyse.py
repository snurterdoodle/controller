import serial
import pyautogui

ser = serial.Serial('COM5', 9600)  # Change 'COM5' to the port your Arduino is connected to

# Define dead zone thresholds
DEAD_ZONE_X = 512
DEAD_ZONE_Y = 512
DEAD_ZONE_THRESHOLD = 400

# Screen dimensions (adjust according to your screen resolution)
screenWidth, screenHeight = 1920, 1080

# Adjust this scaling factor to control the sensitivity of the mouse movement
scaling_factor = 0.03

while True:
    data = ser.readline().decode().strip().split(',')
    if len(data) == 6:  # Check if data contains X, Y, left-click, right-click, space 2, and space 4 button states
        x = int(data[0])
        y = int(data[1])
        left_click = int(data[2])
        right_click = int(data[3])
        space2 = int(data[4])
        space4 = int(data[5])

        # Apply dead zone
        if abs(x - DEAD_ZONE_X) > DEAD_ZONE_THRESHOLD or abs(y - DEAD_ZONE_Y) > DEAD_ZONE_THRESHOLD:
            # Calculate the amount of movement based on joystick position with scaling factor
            moveX = (x - DEAD_ZONE_X) * screenWidth / 1023 * scaling_factor
            moveY = (y - DEAD_ZONE_Y) * screenHeight / 1023 * scaling_factor

            # Move the mouse relative to its current position
            pyautogui.moveRel(moveX, -moveY)  # Invert vertical movement

        # Check button states and simulate mouse clicks and keyboard presses
        if left_click == 0:
            pyautogui.click(button='left')
        if right_click == 0:
            pyautogui.click(button='right')
        if space2 == 0:
            # Simulate pressing the Ctrl key
            pyautogui.keyDown('ctrl')
        else:
            # Release the Ctrl key
            pyautogui.keyUp('ctrl')
        if space4 == 0:
            # Simulate pressing the Space key
            pyautogui.press('space')
