import requests

def buscar_endereco_por_cep(cep):
    """Busca o endereço de um paciente utilizando a API do ViaCEP."""
    cep = str(cep).replace("-", "").replace(" ", "")
    if len(cep) != 8 or not cep.isdigit():
        return {"success": False, "message": "Erro: CEP inválido."}
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            if "erro" in dados:
                return {"success": False, "message": "Erro: CEP não encontrado."}
            return {"success": True, "data": dados}
        return {"success": False, "message": "Erro ao conectar com a API de CEP."}
    except:
        return {"success": False, "message": "Erro de conexão."}