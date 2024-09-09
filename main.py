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

# Conexão ao portal de gerenciamento usando as credenciais para a API CloudInfra
he.connect(infinity_portal_auth=InfinityPortalAuth(
        client_id=client_id, # O "Client ID"
        access_key=api_key, # A "Secret Key"
        gateway=api_url # A "Authentication URL"
        )) 

# Requisição para receber metadados das policies
print("Requisitando metadados das policies")
#rules_metadata_res = he.policy_general_api.get_all_rules_metadata(header_params={ "x-mgmt-run-as-job": 'off'})
#print(rules_metadata_res.payload)  # Metadados das policies
print("\n-----------------------------------------\n")

# A mesma operação, mas usando um job no background -- o resultado final será enviado quando o job encerrar
rules_metadata_res = he.policy_general_api.get_all_rules_metadata(header_params={ "x-mgmt-run-as-job": 'on'})
print(rules_metadata_res.is_job)  # True
print(rules_metadata_res.payload)  # Metadados das policies
print("\n-----------------------------------------\n")

# Requisição de status de operações de remediação
# Precisa ser job:on
print("Requisitando status de todas as operações de remediação")
remediation_statuses = he.remediation_response_general_api.get_all_remediation_operation_statuses(header_params={ "x-mgmt-run-as-job": 'on'})
print(remediation_statuses.payload)
print("\n-----------------------------------------\n")

# Requisição de dados de vulnerabilidades para gerenciamento
print("Requisitando dados de vulnerabilidades para gerenciamento")
vulnerabilities = he.posture_management_vulnerabilities_api.get_vulnerabilities_data(
    header_params={ "x-mgmt-run-as-job": 'on'}, 
    query_params={"pageSize":2, "offset":0}
)
print(vulnerabilities.payload)
print("\n-----------------------------------------\n")

# Encerramento da sessão
he.disconnect()