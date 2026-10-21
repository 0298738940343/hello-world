from machine import Pin
import time

print("Hello, World!")
led = Pin(2, Pin.OUT)
while True:
    led.toggle()
    time.sleep(0.5)
