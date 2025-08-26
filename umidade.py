from machine import Pin, ADC
import time

# --- Configuração dos Pinos ---
# Pino do sensor de umidade de solo
# O ESP32 possui pinos ADC específicos, como o GPIO 34.
# Verifique o diagrama de pinos do seu ESP32.
PINO_SENSOR_UMIDADE = 34

# Pino do LED indicador de solo seco
PINO_LED_SECO = 26

# Crie os objetos Pin e ADC com a configuração correta
# ADC é a classe para leitura analógica
sensor_umidade ADC(Pin(PINO_SENSOR_UMIDADE))
# O LED é uma saída digital
led_seco Pin(PINO_LED_SECO, Pin.OUT)

# Configure a resolução do ADC.
# A resolução padrão é 10 bits (0-1023), mas vamos usar 12 bits para maior precisão (0-4095).
sensor_umidade.width(ADC.WIDTH_12BIT)
# Configure a atenuação. A atenuação de 11dB (ADC.ATTN_11DB) permite ler a faixa de 0 a 3.3V
sensor_umidade.atten (ADC.ATTN_11DB)

# --- Loop Principal de Ação ---
while True:
    # Ação: Ler o valor do sensor
    valor_umidade = sensor_umidade.read()

    # Exibe a leitura no console
    print("Valor do sensor:", valor_umidade)

    # Habilidade: Tomada de Decisão baseada em dados
    # Valores do sensor:
    # Solo seco: 4095 (ou próximo disso)
    # Solo úmido: 0 (ou próximo disso)
    # Ajuste este valor limite (por exemplo, 2000) com base nos seus testes. 
    LIMIAR SECO = 2000

    if valor_umidade > LIMIAR_SECO:
        # Se o solo estiver seco, acende o LED
        print("ALERTA: Solo seco! É hora de regar.")
        led_seco.value(1) # Acende o LED
    else:
        # Se o solo estiver úmido, apaga o LED
        print("Solo úmido. Tudo certo!")
        led_seco.value(0) # Apaga o LED
        
    time.sleep(5) # Aguarda 5 segundos antes da próxima leitura