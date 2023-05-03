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


#R2
import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator = IAMAuthenticator('9HThaLRjDOC9g5DWsqa_dwlLKO-wEO3LNpCE4PdeTyn3')
assistant = AssistantV2(
    version='2021-06-14',
    authenticator = authenticator
)
assistant.set_service_url('https://api.us-south.assistant.watson.cloud.ibm.com/instances/c88c55e0-32a6-45fe-a77a-0fdcdce11a62')
response = assistant.message_stateless(
    assistant_id='f4a83c84-76e5-43bc-aa6e-a218e51c35a6',
    input={
        'message_type': 'text',
        'text': 'Hello'
    }
).get_result()
print(json.dumps(response, indent=2))

#R3
import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator = IAMAuthenticator('AatpwqFNBQy6px_zJA38q9WFbbpBczaNw_gYnv8UW3NY')
assistant = AssistantV2(
    version='2021-06-14',
    authenticator = authenticator
)
assistant.set_service_url('https://api.us-south.assistant.watson.cloud.ibm.com/instances/9f9c06a3-c213-479d-8996-0fc5e1318bb0')
response = assistant.message_stateless(
    assistant_id='1beaa20c-d894-4363-854a-cbbacd29228b',
    input={
        'message_type': 'text',
        'text': 'Hello'
    }
).get_result()
print(json.dumps(response, indent=2))

#R4
import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator = IAMAuthenticator('J8ihLg4IicJlFaEYwWGls2BzkxGU54ucIhtw-xiHg9BG')
assistant = AssistantV2(
    version='2021-06-14',
    authenticator = authenticator
)
assistant.set_service_url('https://api.us-south.assistant.watson.cloud.ibm.com/instances/b9e7eb5d-1c1a-43af-82bc-317a19f9da13')
response = assistant.message_stateless(
    assistant_id='2baf69c1-81a1-4997-94f0-b20bd818001e',
    input={
        'message_type': 'text',
        'text': 'Hello'
    }
).get_result()
print(json.dumps(response, indent=2))