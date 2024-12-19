import serial 
import time 
import struct

serial_rx_len = 3
ser = serial.Serial('COM20', 115200) 

def Serial_Rx():
    try:
        count = ser.inWaiting()  
        if count == serial_rx_len:
            recv = ser.read(count) 
            serial_rx = list(struct.unpack('!3B', recv))
            if serial_rx[0] == 255:  
                if serial_rx[2] == 254:  
                    ser.flushInput()
                    time.sleep(0.1)
                    serial_rx = serial_rx[1:-1]  
                    return serial_rx  
        ser.flushInput() 
        time.sleep(0.1) 
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    except Exception as e:
        print("Exception:", e)

def Serial_Tx(a, b, c, d):
    try:
        # serial_tx = [44] + tx + [91]
        # pack=struct.pack(tx)
        data = struct.pack("BHHHHB",#BFFFFFFB
                           0xFE,
                           int(a),
                           int(b),
                           int(c),
                           int(d),
                           0xFF,
                           )
        ser.write(data)
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    except Exception as e:
        print("Exception:", e)
