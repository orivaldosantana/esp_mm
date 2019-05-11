# ESP, MicroPython e MQTT
Este repositório realiza alguns testes introdutórios com ESP, MicroPython e MQTT 

## Instalação 
* uPyCraft -IDE de desenvolvimento em MicroPython e ESP, https://www.embarcados.com.br/micropython-no-esp8266/

## Configuração do Broker MQTT 
* CloudMQTT - Disponível na internet e possui um plano básico limitado e gratuíto, https://www.cloudmqtt.com/ 

## Teste 1
* Criando um cliente MQTT no ESP
* Publicando em um tópico ('hello') 
* Subescrevendo em um tópico ('notification') 
* Testando a comunicação via "Websocket UI" do site cloudmqtt
* Arquivos disponíveis na pasta "/teste1" 

## Teste 2
* Ajustando o cliente MQTT no ESP para uso de um relé
* Subescrevendo em um tópico ('rele1')
* Modificando a função 'sub_cb' para desativar o relé quando receber 0 ou ativar quando receber 1 no tópico 'rele1'
* Arquivos disponíveis na pasta "/teste2" 

## Teste 3 
* Instalando o Broker MQTT no rapsberry pi
* Configurando um _hostname_ local para o raspberry pi 
* Configurando o Broker 
* Realizando um teste local, via cliente execuntando em linha de comando 
* Realizando com o aplicativo do google chrome, MQTTLens



## Referências 
* Primeiros passos com MicroPython no ESP8266, https://www.embarcados.com.br/micropython-no-esp8266/
* MicroPython – Getting Started with MQTT on ESP32/ESP8266, https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/ 
* IDE uPyCraft, https://github.com/DFRobot/uPyCraft_src
* ESP8266 com MQTT controlando lâmpada ligada em outro ESP (Interruptor WiFi) [ESP8266 #07],  https://www.youtube.com/watch?v=oX4ttJEULmA
* O protocolo MQTT, https://www.gta.ufrj.br/ensino/eel878/redes1-2018-1/trabalhos-vf/mqtt/ 
* Instalando Broker Mosquitto - Filipe Flop,  https://www.filipeflop.com/blog/broker-mqtt-com-raspberry-pi-zero-w/
* Instalando Broker Mosquitto - Random Nerd Tutorial, https://randomnerdtutorials.com/how-to-install-mosquitto-broker-on-raspberry-pi/ 
* Teste local do Broker,  https://randomnerdtutorials.com/testing-mosquitto-broker-and-client-on-raspbbery-pi/ 
