#                               ___  ___ ___
#                              /   ||  _ \  |    _   _
#                             / /| || |_) ) |__ | | | |
#                            / /_| ||  __/|  _ \| | | |
#                           / ___  || |   | | | | |_| |
# Author: Tran Van The Phu /_/   |_||_|   |_| |_\_____| Dai hoc Can Tho
# Gmail: tranvanthephu@gmail.com
# Edit from Sandeep LoRa library https://github.com/sandeepmistry/arduino-LoRa

import time
from lora import LoRa

LoRa = LoRa()

def LoRa_txMode():
    LoRa.idle() # set standby mode
    LoRa.enableInvertIQ() # active invert I and Q signals

def LoRa_rxMode():
    LoRa.disableInvertIQ() # normal mode
    LoRa.receive() # set receive mode

def main():
    if LoRa.Init(433E6) == 0:
        print("Starting LoRa TX Failed")
        while True:
            pass

    print("Starting LoRa TX Successful")

    LoRa.setGain(6)
    LoRa.setTxPower(20)

    LoRa.setSignalBandwidth(125E3)
    LoRa.setSpreadingFactor(12)
    LoRa.setPreambleLength(8)
    LoRa.setCodingRate4(5)
    LoRa.enableCrc()

    count = 0

    while True:
        LoRa_txMode()
        data = 'Raspberry Pi LoRa - ' + str(count)
        LoRa.sendPacket(data)
        print("[TX] ->", data)
        count += 1
        time.sleep(1)

if __name__ == '__main__':
    main()
