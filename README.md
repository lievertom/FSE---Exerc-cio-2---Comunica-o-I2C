
# FSE - Exercício 2 - Comunicação I2C

## 1 - OBJETIVOS

Neste trabalho o(a) aluno(a) irá exercitar o uso do protocolo de comunicação I2C utilizando
a linguagem Python para comunicar a placa Raspberry Pi com dois dispositivos externos: um
Sensor de Pressão, Umidade e Temperatura modelo BME280 e um Display LCD de 16x
caracteres.

## 2 - COMPONENTES

### 2.1 Sensor de Pressão, Umidade e Temperatura modelo BME

O sensor a ser usado no experimento é o modelo BME280, fabricado pela Bosch, que
possui internamente suporte aos protocolos I2C e SPI.

| Grandeza | Faixa de Operação | Acurácia|
| -------- | ----------------- | ------- |
| **Umidade** | 0 % a 100 % | ± 3 %|
| **Temperatura** | -40 a 80 ̊C | ± 0.5 ̊C |
| **Pressão** | 300 a 1100 hPa | ± 0.12 hPa |

A placa que contém o sensor BME280 deste exercício possui suporte exclusivo ao
protocolo I2C e opera com tensão de 5V. Portanto, para a interface com a placa Raspberry Pi que
opera em tensão de 3.3V será necessário o uso de um conversor lógico bidirecional de 3.3V/5V.

**Datasheet:**  <https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf>

### 2.2 Display LCD 16x2

O módulo Display LCD 16x2 a ser utilizado possui duas linhas de 16 caracteres cada uma
bom _backlight_ azul e módulo I2C integrado. O display utiliza o controlador HD44780.

## 3 - CIRCUITO ESQUEMÁTICO

Para conectar a placa Raspberry Pi aos dispositivos via I2C serão utilizados os pinos 3
(SDA / GPIO 2) e 5 (SCL / GPIO 3) da placa Raspberry Pi. O sensor BME280 utilizado neste
exercício possui tensão de operação de 5V e portanto, será utilizado um circuito auxiliar
(Conversor de nível lógico de 5V / 3.3V Bidirecional) para fazer a interface entre os pinos da placa
Raspberry Pi (3.3V) e o sensor (5V). O módulo Display LCD 16x2 utilizado já possui conversor I2C
incorporado e opera nas tensões 3.3V ou 5V e portanto pode ser conectado diretamente ao
barramento I2C da placa Raspberry Pi ou através do conversor.

## 4 - ROTEIRO

## 4.1 - Programa em Python

Criar um programa em Python que leia as 3 grandezas (Temperatura, Umidade e Pressão) do
sensor BME280 e as apresente no display utilizando 2 casas decimais e sendo atualizadas a cada
1 segundo.

**Dependências:**

1. Utilizar as bibliotecas: **_smbus2_** (I2C) e **_bme280_** (Sensor)

    ```bash
        pip3 install smbus
        pip3 install RPi.bme
    ```

2. Biblioteca para escrita no Display LCD:

    - <https://gist.github.com/DenisFromHR>

O sensor está no endereço 0x76 do barramento I2C enquanto o Display LCD está no endereço
0x27. Isso pode ser verificado através do comando: **i2detect -y 1**

## 4.2 - Programa em C

Criar um programa em C, utilizando a biblioteca oficial do fabricante (Bosch) para realizar a
medida das 3 grandezas (Temperatura, Umidade e Pressão) a cada 1 segundo e registrar, a cada
10 segundos, a média das amostras em um arquivo em formato CSV registrando data e hora de
cada registro.

**Repositório da Bosch:** <https://github.com/BoschSensortec/BME280_driver>
