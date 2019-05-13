# Broker MQTT

## Instalação

O Boker escolhido foi o Mosquitto. 

### Usando apt-get 

Atualizando pacotes e instalnado o pacote mosquitto. 

```bash
$ sudo apt-get update 
$ sudo apt-get upgrade
$ sudo apt-get install mosquitto
$ sudo apt-get install mosquitto-clients
```

## Configuração 


### Arquivo conf

Configurando para não permitir usuários sem login e definindo a porta do broker como 1883 (padrão). 

Editar o arquivo conf:
```
sudo nano /etc/mosquitto/mosquitto.conf
```

Remover a linha abaixo: 
```
include_dir /etc/mosquitto/conf.d
```

Adicionar: 
```
allow_anonymous false
password_file /etc/mosquitto/pwfile
listener 1883
```

### Adicionado usuário 

Adicionando uma entrada no arquivo de login e senha dos usuários:
```bash
$ sudo mosquitto_passwd -c /etc/mosquitto/pwfile nome_do_usuario
```

O serviço mosquito deve ser reiniciado para carregar as novas configurações do arquivo de configuração/: 
```bash
$ sudo systemctl stop mosquitto
$ sudo systemctl start mosquitto
```

## Teste 
Inscrição em um canal via linha de comando:
```bash
$ mosquitto_sub -v -t "topico" -u nome_usuario -P senha
```
Publicando em um canal: 
```bash
mosquitto_pub -d -t 'topicoB' -m "0" -u nome_usuario -P senha
```
O teste pode ser realizado via aplicativo do chrome, MQTTLens. 

### Programação

Variáveis atualizadas no arquivo _boot.py_ 

```python
ssid = '****'
password = '****'
mqtt_server = '****'
server_port=1883
mqtt_user='****'
mqtt_password='****'

topic_sub = b'esp/rele1'
topic_pub = b'esp/vivo'
```

No arquivo _main.py_ a função para subscrição foi atualizada para o tópico desejado. 



