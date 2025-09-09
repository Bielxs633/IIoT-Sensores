from machine import Pin, time_pulse_us
import time


#configuração de pinos
TRIG_PIN = 25
ECHO_PIN = 27
LED_PIN = 26

trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)
led = Pin(LED_PIN, Pin.OUT)


#variáveis de contagem
frascos = 0
caixas = 0
detectando = False

#medindo distancia
def obter_distancia():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    duracao = time_pulse_us(echo, 1, 30000)
    distancia = (duracao / 2) * 0.0343
    return distancia


#loop principal
print('Sistema de Contagem Alpha Corp')
while True:
    dist = obter_distancia()

    #frasco foi detectado
    if dist < 10 and not detectando:
        detectando = True
        frascos += 1
        print(f'Frasco detectado! Total de frascos: {frascos}')

        #quando atingir 10 frascos → conta 1 caixa
        if frascos == 10:
            caixas += 1
            frascos = 0
            print(f'Caixa completa! Total de caixas: {caixas}')

            #sinaliza no LED
            led.value(1)
            time.sleep(0.5)
            led.value(0)

    #libera o sensor para próxima leitura
    if dist >= 10:
        detectando = False

    time.sleep(0.1)

