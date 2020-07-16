# Solution:

To read the I2C record data file i used the [saleae logic analyzer software](https://www.saleae.com/downloads/) and set the channels to I2C protocol.
![alt text](https://github.com/VikiFadlon/HackTheBox/blob/master/Hardware/Mission%20Pinpossible/Images/I2C_record.JPG)

After exporting the data i'm looking for the chip PCF8574 (main component on LCD I2C adapter) I2C address from the datasheet, the address set from pins A0,A1,A2 state according to the device datasheet: 
![alt text](https://github.com/VikiFadlon/HackTheBox/blob/master/Hardware/Mission%20Pinpossible/Images/PCF8574.JPG)

From the LCD I2C adapter schematic we can see that the LCD run on 4-bit bus mode, it needs to transfer 4 bit data by two times.
![alt text](https://github.com/VikiFadlon/HackTheBox/blob/master/Hardware/Mission%20Pinpossible/Images/I2C_LCD_adapter.JPG)

Reading the data and find the characteristics using the LCD 16X2 datasheet (1602A-1)
![alt text](https://github.com/VikiFadlon/HackTheBox/blob/master/Hardware/Mission%20Pinpossible/Images/LCD_char.JPG)


