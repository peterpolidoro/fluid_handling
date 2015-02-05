from __future__ import print_function,division
from arduino_device import ArduinoDevice

class FluidHandling(object):
    def __init__(self):
        self.dev = ArduinoDevice()
    def state1(self):
        self.dev.set_relays(17)
    def state2(self):
        self.dev.set_relays(18)
    def state3(self):
        self.dev.set_relays(20)
    def state4(self):
        self.dev.set_relays(24)
    def state5(self):
        self.dev.set_relays(0)
    def state6(self):
        self.dev.set_relays(32)
