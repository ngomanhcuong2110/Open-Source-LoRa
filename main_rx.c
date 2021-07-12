#include <msp430.h>
#include "lora.h"

char rxdata[255];

void main(void)
{
    if(!LoRa_Init(433E6))
    {
        Write_PC("\r\nStarting LoRa RX Failed");
        while(1);
    }

    Write_PC("\r\nStarting LoRa RX OK");

    while(1)
    {
        LoRa_receive(0);
        LoRa_readPacket(rxdata, 5000);
        Write_PC(rxdata);
    }
}
