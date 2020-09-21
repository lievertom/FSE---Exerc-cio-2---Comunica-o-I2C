# Programa em Python

## Proposta

Criar um programa em Python que leia as 3 grandezas (Temperatura, Umidade e Pressão) do sensor BME280 e as apresente no display utilizando 2 casas decimais e sendo atualizadas a cada 1 segundo.

## Dependências

1. Utilizar as bibliotecas: **_smbus2_** (I2C) e **_bme280_** (Sensor)

    ```bash
    pip3 install smbus
    pip3 install RPi.bme
    ```

2. Biblioteca para escrita no Display LCD:
    - <https://gist.github.com/DenisFromHR>

O sensor está no endereço 0x76 do barramento I2C enquanto o Display LCD está no endereço
0x27. Isso pode ser verificado através do comando: **i2cdetect -y 1**

## Execução

1. Clonar repositório:

    ```bash
    git clone https://github.com/lievertom/FSE_Exercicio_2_Comunicao_I2C.git
    ```

2. Entrar no diretório programa_em_python:

    ```bash
    cd FSE_Exercicio_2_Comunicao_I2C/programa_em_python
    ```

3. Executar:

    ```bash
    python3 main.py
    ```

4. Parar:

    `Ctrl+c`

## Resultado Esperado

- mostrar no display os valores aferidos para temperatura, pressão e humidade.
