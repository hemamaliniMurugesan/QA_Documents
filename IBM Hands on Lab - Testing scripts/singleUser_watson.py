import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator = IAMAuthenticator('arW1e1SrWlqZ9MoyUF3b6AqW4_LS9ijZ_AeL5RKByhfz')
assistant = AssistantV2(
    version='2021-06-14',
    authenticator = authenticator
)
assistant.set_service_url('https://api.us-south.assistant.watson.cloud.ibm.com/instances/86bfc1d7-0243-475b-aed2-9260a6aa85b4')
response = assistant.message_stateless(
    assistant_id='2d5116c4-a97c-4051-8572-8c2b051fddb5',
    input={
        'message_type': 'text',
        'text': 'Hello'
    }
).get_result()
print(json.dumps(response, indent=2))