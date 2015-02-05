from __future__ import print_function,division
from arduino_device import ArduinoDevice

class FluidHandling(object):
    def __init__(self):
        self.dev = ArduinoDevice()
    def state1(self):
        self.dev.setRelays(17)
    def state2(self):
        self.dev.setRelays(18)
    def state3(self):
        self.dev.setRelays(20)
    def state4(self):
        self.dev.setRelays(24)
    def state5(self):
        self.dev.setRelays(0)
    def state6(self):
        self.dev.setRelays(32)
