import threading
import json
import time
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator 
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator 
def speech1():
    authenticator = IAMAuthenticator('vH41WF6fNXjXBX0_zntz6ttCifWbH_AOG037gM55-l8h') 
    speech_to_text = SpeechToTextV1(authenticator=authenticator) 
    speech_to_text.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/d35adae7-7e24-48f1-a57b-8c63f1323575') 
    with open('sampleaudio.mp3','rb') as audio_file: 
        speech_recognition_results=speech_to_text.recognize(audio = audio_file, content_type='audio/mp3').get_result() 
    print(json.dumps(speech_recognition_results, indent=2))


def speech2():
    authenticator = IAMAuthenticator('f-_llJ6bHC0bhv7-lqwzjHJLSxtaLNDFCFoXmDwEdjxf') 
    speech_to_text = SpeechToTextV1(authenticator=authenticator) 
    speech_to_text.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/4ae898be-926f-4cf3-90a7-0072a896788d') 
    with open('sampleaudio.mp3','rb') as audio_file: 
        speech_recognition_results=speech_to_text.recognize(audio = audio_file, content_type='audio/mp3').get_result() 
    print(json.dumps(speech_recognition_results, indent=2))

speech1()
speech2()
