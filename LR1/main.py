import serial
import threading, sys


class Worker(threading.Thread):

    def __init__(self, num_thread):
        # вызываем конструктор базового класса
        super().__init__()
        # определяем аргументы собственного класса
        self.num_thread = num_thread

    def run(self):
        while(1):
            sp.send(input().encode('utf-8'))





class SerPort(serial.SerialBase):
    def __init__(self, name, baudrate):
        self.name = name
        try:
            self.serialPort = serial.Serial(self.name)
            self.serialPort.baudrate = baudrate
            print(f'Port {self.name} was successfully connected')
        except Exception as e:
            print(e)


    def send(self, data):
        try:
            if (self.serialPort):
                self.serialPort.write(data)
        except IOError as ioe:
            print(f"Port {self.name} can't send data")

    def receive(self):
        try:
                rec_data = self.serialPort.read(self.serialPort.inWaiting())
        except IOError as ioe:
            print(f"Port {self.name} can't read data")
        return rec_data


    def inWaiting(self):
        k = 0
        if self.serialPort.inWaiting():
            k = 1
        return self.serialPort.inWaiting()

    def setBaud(self, baudrate):
        self.serialPort.baudrate = baudrate

    def getBaud(self):
        return self.serialPort.baudrate

    def showBaud(self):
        print(f'Now baud is {sp.getBaud()}')



sp = SerPort('COM1', 9600)
print(f'Now baud is {sp.getBaud()}')

th = Worker(1)
th.start()


while(1):
    if sp.inWaiting():
        data = sp.receive().decode('utf-8')
        if ('set baud' in data):
            speed = data.split()[2]
            if (speed.isdigit()):
                if int(speed)>0:
                    sp.setBaud(speed)
                print(f'Now baud is {sp.getBaud()}')
            else:
                print(data)
        elif (data=='show baud'):
            sp.showBaud()
        elif (data=='disconnect'):
            sp.send('disconnect'.encode('utf-8'))
            sys.exit()
        else:
            print(data)










#     def switch(self, case):
#         try:
#             switcher = {
#                 110: 1040,
#                 150: 768,
#                 300: 384,
#                 600: 600,
#                 1200: 96,
#                 2400: 48,
#                 4800: 24,
#                 9600: 12,
#                 19200: 6,
#                 38400: 3,
#                 57600: 2,
#                 115200: 1
#             }
#             switcher[case]
#             return switcher[case]
#         except KeyError as ke:
#             raise KeyError(f'Invalid baud {ke.args}')
#
#
# # from serial.tools import list_ports
# # print(list_ports.comports())










#print(switch(110))
