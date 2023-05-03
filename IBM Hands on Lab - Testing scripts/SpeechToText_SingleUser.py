import json 
from os.path import join, dirname 
from ibm_watson import SpeechToTextV1 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator 
authenticator = IAMAuthenticator('vH41WF6fNXjXBX0_zntz6ttCifWbH_AOG037gM55-l8h') 
speech_to_text = SpeechToTextV1(authenticator=authenticator) 
speech_to_text.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/d35adae7-7e24-48f1-a57b-8c63f1323575') 
with open('sampleaudio.mp3','rb') as audio_file: speech_recognition_results=speech_to_text.recognize(audio = audio_file, content_type='audio/mp3').get_result() 
print(json.dumps(speech_recognition_results, indent=2))