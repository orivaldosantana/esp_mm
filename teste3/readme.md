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
$ sudo systemctl start mosquitto
$ sudo systemctl start mosquitto
```

## Teste 
```bash
$ mosquitto_sub -v -t "topico" -u nome_usuario -P senha
```




