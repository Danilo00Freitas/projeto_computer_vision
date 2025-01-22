# Treinando YoloV8

## Sobre o Projeto
Este projeto utiliza o modelo YoloV8 para criar um sistema que bloqueia o computador e somente desbloqueia quand
o modelo treinado reconhecer que estou bebendo água. 
A ideia principal é incentivar hábitos saudáveis, como manter-se hidratado, de forma interativa e automatizada.

### Funcionalidades Implementadas
- Reconhecimento básico do rosto e de um copo de água.
- O sistema libera a tela preta após **50 frames consecutivos** de reconhecimento bem-sucedido.
- Implementação inicial baseada em um treinamento próprio do modelo YoloV8.

### Objetivos Futuros
- Aprimorar a confiabilidade do reconhecimento de gestos e objetos.
- Expandir o projeto com suporte para diferentes cenários e comportamentos.
- Aprender e aplicar mais conceitos avançados de **computer vision**.

---

## Como Configurar o Projeto

### 1. Instalando PyTorch com CUDA (para usar GPU)
Caso possua uma GPU compatível com CUDA, instale o PyTorch configurado para utilizá-la. Consulte o site oficial do PyTorch para instruções detalhadas de instalação:  
[https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)

### 2. Instalando a Biblioteca YoloV8
Para instalar o YoloV8, utilize o seguinte comando no terminal:
```bash
pip install ultralytics
```

---

## Treinamento do Modelo

Como base para o treinamento da YOLO utilizei o conteúdo do vídeo **"Treinando Redes Neurais Com Imagens Próprias"**, disponível no YouTube. 
Este vídeo ajudou a construir a base para realizar o treinamento utilizando o arquivo `train_drinkWater_v8.py`.

Você pode assistir ao vídeo para compreender os conceitos utilizados no treinamento:  
[![Treinando Redes Neurais Com Imagens Próprias](https://img.youtube.com/vi/KV5lszcKuiE/0.jpg)](https://www.youtube.com/watch?v=KV5lszcKuiE)  

---
