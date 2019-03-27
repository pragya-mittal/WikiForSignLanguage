#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import tempfile
import base64
import json
from flask import Flask, render_template, request, jsonify
from watson_developer_cloud import VisualRecognitionV3

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
print UPLOAD_FOLDER
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

visual_recognition = VisualRecognitionV3(version='2018-03-19',
        iam_apikey='C4aEBzQk4Feg_czj94E-joSMX30z_QZLGy5TDarPfVzC')


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    imgdata = request.form['imgData']
    (header, encoded_image) = imgdata.split(',', 1)

    with open('tmp.jpg', 'wb') as f:
        if len(encoded_image) % 4:
            encoded_image += '=' * (4 - len(encoded_image) % 4)
        f.write(base64.b64decode(encoded_image))

    with open('tmp.jpg', 'rb') as images_file:
        classes = visual_recognition.classify(images_file,
                threshold='0.5', classifier_ids='signlanguage_514642511'
                ).get_result()

    print json.dumps(classes, indent=2)
    return jsonify(classes)

if __name__ == '__main__':
    app.run()