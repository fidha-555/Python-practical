from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def boot(self):
        pass

    def _check_hardware(self):
        print("Checking Hardware..")

    def _load_os(self):
        print("Loading OS..")

class Laptop(Device):
    def boot(self):
        self._check_hardware()
        self._load_os()
        print("Device is Ready!")



d = Laptop()
d.boot()