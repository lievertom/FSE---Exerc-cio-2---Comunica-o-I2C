# requires RPi_I2C_driver.py
import RPi_I2C_driver
import time
import smbus2
import bme280

mylcd = RPi_I2C_driver.lcd()

porta_i2c = 1
endereco = 0x76
bus = smbus2.SMBus(porta_i2c)

calibracao_paramentros = bme280.load_calibration_params(bus, endereco)

while True:
    dado = bme280.sample(bus, endereco, calibracao_paramentros)

    mylcd.lcd_display_string('P:{:.2f}'.format(dado.pressure), 1)
    mylcd.lcd_display_string('T:{:.2f} U:{:.2f}'.format(dado.temperature, dado.humidity), 2) 
    time.sleep(1)