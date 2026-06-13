import sys
import Ice
import Demo


class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)
        return s + "*"

    def fatorial(self, n, current=None):
        if n == 0:
            return 1
        return n * self.fatorial(n - 1)

    def calc_pi(self, precision, current=None):
        k = 1
        parcel = 4 / k
        s = 0
        i = 0
        while abs(parcel) > precision:
            s += parcel
            k += 2
            i += 1
            if i % 2 == 0:
                parcel = 4 / k
            else:
                parcel = -4 / k
        return s


communicator = Ice.initialize(sys.argv)

adapter = communicator.createObjectAdapterWithEndpoints(
    "SimpleAdapter", "default -p 11000"
)
obj = PrinterI()
adapter.add(obj, Ice.stringToIdentity("SimplePrinter"))

adapter.activate()

communicator.waitForShutdown()
