from EmotionDetection.emotion_detection import emotion_detector 
import unittest

class EmotionDetection (unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector("I am glad this happened")
        dominant_value = result_1.split("'dominant_emotion':")[-1].strip(" '}")
        self.assertEqual(dominant_value, 'joy')
        
        result_2 = emotion_detector("I am really mad about this")
        dominant_value = result_2.split("'dominant_emotion':")[-1].strip(" '}")
        self.assertEqual(dominant_value, 'anger')

        result_3 = emotion_detector("I feel disgusted just hearing about this")
        dominant_value = result_3.split("'dominant_emotion':")[-1].strip(" '}")
        self.assertEqual(dominant_value, 'disgust')

        result_4 = emotion_detector("I am so sad about this")
        dominant_value = result_4.split("'dominant_emotion':")[-1].strip(" '}")
        self.assertEqual(dominant_value, 'sadness')

        result_5 = emotion_detector("I am really afraid that this will happen")
        dominant_value = result_5.split("'dominant_emotion':")[-1].strip(" '}")
        self.assertEqual(dominant_value, 'fear')

unittest.main()
