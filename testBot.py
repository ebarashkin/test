import sys
import api
import serial

PORT = '/dev/ttyUSB0'
BAUDRATE = 9600

STATIC_CMD = {}
STATIC_CMD['Зелёный'] = 'A'
STATIC_CMD['Красный'] = 'B'
STATIC_CMD['Красная'] = 'C'
STATIC_CMD['Синяя'] = 'D'
STATIC_CMD['Помахать'] = 'F'
STATIC_KEYBOARD = [list(STATIC_CMD.keys())[:3], list(STATIC_CMD.keys())[3:]]

arduino = None
try:
    arduino = serial.Serial(PORT, BAUDRATE, timeout=0)
except serial.serialutil.SerialException as e:
    print(e)
    sys.exit()

telegram = api.TelegramBot('601071819:AAGf0OobZXOkfF91VZe6DR_5i60LYXlccSg')

def message_handler(messages):
    for msg in messages:
        print(msg)
        if '/start' in msg[1]:
            answer = 'Welcome to my remote Arduino control!'
            telegram.send(msg[0], answer, STATIC_KEYBOARD)
            continue
        if msg[1] in STATIC_CMD:
            arduino.write(STATIC_CMD[msg[1]].encode('utf-8'))
            continue
        if 'Температура' in msg[1]:
            arduino.write('E'.encode('utf-8'))
            answer = arduino.readline().decode('utf-8')
            if answer:
                telegram.send(msg[0], answer)
            continue

        telegram.send(msg[0], 'Wrong command', STATIC_KEYBOARD)

telegram.listen(message_handler)
