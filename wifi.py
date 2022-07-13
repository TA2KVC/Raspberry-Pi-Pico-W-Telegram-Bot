import network
from sifre import ssid, password

def wactive():
 wlan = network.WLAN(network.STA_IF)
 wlan.active(True)
 wlan.connect(ssid, password)

 print("Bağlanıyor...")
 while wlan.isconnected() == False:
     pass

 print("Bağlandı!")
 print(wlan.ifconfig())
 