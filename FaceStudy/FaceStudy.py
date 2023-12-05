from deepface import DeepFace
import cv2
import time

class FaceStudy:
    def __init__(self,analyze_type,window):
        self.action_name = analyze_type
        self.window_title = window

    def analyze(self, frame):
        try:
            result = DeepFace.analyze(frame, actions=[self.action_name], enforce_detection=False)
            #time.sleep(0.1)
            return result[0][f'dominant_{self.action_name.lower()}']
        except ValueError as e:
            print(f"Error: {e}")
            return "Not detected"
        
    def run(self):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()

            result = self.analyze(frame)
            print(f"Dominant {self.action_name}: {result}")
            cv2.putText(frame, str(result), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

            cv2.imshow(self.window_title, frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    """ def analyze_emotion():
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            try:
                results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                emotion = results[0]['dominant_emotion']
                print(f"Dominant Emotion: {emotion}")
                cv2.putText(frame, emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            except ValueError as e:
                print(f"Erro: {e}")
                emotion = "Não detectado"

            cv2.imshow('Emotion Detection', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def analyze_age():
        # Initialize the video capture object
        cap = cv2.VideoCapture(0)

        while True:
            # Capture the current frame
            ret, frame = cap.read()

            # Analyze the frame using DeepFace
            try:
                results = DeepFace.analyze(frame, actions=['age'], enforce_detection=False)

                # Extract the age from the results
                age = results[0]['age']
                print(f"Estimated Age: {age}")
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

    def analyze_gender():
        # Initialize the video capture object
        cap = cv2.VideoCapture(0)

        while True:
            # Capture the current frame
            ret, frame = cap.read()
            # Analyze the frame using DeepFace
            try:
                results = DeepFace.analyze(frame, actions=['gender'], enforce_detection=False)

                # Extract the gender from the results
                gender = results[0]['dominant_gender']
                print(f"Dominant gender: {gender}")
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

    def analyze_race():
        import cv2
        from deepface import DeepFace

        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()

            try:
                results = DeepFace.analyze(frame, actions=['race'], enforce_detection=False)  
                
                race = results[0]['dominant_race'] 
                print(f"Dominant Race: {race}")
                cv2.putText(frame, race, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
            except ValueError as e:
                print(f"Erro: {e}")
                race = "Não detectado"  # Reassign race variable in the exception block

            cv2.imshow('Raça Detection', frame)  # Correct window title

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
 """

