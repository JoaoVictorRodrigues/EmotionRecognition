import asyncio
import cv2
from deepface import DeepFace

class AsyncFaceStudy:
    def __init__(self, analyze_type, window, result_callback=None):
        self.action_name = analyze_type
        self.window_title = window
        self.result_callback = result_callback

    async def analyze(self, frame):
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, self._analyze_sync, frame)
        return result

    def _analyze_sync(self, frame):
        try:
            result = DeepFace.analyze(frame, actions=[self.action_name], enforce_detection=False)
            if self.action_name != 'age':
                return result[0][f'dominant_{self.action_name.lower()}']
            else:
                return result[0][f'{self.action_name.lower()}']
        except ValueError as e:
            print(f"Error: {e}")
            return "Not detected"

    async def run(self):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()

            result = await self.analyze(frame)
            print(f"Dominant {self.action_name}: {result}")

            if self.result_callback:
                # Chama o callback se fornecido
                await self.result_callback(self.action_name, result)

            cv2.putText(frame, str(result), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

            cv2.imshow(self.window_title, frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    # Adicione a função result_callback aqui
    async def result_callback(self, action_name, result):
        print(f"Callback: Dominant {action_name}: {result}")

class SyncFaceStudy:
    def __init__(self, analyze_type, window):
        self.action_name = analyze_type
        self.window_title = window

    def analyze(self, frame):
        try:
            result = DeepFace.analyze(frame, actions=[self.action_name], enforce_detection=False)
            if self.action_name != 'age':
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
