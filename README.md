Projeto IoT com Raspberry Pi, ESP32, Flask e MQTT

📋 Introdução

Este projeto foi desenvolvido para explorar a Internet das Coisas (IoT), utilizando o protocolo MQTT para conectar dispositivos em tempo real. Ele integra uma Raspberry Pi como broker MQTT, um ESP32 para controle de dispositivos e Flask para a interface web, permitindo o gerenciamento de LEDs e monitoramento de status diretamente pelo navegador.

🚀 Tecnologias Utilizadas

Raspberry Pi - Broker MQTT com Mosquitto

ESP32 - Dispositivo para controle de LEDs

Flask - Sistema web para exibir o status dos dispositivos

MQTT Explorer - Ferramenta para testes e envio de comandos

LED - Dispositivo para demonstração do sistema

🛠️ Funcionalidades

Controle remoto de dispositivos via MQTT

Interface web para visualização do status

Integração com LED para feedback visual

🗂️ Arquitetura do Sistema

O sistema foi estruturado em três partes principais:

Broker MQTT (Raspberry Pi) - Responsável por gerenciar os tópicos e distribuir as mensagens.

Dispositivo IoT (ESP32) - Conectado ao broker para controlar o LED.

Sistema Web (Flask) - Exibe o status do LED e recebe as atualizações em tempo real.

🔄 Fluxo de Funcionamento

O comando é enviado via MQTT Explorer para a Raspberry Pi.

A Raspberry Pi repassa o comando para o ESP32.

O ESP32 interpreta o comando e controla o LED.

O sistema web Flask exibe o status atualizado.

✅ Conclusão

Este projeto foi uma excelente oportunidade para aplicar conceitos de IoT, explorar o uso do protocolo MQTT e desenvolver habilidades práticas em programação e integração de dispositivos.
