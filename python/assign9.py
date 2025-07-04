import serial
import time
ser = serial.Serial('COM8', 9600)
while True:
  try:
   command = input("Press Enter to check LED status or 'q'to quit: ").strip().lower()
 
   if command == 'q':
    break
   ser.write(b'0') # Send '0' to request LED status
   time.sleep(0.1) # Allow time for Arduino to process
   response = ser.readline().decode().strip()
   if response == "LED ON":
    print("LED is ON")
   elif response == "LED OFF":
    print("LED is OFF")
   else:
    print("Invalid response from Arduino")
  except KeyboardInterrupt:
    break
ser.close()