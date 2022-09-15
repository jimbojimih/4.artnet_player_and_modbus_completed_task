import socket 
import time
from abc import ABC, abstractmethod
from pymodbus.client.sync import ModbusTcpClient

class ModbusBroadcast():    
    #self, unit=0x21, relay_output1=0x0000, relay_output2=0x0001
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.outputs = []
        self.units = []    
        
    def connect(self):
        self.client = ModbusTcpClient(self.host, self.port)
        self.client.connect()
        
    def set_broadcast_settings(self, outputs, modules):
        self.outputs = outputs
        self.modules = modules
        
    def write_coil_false(self):
        for module in self.modules:
            for output in self.outputs:
                self.client.write_coil(output, 0, unit=module)
                self.client.write_coil(output, 0, unit=module)
        
    def write_coil_true(self):
        for module in self.modules:
            for output in self.outputs:
                self.client.write_coil(output, 1, unit=module)
                self.client.write_coil(output, 1, unit=module)

a = ModbusBroadcast('localhost', 502)
a.connect()
outputs = [0x0000, 0x0001]
modules = [0x21]
a.set_broadcast_settings(outputs, modules)
a.write_coil_false()
'''        
class ArtnetAndModbusSender():
    def __init__(self, host1="localhost", host2="127.0.0.2", port=6454,
                 range_=5, sleep1=.025, sleep2=5, file='Test_Color.ani'):
        self.host1 = host1
        self.host2 = host2
        self.port = port
        self.range_ = range_
        self.sleep1 = sleep1
        self.sleep2 = sleep2
        self.file = file
        #self.m = modbus_sender(host='192.168.0.10', port=8234) #modbus
        self.m = modbus_sender()
        self.m.connect()
    def connect(self):
        self.s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s1.connect((self.host1, self.port))
        self.s2.connect((self.host2, self.port))
    def open_packages(self):
        with open('Test_Color.ani', mode='rb') as f: 
            self.packages = f.read() 
    def main_loop(self):
        self.connect()
        self.open_packages()
        for i in range(self.range_):
            i = 0 #index low
            x = 530 #index hight
            self.m.write_coil_true() #send modbus on
            while x <= len(self.packages):
                self.package = self.packages[i:x]
                i += 530
                x += 530            
                self.byte_14 = self.package[14]
                if self.byte_14 == 1:
                    self.s1.sendall(self.package)                       
                else:
                    self.s2.sendall(self.package)
                #time.sleep(self.sleep1)
                if x > 20000000:
                    print(x)
            self.m.write_coil_false() #send modbus off
            time.sleep(self.sleep2)   

if __name__ == '__main__':
    #a = artnet_and_modbus_sender(host1='192.168.0.1', host2='192.168.0.2',
    #                             port=6454)
    a = artnet_and_modbus_sender(host2='127.0.0.2')
    a.main_loop()
'''
