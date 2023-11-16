from deepface import DeepFace
import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    try:
        results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        print(results)

        emotion = results[0]['dominant_emotion']

        cv2.putText(frame, emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    except ValueError as e:
        print(f"Erro: {e}")
        emotion = "Não detectado"

    cv2.imshow('Emotion Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
