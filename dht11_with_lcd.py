import dht11
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
instance = dht11.DHT11(4)
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574', 0x27)
while 1:
    result = instance.read()
    error = result.error_code
    temp = result.temperature
    humi = result.humidity
    if error == 0:
        lcd.cursor_pos = (0, 0)
        lcd.write_string("Temp: %s" %result.temperature)
        lcd.cursor_pos = (0, 8)
        lcd.write_string('C')
        lcd.cursor_pos = (1, 0)
        lcd.write_string("Humi: %s" %result.humidity)
        lcd.cursor_pos = (1, 8)
        lcd.write_string('%RH')
        time.sleep(1)
    else:
        lcd.cursor_pos = (0,0)
        lcd.write_string(u'  Please Wait!  ')
        lcd.cursor_pos = (1,0)
        lcd.write_string(u'  data missing  ')
        time.sleep(1)
        lcd.clear()
