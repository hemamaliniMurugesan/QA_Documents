import json 
from os.path import join, dirname 
from ibm_watson import TextToSpeechV1 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator 
authenticator = IAMAuthenticator('57vBZ7-t_-JNVi2kGD0xBPjtX65rcV-LUW7jxQdhqfVe')
text_to_speech = TextToSpeechV1(authenticator=authenticator)
text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/96c803bc-35d9-42a0-9cda-6e734c6b407a') 
sample = 'welcome to skillup'
with open('D:/sampleaudio_1.mp3','wb') as audio_file:
    res = text_to_speech.synthesize(sample,voice='en-US_AllisonV3Voice',accept='audio/mp3').get_result()
    audio_file.write(res.content)
    