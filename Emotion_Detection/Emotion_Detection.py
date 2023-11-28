from deepface import DeepFace
import cv2

def emotion():
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

def age():
    # Initialize the video capture object
    cap = cv2.VideoCapture(0)

    while True:
        # Capture the current frame
        ret, frame = cap.read()

        if not ret:
            break

        # Analyze the frame using DeepFace
        try:
            results = DeepFace.analyze(frame, actions=['age'], enforce_detection=False)

            # Extract the age from the results
            age = results[0]['age']

            # Display the age on the frame
            cv2.putText(frame, str(age), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        except ValueError as e:
            print(f"Erro: {e}")

            # Display an error message if no face is detected
            cv2.putText(frame, "Não detectado", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        # Display the frame
        cv2.imshow('Emotion Detection', frame)

        # Check for the 'q' key to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Close the video capture object and destroy all windows
    cap.release()
    cv2.destroyAllWindows()

def gender():
    # Initialize the video capture object
    cap = cv2.VideoCapture(0)

    while True:
        # Capture the current frame
        ret, frame = cap.read()

        if not ret:
            break

        # Analyze the frame using DeepFace
        try:
            results = DeepFace.analyze(frame, actions=['gender'], enforce_detection=False)

            # Extract the gender from the results
            gender = results[0]['gender']

            # Display the gender on the frame
            cv2.putText(frame, gender, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        except ValueError as e:
            print(f"Erro: {e}")

            # Display an error message if no face is detected
            cv2.putText(frame, "Não detectado", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        # Display the frame
        cv2.imshow('Gender Detection', frame)

        # Check for the 'q' key to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Close the video capture object and destroy all windows
    cap.release()
    cv2.destroyAllWindows()

def race():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        try:
            results = DeepFace.analyze(frame, actions=[''], enforce_detection=False)

            print(results)

            rece = results[0]['dominant_race']
        
            cv2.putText(frame, race, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        except ValueError as e:
            print(f"Erro: {e}")
            emotion = "Não detectado"

        cv2.imshow('Emotion Detection', frame)  

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
