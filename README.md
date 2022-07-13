# Raspberry-Pi-Pico-W-Telegram-Bot
Raspberry Pi Pico W basic onboard LED and temperature sensor Telegram Bot

Kablosuz bağlantı imkanı sunan Raspberry Pi Pico W'nun dahili LED'i ve sıcaklık sensörünün Telegram Bot ile kontrol edilmesini sağlayan basit bir program.
![pico](https://user-images.githubusercontent.com/62475996/178732305-c20e8080-6a2e-4a8f-bee0-962d29fee346.jpg)


gabrielebarola'nın geliştirdiği Telegram kütüphanesini ESP mikrokontrolcüler için basitleştiren  "utelegram.py" eklentisini kullandım.
https://github.com/gabrielebarola/telegram-upy


Pico W'da dahili LED önceki nesil Pico'lar gibi (GPIO25) bir pine bağlanmayıp, üzerindeki WIFI çipine (WL_GPIO0) taşınmış. 
Pico'larda dahili sıcaklık sensörü sanal ADC4 pinine bağlı. 
