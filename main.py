from chkp_harmony_endpoint_management_sdk import HarmonyEndpoint, InfinityPortalAuth, HarmonyEndpointSDKInfo
import os

def load_configuration():
    client_id = os.getenv('CLIENT_ID')
    api_key = os.getenv('API_SECRET')
    api_url = os.getenv('API_URL')
    return client_id, api_key, api_url


he = HarmonyEndpoint()
client_id, api_key, api_url = load_configuration()

sdk_info: HarmonyEndpointSDKInfo = HarmonyEndpoint.info()
print(sdk_info)

# Connect to management using CloudInfra API credentials
he.connect(infinity_portal_auth=InfinityPortalAuth(
        client_id=client_id, # The "Client ID"
        access_key=api_key, # The "Secret Key"
        gateway=api_url # The "Authentication URL"
        )) 

# Query the API operation
rules_metadata_res = he.policy_general_api.get_all_rules_metadata(header_params={ "x-mgmt-run-as-job": 'off'})
print(rules_metadata_res.payload)  # Your rulebase metadata

# Also you can query this operation using job, no extra logic required, in the background, it will trigger a job and will pull the status till it finish and return the final results. 
rules_metadata_res = he.policy_general_api.get_all_rules_metadata(header_params={ "x-mgmt-run-as-job": 'on'})
print(rules_metadata_res.is_job)  # True
print(rules_metadata_res.payload)  # Your rulebase metadata

# Once finish, disconnect to stop all background session management. 
he.disconnect()