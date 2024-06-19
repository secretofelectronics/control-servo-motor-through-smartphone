from machine import Pin, PWM, UART
from time import sleep


# Define UART pins
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

pwm = PWM(Pin(14))
pwm.freq(50)


while True:
    if uart.any():
        data = uart.readline()
        if data== b'f':
            for position in range(1000,9000,50):
                pwm.duty_u16(position)
                sleep(0.01)
        elif data== b'b':
            for position in range(9000,1000,-50):
                pwm.duty_u16(position)
                sleep(0.01)