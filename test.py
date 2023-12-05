from FaceStudy.FaceStudy import FaceStudy

if __name__ == "__main__":
    emotion_analyzer = FaceStudy('emotion', 'Emotion Detection')
    age_analyzer = FaceStudy('age', 'Age Detection')
    gender_analyzer = FaceStudy('gender', 'Gender Detection')
    race_analyzer = FaceStudy('race', 'Race Detection')

    emotion_analyzer.run()
    # age_analyzer.run()  
    # gender_analyzer.run()
    # race_analyzer.run()