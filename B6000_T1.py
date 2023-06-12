import time
from ppadb.client import Client as AdbClient
import os

#Settings
cap_folder = 'capture'
sn_lara = '3c218347' # Laras Handy
sn_nico = '42001537e4305400' # Nicos Handy
sn_gerd = '3a5a2bf9' # Gerds Handy
sn = sn_nico

def connect():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037
    devices = client.devices()
    if len(devices) == 0:
        print('No devices')
        quit()

    for i in range(len(devices)):
         if devices[i].serial == sn:
              device = devices[0]
              print(f'Connected to {device}')
              return device, client
         print(f'Device {sn} not found ')
         quit()

def capture_screen(device, count):
     device.shell('screencap -p /sdcard/screencap.png')
     device.pull('/sdcard/screencap.png', cap_folder + '/' + f'bild{count}.png')

def button_lock(device):
     device.shell('input touchscreen tap 800 1040') # 1

def button_unlock(device):
     device.shell('input touchscreen tap 275 1040') # 1


def button_open(device):
     print("open")
     device.shell('input touchscreen tap 280 840')# 1
     #device.shell('input touchscreen tap 280 1040') # 1


def swipe_left(device):
     device.shell('input swipe 800 480 100 480') # 1    

def swipe_right(device):
     device.shell('input swipe 100 480 800 480') # 1   

# ----------------------------------------------------------    
# Anfang Main Routine
# ---------------------------------------------------------
print('Testprogramm Start')
os.system('~/adb-dev/5.1.1/system/core/adb/adb kill-server')
os.system('~/adb-dev/5.1.1/system/core/adb/adb start-server')

device, client = connect()
count = 0
    
while(1):
       count = count + 1
       print(time.strftime("%H:%M:%S", time.localtime()) + f' count = {count}')
       button_open(device)
       with open('output.txt', 'a') as f:
             f.write(time.strftime("%H:%M:%S", time.localtime()) + f' count = {count}' +'\r\n')

       #button_Test(device)
       #swipe_left(device)
       #swipe_right(device)
       time.sleep(15)
       #capture_screen(device,count)
       
      

   
