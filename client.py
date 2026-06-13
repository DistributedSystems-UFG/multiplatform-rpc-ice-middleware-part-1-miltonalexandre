import sys
import Ice
import Demo

with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("SimplePrinter:tcp -h 127.0.0.1 -p 11000")

    printer = Demo.PrinterPrx.checkedCast(base)
    if not printer:
        raise RuntimeError("Invalid proxy")

    print(printer.printString("Hello World!"))
    print(printer.fatorial(5))
    print(printer.calc_pi(0.0001))
