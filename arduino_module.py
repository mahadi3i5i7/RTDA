import serial
import time
import serial.tools.list_ports

#ser = serial.Serial('COM5', 115200)
#time.sleep(2)

def check_port():
    #available_ports = serial.tools.list_ports.comports()
    #if available_ports:
        print("Available serial ports:")
    #   for port in available_ports:
    #      print(port.device)
    #else:
    #    print("No serial ports")

def traffic_light_red():
    #ser.write('1'.encode())
    print("SERIAL SENT")
def traffic_light_green():
    #ser.write('2'.encode())
    print("SERIAL SENT")

def traffic_light_yellow():
    #ser.write('1'.encode())
    #ser.write('2'.encode())
    print("SERIAL SENT")

def center_led_blink():
    #ser.write('3'.encode())
    print("SERIAL SENT")

def left_middle_led_blink():
    #ser.write('4'.encode())
    print("SERIAL SENT")

def left_most_led_blink():
    #ser.write('5'.encode())
    print("SERIAL SENT")

def right_middle_led_blink():
    #ser.write('6'.encode())
    print("SERIAL SENT")

def right_most_led_blink():
    #ser.write('7'.encode())
    print("SERIAL SENT")


def automatic_braking():
    #ser.write('9'.encode())
    print("SERIAL SENT")


