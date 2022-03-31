import serial

ser = serial.Serial('COM2',19200)
print(ser.name)
ser.write(b'mogo 1:45 2:45')
ser.close()
