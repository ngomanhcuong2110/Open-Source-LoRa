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

data = []

def LoRa_txMode():
    LoRa.idle() # set standby mode
    LoRa.disableInvertIQ() # normal mode

def LoRa_rxMode():
    LoRa.enableInvertIQ() # active invert I and Q signals
    LoRa.receive() # set receive mode

def main():
    if LoRa.Init(433E6) == 0:
        print("Starting LoRa RX Failed")
        while True:
            pass

    print("Starting LoRa RX Successful")

    LoRa.setGain(6)
    LoRa.setTxPower(20)

    LoRa.setSignalBandwidth(125E3)
    LoRa.setSpreadingFactor(12)
    LoRa.setPreambleLength(8)
    LoRa.setCodingRate4(5)
    LoRa.enableCrc()

    while True:
        LoRa_rxMode()
        size = LoRa.readPacket(data, 1000)
        if size > 0:
            print("[RX] <-", LoRa.convert(data), ", RSSI:", LoRa.packetRssi())
        else:
            print("[RX] <- Error")

if __name__ == '__main__':
    main()
