DOCUMENTAÇÃO DO PROJETO IoT COM Raspberry Pi, ESP32, Flask e MQTT

- Introdução

Este projeto foi desenvolvido com o objetivo de explorar a Internet das Coisas (IoT) usando MQTT para conectar dispositivos em tempo real. Utilizamos uma Raspberry Pi como broker MQTT, um ESP32 para controle de dispositivos e Flask para a interface web, permitindo o gerenciamento de LEDs e monitoramento de status diretamente pelo navegador.

- Tecnologias Utilizadas

Raspberry Pi - Broker MQTT com Mosquitto

ESP32 - Dispositivo para controle de LED

Flask - Sistema web para exibir o status dos dispositivos

MQTT Explorer - Ferramenta para testes e envio de comandos

LED - Dispositivo para demonstração do sistema


- Funcionalidades

Controle remoto de dispositivos via MQTT

Interface web para visualização do status

Integração com LED para feedback visual


- Arquitetura do Sistema

O sistema foi estruturado em três partes principais:

1. Broker MQTT (Raspberry Pi) - Responsável por gerenciar os tópicos e distribuir as mensagens.


2. Dispositivo IoT (ESP32) - Conectado ao broker para controlar o LED.


3. Sistema Web (Flask) - Exibe o status do LED e recebe as atualizações em tempo real.



- Fluxo de Funcionamento

1. O comando é enviado via MQTT Explorer para a Raspberry Pi.


2. A Raspberry Pi repassa o comando para o ESP32.


3. O ESP32 interpreta o comando e controla o LED.


4. O sistema web Flask exibe o status atualizado.

- Conclusão

Este projeto foi uma excelente oportunidade para aplicar conceitos de IoT, explorar o uso do protocolo MQTT e desenvolver habilidades práticas em programação e integração de dispositivos.

Desenvolvedores:

@ Pedro Ribero
@ Leonardo Felix
