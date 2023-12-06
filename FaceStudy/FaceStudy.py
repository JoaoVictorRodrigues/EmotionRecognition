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
            if(self.action_name != 'age'):
                return result[0][f'dominant_{self.action_name.lower()}']
            else:
                return result[0][f'{self.action_name.lower()}']
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
    
    def verify():
        pass
    def find():
        pass
            
    def represent():
        pass

