from machine import Pin, time_pulse_us
import time
#Configuração dos Pinos
#Pinos do sensor ultrassônico HC-SR04
PINO_TRIG = 25
PINO_ECHO = 27
#Pino do LED vermelho
#Escolha un pino GPIO digital disponível, por exemplo, o 26.
#Verifique o diagrama de pinos do seu ESP32 no simulador ou datashee
PINO_LED_INTRUSO = 26
#Crie os objetos Pin com a configuração correta
trig = Pin(PINO_TRIG, Pin.OUT)
echo = Pin(PINO_ECHO, Pin.IN)
led_intruder = Pin(PINO_LED_INTRUSO, Pin.OUT)
#Funcão de Medição de Distância (sem alterações)
def obter_distancia():
    #Mede a distância en centimetros usando o sensor HC-5884.
    trig.value(0)
    time.sleep_us(2)

    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    duracao = time_pulse_us(echo, 1, 30000)
    distancia = (duracao /2) * 0.0343
    return distancia

#Loop Principal de Ação
while True:
    dist = obter_distancia()
    print("Distancia:", dist, "cm")
    #Ação de Atuação: Controle do LED
    if dist < 10:
        #Se a distância for menor ou igual a 18 cm, acende a LED
        print("INTRUSO DETECTADO!")
        led_intruder.value(1) #Acende o LED (sinal HIGH)
        time.sleep(1)
    else:
        #Se não houver Intruso, apaga o LED
        print("Ambiente seguro.")
        led_intruder.value(8) #Apaga o LED (sinal LOW)
        time.sleep(3)