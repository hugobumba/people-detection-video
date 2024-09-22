# Detecção de Pedestres em Vídeo

Este projeto utiliza o HOG (Histograms of Oriented Gradients) para detectar pedestres em um vídeo. O código é baseado na biblioteca OpenCV e realiza processamento em tempo real.

## Requisitos

- Python 3.8.0
- OpenCV
- NumPy
- imutils

## Instalação

Para instalar as dependências, execute:

```bash
pip install opencv-python numpy imutils
```

## Uso

1. Coloque um vídeo no mesmo diretório do script.
2. Execute o script:

```bash
python pedestrian_detection_video.py
```

3. O programa abrirá uma janela mostrando o vídeo com os pedestres detectados.

## Funcionamento

- O código inicializa o detector HOG.
- O vídeo é lido frame a frame e cada frame é processado.
- Os pedestres detectados são destacados com retângulos e etiquetas.
- O total de pedestres detectados é exibido na tela.