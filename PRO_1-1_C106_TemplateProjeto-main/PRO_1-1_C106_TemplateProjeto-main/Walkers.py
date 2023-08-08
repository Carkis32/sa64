import cv2


body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')


# Inicie a captura de vídeo para o arquivo de vídeo
cap = cv2.VideoCapture('walking.avi')

# Faça o loop assim que o vídeo for carregado com sucesso
while True:
    cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, frame = cap.read()
    

    # Converta cada quadro em escala de cinza
    
    # Passe o quadro para nosso classificador de corpos
    body_classifier.detectMultiScale()
    
    # Extraia as caixas delimitadoras para quaisquer corpos identificados
    for x, y, w, h in bodies:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if cv2.waitKey(1) == 32: #32 é a barra de espaço
        break

cap.release()
cv2.destroyAllWindows()
