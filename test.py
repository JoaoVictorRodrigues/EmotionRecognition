import asyncio
from FaceStudy.FaceStudy import FaceStudy, AsyncFaceStudy

async def result_callback(action_name, result):
    # Custom async callback function to handle the results
    print(f"Custom Async Callback: Dominant {action_name}: {result}")

async def main():
    emotion_study = AsyncFaceStudy('emotion', 'Emotion Study')
    #age_study = AsyncFaceStudy('age', 'Age Study')

    # Run the studies concurrently
    await asyncio.gather(
        emotion_study.run(result_callback),
        #age_study.run(result_callback)
    )

if __name__ == "__main__":
    emotion_analyzer = FaceStudy('emotion', 'Emotion Detection')
    age_analyzer = FaceStudy('age', 'Age Detection')
    gender_analyzer = FaceStudy('gender', 'Gender Detection')
    race_analyzer = FaceStudy('race', 'Race Detection')
    
    emotion_study = AsyncFaceStudy('emotion', 'Emotion Study')
    
    asyncio.run(main())
    # emotion_analyzer.run()
    #age_analyzer.run()
    # gender_analyzer.run()
    # race_analyzer.run()