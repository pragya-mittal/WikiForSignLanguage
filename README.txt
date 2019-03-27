## How to run (Linux)
Install all the dependencies like python, flask, watson_developer_cloud etc, using pip command
python server.py 


IBM watson api documentation
https://console.bluemix.net/docs/services/visual-recognition/tutorial-custom-classifier.html#tutorial-custom-classifier

Sample API's
To create a new classifier
curl -X POST -u "apikey:C4aEBzQk4Feg_czj94E-joSMX30z_QZLGy5TDarPfVzC" --form "one_positive_examples=@Images/1.zip" \
 --form "two_positive_examples=@Images/2.zip" \
 --form "three_positive_examples=@Images/3.zip" \
 --form "name=sign language" \
 "https://gateway.watsonplatform.net/visual-recognition/api/v3/classifiers?version=2018-03-19"

To check classifier is ready for queries
curl -X GET -u "apikey:C4aEBzQk4Feg_czj94E-joSMX30z_QZLGy5TDarPfVzC" \
"https://gateway.watsonplatform.net/visual-recognition/api/v3/classifiers/signlanguage_514642511?version=2018-03-19"

To query classifier
curl -X POST -u "apikey:C4aEBzQk4Feg_czj94E-joSMX30z_QZLGy5TDarPfVzC" \
--form "images_file=@TEST.jpg" \
--form "classifier_ids=signlanguage_514642511,default" \
"https://gateway.watsonplatform.net/visual-recognition/api/v3/classify?version=2018-03-19"

To run the server use the following command :
python3 server.py

To install flask, pip and required packages use the following commands :
sudo apt install python3-pip
sudo pip install Flask
sudo pip install watson-developer-cloud
Note : In case you have different version of pip use that version eg : pip3
