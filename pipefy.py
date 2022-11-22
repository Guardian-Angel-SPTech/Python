import requests

url = "https://api.pipefy.com/graphql"

variavel = "Luis"
variavel2 = "Outros"

payload = {"query": "mutation{ createCard( input: { pipe_id: \"302636936\" fields_attributes: [     {field_id: \"qual_o_assunto_do_seu_pedido\", field_value: \"Testar geração de card2\"}   {field_id: \"informa_es_do_solicitante\", field_value: \"603834395\"}   {field_id: \"tipo\", field_value: \"%s\"}   {field_id: \"mais_informa_es\", field_value: \"%s\"} ] } ) {clientMutationId card {id title }}}" % (variavel2, variavel)} 

headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7ImlkIjozMDIwODAyNDQsImVtYWlsIjoibHVpcy5udW5lc0BzcHRlY2guc2Nob29sIiwiYXBwbGljYXRpb24iOjMwMDIxNDI1MH19.ib-5cnqvW9NHv5rzehMgfaxIGE3iGxOsuBGs8CLAGvgQcoBBBYeC6up3lMwD-ymn5SCmZAIJnQ9Qp_ZoggN-DQ",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)