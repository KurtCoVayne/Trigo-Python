import network
import machine
import urequests
import time
def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('Alejandro', 'ledis123')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
def blink(seconds):
    led = machine.Pin(2,machine.Pin.OUT)
    for _ in range(seconds):
        led.value(not led.value())
        time.sleep(0.5)
        led.value(not led.value())
        time.sleep(0.5)

def request():
    response = urequests.get('https://educacion-financiera.herokuapp.com/control/operations')
    res = response.json()
    print(res)
    if(res['right_lights']):
        blink(5)
def move(direction=None):
    l1 = machine.Pin(15,machine.Pin.OUT)
    l2 = machine.Pin(13,machine.Pin.OUT)
    r1 = machine.Pin(2,machine.Pin.OUT)
    r2 = machine.Pin(0,machine.Pin.OUT)

    rMotor = machine.Pin(4,machine.Pin.OUT)
    lMotor = machine.Pin(14,machine.Pin.OUT)
    
    rMotor.value(1)
    lMotor.value(1)
    if(direction == "forward"):
        l2.value(0)
        r2.value(0)
        l1.value(1)
        r1.value(1)
    elif(direction == "backward"):
        l2.value(1)
        r2.value(1)
        l1.value(0)
        r1.value(0)
    elif(direction =="left"):
        l2.value(0)
        r2.value(0)
        l1.value(1)
        r1.value(0)
    elif(direction =="right"):
        l2.value(0)
        r2.value(0)
        l1.value(0)
        r1.value(1)
    else:
        l2.value(0)
        r2.value(0)
        l1.value(0)
        r1.value(0)