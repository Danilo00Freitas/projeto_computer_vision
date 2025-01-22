from ultralytics import YOLO
import cv2
from collections import defaultdict
import numpy as np
import pyautogui

# Configurações de captura de tela
offset_x = 400  # Coordenada X da origem
offset_y = 300  # Coordenada Y da origem
width = 800     # Largura da área de captura
height = 600    # Altura da área de captura

# Carrega o modelo YOLO treinado
model = YOLO("/home/dandan/Documentos/estudos/drink_water/drink_water_yolo/runs/detect/train/weights/best.pt")

track_history = defaultdict(lambda: [])
seguir = True
deixar_rastro = True

while True:
    try:
        # Captura uma imagem da área definida
        screenshot = pyautogui.screenshot(region=(offset_x, offset_y, width, height))
        img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        if seguir:
            results = model.track(img, persist=True)
        else:
            results = model(img)

        # Processa os resultados
        for result in results:
            # Visualiza os resultados no frame
            img = result.plot()

            if seguir and deixar_rastro:
                try:
                    # Obtém as caixas e IDs de rastreamento
                    boxes = result.boxes.xywh.cpu()
                    track_ids = result.boxes.id.int().cpu().tolist()

                    # Desenha as linhas de rastreamento
                    for box, track_id in zip(boxes, track_ids):
                        x, y, w, h = box
                        track = track_history[track_id]
                        track.append((float(x), float(y)))  # Ponto central x, y
                        if len(track) > 30:  # Mantém 30 trilhas para 30 frames
                            track.pop(0)

                        # Desenha as linhas de rastreamento
                        points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
                        cv2.polylines(img, [points], isClosed=False, color=(230, 0, 0), thickness=5)
                except Exception as e:
                    print(f"Erro durante o rastreamento: {e}")

        # Exibe a imagem capturada
        cv2.imshow("Tela", img)

        # Interrompe o loop ao pressionar 'q'
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    except Exception as e:
        print(f"Erro durante a captura ou processamento: {e}")
        break

cv2.destroyAllWindows()
print("Desligando")
