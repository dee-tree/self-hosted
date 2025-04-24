#!/usr/bin/env python3
# This python script is only suitable for UPS Shield X1200, X1201 and X1202 for Rasberry Pi 5

# Prints UPS battery level and voltage for prometheus node-exporter

import struct
import smbus2
import time
from subprocess import call
import sys
from os import replace
from os import makedirs
from os import path

def readVoltage(bus):
     address = 0x36
     read = bus.read_word_data(address, 2)
     swapped = struct.unpack("<H", struct.pack(">H", read))[0]
     voltage = swapped * 1.25 /1000/16
     return voltage

def readCapacity(bus):
     address = 0x36
     read = bus.read_word_data(address, 4)
     swapped = struct.unpack("<H", struct.pack(">H", read))[0]
     capacity = swapped/256
     return capacity

bus = smbus2.SMBus(1)
UPS_SHUTDOWN_TRESHOLD_V = 3.20
DEFAULT_OUT_FILE = "/var/log/ups/ups-node-exporter.prom"

def main(out):
    voltage = readVoltage(bus) # (battery voltage)
    capacity = readCapacity(bus) # (battery level)

    tmpout = out + ".new"

    makedirs(path.dirname(tmpout), exist_ok=True)
    with open(tmpout, "w") as f:
        f.writelines([
              "# HELP node_ups_voltage UPS power voltage, V\n",
              "# TYPE node_ups_voltage gauge\n",
              "node_ups_voltage %3.2f\n" % voltage,

              "# HELP node_ups_level UPS power level, %\n",
              "# TYPE node_ups_level gauge\n",
              "node_ups_level %3i\n" % capacity,

              "# HELP node_ups_shutdown_treshold_v UPS voltage shutdown treshold, %\n",
              "# TYPE node_ups_shutdown_treshold_v gauge\n",
              "node_ups_shutdown_treshold_v %3.2f\n" % UPS_SHUTDOWN_TRESHOLD_V,
        ])
    
    replace(tmpout, out)
    

    # set battery low voltage to shut down
    if readVoltage(bus) < UPS_SHUTDOWN_TRESHOLD_V:
        print("[WARNING] UPS: battery LOW (%3i%% %, %3.2f V), going to shutdown in 5 seconds" % capacity % voltage, file=sys.stderr)
        time.sleep(5)
        print("[WARNING] UPS: going to shutdown", file=sys.stderr)

        call("sudo nohup shutdown -h now", shell=True)

if __name__ == "__main__":
    outfile = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUT_FILE
    main(out=outfile)
