#include <msp430.h>
#include "lora.h"

void main(void)
{
    if(!LoRa_Init(433E6))
    {
        Write_PC("\r\nStarting LoRa TX Failed");
        while(1);
    }

    Write_PC("\r\nStarting LoRa TX OK");

    while(1)
    {
        LoRa_beginPacket(false);
        LoRa_sendPacket("0123456789");
        LoRa_endPacket(false);
        delay_ms(2000);
    }
}
