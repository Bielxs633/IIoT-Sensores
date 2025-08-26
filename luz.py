from machine import Pin, ADC
import time
# --- Configuração dos Pinos ---
# Pino para o sensor Fotoresistor LDR
#D pino GPIO4 será usado para leitura analógica
PINO_LDR = 4
# Pino do LED indicador de ambiente escuro
# O pino GP1023 será usado para controlar o LED
PINO_LED_ESCURO = 23
# Crie os objetos ADC e Pin com a configuração correta.
# A classe ADC é para leitura analógica
sensor_ldr = ADC(Pin(PINO_LDR))
# A classe Pin é para controle digital (ligar/desligar o LED)
led_escuro = Pin(PINO_LED_ESCURO, Pin.OUT)
# Configure a resolução do ADC para malor precisão (12 bits).
sensor_ldr.width(ADC.WIDTH_12BIT)
# Configure a atenuação para a faixa de 0 a 3.3V
sensor_ldr.atten(ADC.ATTN_11DB)
# --Loop Principal de Ação
while True:
    # Ação: Ler o valor do sensor LDR 
    valor_luminosidade = sensor_ldr.read() 
    #Exibe a leitura no console 
    print("Valor de luminosidade:", valor_luminosidade) 
    #Habilidade: Tomada de Decisão baseada en dados 25
    #A lógica de leitura do LDR é: quanto mais AUSENCIA DE LUZ 
    LIMIAR_ESCURO = 400

    if valor_luminosidade < LIMIAR_ESCURO: 
        #Se o valor for biaxo (indicando pouca luz), acende o LED
        print("Ambiente escuro! Acendendo o LED.")
        led_escuro.value(1) # Acende o LED
    else:
        #Se houver luz, apaga o LED
        print("Ambiente claro. LED apagado.")
        led_escuro.value(0) # Apaga o LED
    time.sleep(1) # Aguarda 1 segundo antes da próxima leitura   