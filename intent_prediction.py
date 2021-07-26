import requests
import os
import csv


def get_predictions():
    api_string = "http://localhost:5005/model/parse?token=rasa123"

    os.remove('final.csv')

    with open('final.csv', 'a', newline='') as newfile:
        testwriter = csv.writer(newfile)
        testwriter.writerow(["Test Sentence", "Intent Prediction", "Prediction Confidence"])

    with open('Test_DataSet.csv', newline='') as testfile:
        testreader = csv.reader(testfile, delimiter=',')
        for row in testreader:
            json_str = {"text": row}
            prediction_raw = requests.post(api_string, json=json_str)
            prediction_text = prediction_raw.json()['text']
            prediction_intent = prediction_raw.json()['intent']['name']
            prediction_conf = prediction_raw.json()['intent']['confidence']

            with open('final.csv', 'a', newline='') as newfile:
                testwriter = csv.writer(newfile)
                testwriter.writerow([prediction_text, prediction_intent, prediction_conf])


get_predictions()
