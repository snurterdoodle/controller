import serial
import keyboard

ser = serial.Serial('COM3', 9600)  # Change 'COM3' to the port your Arduino is connected to

# Define dead zone thresholds
DEAD_ZONE_X = 508
DEAD_ZONE_Y = 514
DEAD_ZONE_THRESHOLD = 300

while True:
    data = ser.readline().decode().strip().split(',')
    if len(data) == 2:  # Check if data contains X and Y values
        x = int(data[0])
        y = int(data[1])

        # Apply dead zone
        if abs(x - DEAD_ZONE_X) > DEAD_ZONE_THRESHOLD or abs(y - DEAD_ZONE_Y) > DEAD_ZONE_THRESHOLD:
            # Determine direction based on joystick movement
            if x < DEAD_ZONE_X - DEAD_ZONE_THRESHOLD:  # Move left
                keyboard.press('s')
            elif x > DEAD_ZONE_X + DEAD_ZONE_THRESHOLD:  # Move right
                keyboard.press('w')
            else:
                keyboard.release('s')
                keyboard.release('w')

            if y < DEAD_ZONE_Y - DEAD_ZONE_THRESHOLD:  # Move up
                keyboard.press('a')
            elif y > DEAD_ZONE_Y + DEAD_ZONE_THRESHOLD:  # Move down
                keyboard.press('d')
            else:
                keyboard.release('a')
                keyboard.release('d')
        else:
            # Release all keys when joystick is in dead zone
            keyboard.release('a')
            keyboard.release('d')
            keyboard.release('w')
            keyboard.release('s')
