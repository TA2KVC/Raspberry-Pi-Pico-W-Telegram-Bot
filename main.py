import wifi
import machine
from utelegram import Bot

wifi.wactive()

TOKEN = 'xxxxxxx:yyyyyyyyyyyyyy'

bot = Bot(TOKEN)
led = machine.Pin('LED', machine.Pin.OUT)
temp = machine.ADC(4)
ceviri = 3.3 / (65535)
led.off()
say = 0

@bot.add_command_handler('start')
def help(update):
    hosgeldin = ('* Hosgeldin VOLKAN * \n')
    hosgeldin += ('*Raspberry Pi Pico W TelegramBot* \n')
    hosgeldin += ('\n*KOMUTLAR:* \n')
    hosgeldin +=('*/ON* : LED ACIK\n*/OFF* : LED KAPALI \n')
    hosgeldin += ('*/deger:* LEDin durumunu gosterir \n')
    hosgeldin += ('*/sensor:* Ortam SICAKLIK degerini gosterir \n')
    hosgeldin += ('*/start:* Baslangic ekranini ve komutlari listeler.')
    update.reply(hosgeldin)
    
@bot.add_command_handler('deger')
def value(update):
    if led.value():
        update.reply('LED ACIK')
    else:
        update.reply('LED KAPALI')

@bot.add_message_handler('^on|On|ON$')
def on(update):
    global say
    say += 1
    led.on()
    ledd = ('*LED ACIK* \n')
    ledd +=('LED ')
    ledd +=(str(say))
    ledd +=(' kere acildi.')
    update.reply(ledd)
        
@bot.add_message_handler('^off|Off|OFF$')
def off(update):
    led.off()
    update.reply('* LED kapalı *')

@bot.add_command_handler('sensor')
def sensor(update):
    oku = temp.read_u16() * ceviri
    isi = round((27 - (oku - 0.706)/0.001721),2)
    mesaj = ('*Ortam sicakligi :  * ')
    mesaj +=(str(isi))
    mesaj +=(' °C')
    update.reply(mesaj)
    
bot.start_loop()
