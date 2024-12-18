from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
  "UF_CRM_1697653896576",


CODIGO_BITRIX = os.getenv('CODIGO_BITRIX')
CODIGO_BITRIX_STR = os.getenv('CODIGO_BITRIX_STR')
PROFILE = os.getenv('PROFILE')
BASE_URL_API_BITRIX = os.getenv('BASE_URL_API_BITRIX')

BITRIX_WEBHOOK_URL = f"{BASE_URL_API_BITRIX}/{PROFILE}/{CODIGO_BITRIX}"

# Mapeamento dos campos personalizados do CRM
CRM_CUSTOM_FIELDS = [
  "UF_CRM_1697653896576",
  "UF_CRM_1697762313423",
  "UF_CRM_1697763267151",
  "UF_CRM_1697763906167",
  "UF_CRM_1697764091406",
  "UF_CRM_1697764123510",
  "UF_CRM_1697807340141",
  "UF_CRM_1697807353336",
  "UF_CRM_1697807372536",
  "UF_CRM_1697808018193",
  "UF_CRM_1698688252221",
  "UF_CRM_1698697044148",
  "UF_CRM_1698698407472",
  "UF_CRM_1698698858832",
  "UF_CRM_1698761052502",
  "UF_CRM_1698761151613",
  "UF_CRM_1699368958570",
  "UF_CRM_1699369257531",
  "UF_CRM_1699369424819",
  "UF_CRM_1699375244400",
  "UF_CRM_1699376317370",
  "UF_CRM_1699376523381",
  "UF_CRM_1699452141037",
  "UF_CRM_1699475211222",
  "UF_CRM_1699623587624",
  "UF_CRM_1700239715167",
  "UF_CRM_1700661252544",
  "UF_CRM_1700661275591",
  "UF_CRM_1700661287551",
  "UF_CRM_1700661298591",
  "UF_CRM_1700661314351",
  "UF_CRM_1700663313965",
  "UF_CRM_1700674506092",
  "UF_CRM_656A246C490E8",
  "UF_CRM_1704220651467",
  "UF_CRM_1704746567933",
  "UF_CRM_1706040523430",
  "UF_CRM_1706279998600",
  "UF_CRM_1707505212188",
  "UF_CRM_1708527436550",
  "UF_CRM_1709042046",
  "UF_CRM_1713214941",
  "UF_CRM_1713556388376",
  "UF_CRM_1714142479",
  "UF_CRM_1714143720",
  "UF_CRM_1715262825761",
  "UF_CRM_1715364357059",
  "UF_CRM_1715623261063",
  "UF_CRM_1715979400253",
  "UF_CRM_1715979433863",
  "UF_CRM_1715979454408",
  "UF_CRM_1716823850",
  "UF_CRM_1716824098",
  "UF_CRM_1717710167",
  "UF_CRM_1717782237025",
  "UF_CRM_1717782566165",
  "UF_CRM_1719408744616",
  "UF_CRM_1720189786452",
  "UF_CRM_1720209627527",
  "UF_CRM_1720209658075",
  "UF_CRM_1720209709775",
  "UF_CRM_1721221888184",
  "UF_CRM_1722618036",
  "UF_CRM_1722948609",
  "UF_CRM_1723039822",
  "UF_CRM_1723234517934",
  "UF_CRM_1723557410",
  "UF_CRM_1724090639394",
  "UF_CRM_1724090810990",
  "UF_CRM_1724091021655",
  "UF_CRM_1724091093006",
  "UF_CRM_1724091924045",
  "UF_CRM_1724096872",
  "UF_CRM_1724173397",
  "UF_CRM_1724173431",
  "UF_CRM_1724173468",
  "UF_CRM_1724173498",
  "UF_CRM_1724173536",
  "UF_CRM_1724174693",
  "UF_CRM_1724298927",
  "UF_CRM_1724419291",
  "UF_CRM_1725544974",
  "UF_CRM_1725563653",
  "UF_CRM_1725913768700",
  "UF_CRM_1725913938604",
  "UF_CRM_1725913962585",
  "UF_CRM_1725914211188",
  "UF_CRM_1725914243672",
  "UF_CRM_1726073260619",
  "UF_CRM_1726073327213",
  "UF_CRM_1726073380230",
  "UF_CRM_1726162708276",
  "UF_CRM_1726162757261",
  "UF_CRM_1726782459459",
  "UF_CRM_1726782549702",
  "UF_CRM_1726782581466",
  "UF_CRM_1726788668",
  "UF_CRM_1726842814441",
  "UF_CRM_1726842828171",
  "UF_CRM_1726842871219",
  "UF_CRM_1726842926368",
  "UF_CRM_1726842939868",
  "UF_CRM_1726843039677",
  "UF_CRM_1726843053851",
  "UF_CRM_1726843072587",
  "UF_CRM_1726843092562",
  "UF_CRM_1726856444600",
  "UF_CRM_1726856458900",
  "UF_CRM_1727190530486",
  "UF_CRM_1727291634592",
  "UF_CRM_1727296926",
  "UF_CRM_1727470306288",
  "UF_CRM_1727470319248",
  "UF_CRM_1727470370943",
  "UF_CRM_1727470395228",
  "UF_CRM_1727728888013",
  "UF_CRM_1727728899847",
  "UF_CRM_1727728914704",
  "UF_CRM_1727728926705",
  "UF_CRM_1727729045180",
  "UF_CRM_1727729061662",
  "UF_CRM_1727729073767",
  "UF_CRM_1727729083230",
  "UF_CRM_1727729121304",
  "UF_CRM_1727729146263",
  "UF_CRM_1727729156906",
  "UF_CRM_1727729166109",
  "UF_CRM_1727729259751",
  "UF_CRM_1727729268841",
  "UF_CRM_1727729277541",
  "UF_CRM_1727729286578",
  "UF_CRM_1727729366137",
  "UF_CRM_1727729375564",
  "UF_CRM_1727729386455",
  "UF_CRM_1727729395252",
  "UF_CRM_1727729437611",
  "UF_CRM_1727729445981",
  "UF_CRM_1727729457831",
  "UF_CRM_1727729473049",
  "UF_CRM_1727729525055",
  "UF_CRM_1727729544328",
  "UF_CRM_1727729554242",
  "UF_CRM_1727729565080",
  "UF_CRM_1727791901",
  "UF_CRM_1727974668",
  "UF_CRM_1727981690",
  "UF_CRM_1727983669",
  "UF_CRM_1727986325",
  "UF_CRM_1727986348",
  "UF_CRM_1728321160",
  "UF_CRM_1728496932",
  "UF_CRM_1728569724",
  "UF_CRM_1728648736744",
  "UF_CRM_1729017188576",
  "UF_CRM_1729277245859",
  "UF_CRM_1730916139",
  "UF_CRM_1731010515",
  "UF_CRM_1731360883153"
]

@app.route('/api/update-crm/<int:deal_id>', methods=['POST'])
def update_crm(deal_id):
    try:
        # Passo 1: GET no card do CRM
        get_url = f"{BITRIX_WEBHOOK_URL}/crm.deal.get.json?ID={deal_id}"
        get_response = requests.get(get_url)
        
        if get_response.status_code != 200:
            return jsonify({"error": "Erro ao buscar o Negócio.", "details": get_response.json()}), 500
        
        deal_data = get_response.json().get('result')
        
        if not deal_data:
            return jsonify({"error": "Negócio não encontrado."}), 404
        
        # Passo 2: Transformar os valores dos campos personalizados em maiúsculas
        fields_to_update = {}
        for field, value in deal_data.items():
            if field in CRM_CUSTOM_FIELDS and isinstance(value, str):
                fields_to_update[field] = value.upper()
        
        if not fields_to_update:
            return jsonify({"message": "Nenhum campo para atualizar."})
        
        # Passo 3: POST para atualizar o card no CRM
        update_url = f"{BITRIX_WEBHOOK_URL}/crm.deal.update.json?ID={deal_id}"
        data = {
            'fields': fields_to_update
        }
        
        update_response = requests.post(update_url, json=data)
        
        if update_response.status_code != 200:
            return jsonify({"error": "Falha ao atualizar o Negócio.", "details": update_response.json()}), 500
        
        return jsonify({"message": "Negócio atualizado com sucesso!", "updated_fields": fields_to_update})
    
    except Exception as e:
        return jsonify({"error": "Ocorreu um erro no servidor.", "details": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=49)