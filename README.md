# 🔠 Padronização Automática de Campos Personalizados no Bitrix24 🇧🇷  
_(Scroll down for English version 🇺🇸)_

Este projeto foi desenvolvido para **padronizar automaticamente os valores de campos personalizados** em negócios (deals) do Bitrix24, convertendo seus textos para **letras maiúsculas** via API Flask.

---

### ✅ O que ele faz?

- Recebe o ID de um negócio específico no Bitrix24.
- Busca os dados do negócio via API.
- Verifica vários campos personalizados configurados.
- Converte os valores texto desses campos para **MAIÚSCULAS**.
- Atualiza o negócio com os valores padronizados.

---

### 🔧 Como funciona?

1. O serviço recebe uma requisição POST na rota `/api/update-crm/<deal_id>`.
2. Consulta o negócio correspondente no Bitrix24.
3. Processa os campos listados em `CRM_CUSTOM_FIELDS`.
4. Converte os valores string para letras maiúsculas.
5. Envia a atualização via API para o Bitrix24.

---

### 🛡️ Segurança

- Integração oficial com API do Bitrix24.
- Uso de variáveis de ambiente para proteger credenciais.
- Timeout nas requisições para maior estabilidade.
- Tratamento de erros detalhado para facilitar manutenção.

---

### 📈 Benefícios para sua empresa

- Garante consistência e padronização dos dados no CRM.
- Evita falhas em automações que dependem do formato dos textos.
- Facilita relatórios e análises com dados limpos e uniformes.

> Quer implementar essa automação no seu Bitrix24? Entre em contato para personalizarmos para você. 😉

---

# 🔠 Automatic Custom Field Standardization in Bitrix24 🇺🇸

This project was created to **automatically standardize custom field values** in Bitrix24 deals by converting text fields to **uppercase** using a Flask API.

---

### ✅ What does it do?

- Receives a specific deal ID in a POST request.
- Fetches deal data from Bitrix24 API.
- Checks various configured custom fields.
- Converts string values to **UPPERCASE**.
- Updates the deal with standardized values.

---

### 🔧 How does it work?

1. Accepts a POST request at `/api/update-crm/<deal_id>`.
2. Retrieves the deal info from Bitrix24.
3. Processes the fields listed in `CRM_CUSTOM_FIELDS`.
4. Converts strings to uppercase.
5. Sends updated fields back to Bitrix24 via API.

---

### 🛡️ Security

- Official Bitrix24 API integration.
- Environment variables keep credentials safe.
- Requests use timeout for reliability.
- Detailed error handling for easy troubleshooting.

---

### 📈 Business Benefits

- Ensures clean and consistent CRM data.
- Prevents errors in automations relying on text format.
- Simplifies reporting and data analysis.

> Want to implement this automation in your Bitrix24? Contact us to customize it for your needs. 😉
