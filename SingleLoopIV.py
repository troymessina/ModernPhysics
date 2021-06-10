"""CircuitPython Analog Out example"""
import board
from analogio import AnalogOut
from analogio import AnalogIn
import time

Vout = AnalogOut(board.A0)
VLED = AnalogIn(board.A1)
j=0
while j<1: #run the loop once
    # Count up from 0 to 65535, with 64 increment
    # which ends up corresponding to the DAC's 10-bit range
    for i in range(0, 65535, 512):
        Vout.value = i
        print((VLED.value/65535*3.3, i*3.3/65535))
        time.sleep(0.05)
    j+=1