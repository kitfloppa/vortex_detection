import cv2
import torch


if __name__ == "__main__":
    model = torch.hub.load('yolov5', 'custom', path='best.pt', source='local')
    img = cv2.imread('vortex.jpg')

    result = model(img)

    print(type(result))
