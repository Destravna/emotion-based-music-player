import cv2

def detect_emotion(filename, emotionDetector):
    print('finding emotion of this person')
    img_location = 'user_photos/' +  filename
    # img_location = filename
    print(img_location)
    image = cv2.imread(img_location)

    emotion, score = emotionDetector.top_emotion(image)
    if emotion == 'neutral' and score <= 0.7:
        emotions = emotionDetector.detect_emotions(image)[0]['emotions']
        sorted_emotions = sorted(emotions.items(), key=lambda x: x[1])

        print(sorted_emotions)

        emotion = sorted_emotions[len(sorted_emotions) - 2][0]
        score = sorted_emotions[len(sorted_emotions) -2][1]
        return {
            'emotion' : emotion,
            'score' : score
        }

    # print(emotion, score)
    return {
        'emotion' : emotion,
        'score' : score
    }
