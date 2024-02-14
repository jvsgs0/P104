import cv2

img = cv2.imread("solar-system.jpg")

planet_data = {
    'Sol': {'position': (100, 100), 'font_scale': 1.2, 'color': (0, 165, 255)},
    'Mercurio': {'position': (100, 200), 'font_scale': 0.5, 'color': (128, 128, 128)},
    'Venus': {'position': (200, 220), 'font_scale': 0.7, 'color': (0, 255, 255)},
    'Terra': {'position': (300, 220), 'font_scale': 0.7, 'color': (0, 255, 0)},
    'Marte': {'position': (400, 210), 'font_scale': 0.6, 'color': (0, 0, 255)},
    'Jupiter': {'position': (600, 330), 'font_scale': 1.2, 'color': (0, 128, 255)},
    'Saturno': {'position': (780, 300), 'font_scale': 1.1, 'color': (42, 42, 165)},
    'Urano': {'position': (980, 300), 'font_scale': 0.9, 'color': (255, 255, 0)},
    'Netuno': {'position': (1150, 300), 'font_scale': 0.9, 'color': (255, 0, 0)}
}

for planet, data in planet_data.items():
    position = data['position']
    font_scale = data['font_scale']
    color = data['color']
    cv2.putText(img, planet, (position[0], position[1] + 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, font_scale, color, thickness=2)
cv2.imshow("Sistema Solar", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
