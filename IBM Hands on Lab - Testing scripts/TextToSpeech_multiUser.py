#R1
import json 
from os.path import join, dirname 
from ibm_watson import TextToSpeechV1 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator 
authenticator = IAMAuthenticator('WQfxLhBzduS2C_a2Esrie2qqkJxR7RrxkeOJs3mF5l40')
text_to_speech = TextToSpeechV1(authenticator=authenticator)
text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/9bcf9aff-cad2-48e6-aa19-04148ad76345') 
sample = 'welcome to skillup'
with open('D:/sampleaudio_1.mp3','wb') as audio_file:
    res = text_to_speech.synthesize(sample,voice='en-US_AllisonV3Voice',accept='audio/mp3').get_result()
    audio_file.write(res.content)

#R2
import json 
from os.path import join, dirname 
from ibm_watson import TextToSpeechV1 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator 
authenticator = IAMAuthenticator('40NzLF-ij0GnLYCcW6F53CmWeNj5BfKcYnPFMFywMK1x')
text_to_speech = TextToSpeechV1(authenticator=authenticator)
text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/8801e23f-95ca-48a5-87e7-82e19e41a7fa') 
sample = 'welcome to skillup'
with open('D:/sampleaudio_1.mp3','wb') as audio_file:
    res = text_to_speech.synthesize(sample,voice='en-US_AllisonV3Voice',accept='audio/mp3').get_result()
    audio_file.write(res.content)
    
#R3
import json 
from os.path import join, dirname 
from ibm_watson import TextToSpeechV1 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator 
authenticator = IAMAuthenticator('cvSy0BB342qWhYVI1kPQ6hp8zmTknws2GlEIU6i_9szw')
text_to_speech = TextToSpeechV1(authenticator=authenticator)
text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/579e59d8-9351-46cf-842c-9489e36d9552') 
sample = 'welcome to skillup'
with open('D:/sampleaudio_2.mp3','wb') as audio_file:
    res = text_to_speech.synthesize(sample,voice='en-US_AllisonV3Voice',accept='audio/mp3').get_result()
    audio_file.write(res.content)