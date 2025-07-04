import serial
ser = serial.Serial('COM11', 9600) 
while True:
    line = ser.readline().decode('utf-8').strip()
    button_state = int(line)

    if button_state == 1:
        print("Button pressed")
    else:
        print("Button not pressed")
