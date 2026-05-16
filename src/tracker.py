import datetime
import requests

class MedicationTracker:
    def __init__(self):
        self.medications = []

    def add_medication(self, name, time_str):
        """Adiciona um medicamento com validação de hora e nome."""
        if not name.strip():
            return {"success": False, "message": "Erro: O nome do medicamento é obrigatório."}

        try:
            datetime.datetime.strptime(time_str, "%H:%M")
        except ValueError:
            return {"success": False, "message": "Erro: Formato de hora inválido. Use HH:MM (ex: 08:30)."}

        med_entry = {"name": name, "time": time_str}
        self.medications.append(med_entry)
        return {"success": True, "message": f"Sucesso: {name} agendado para às {time_str}."}

    def list_medications(self):
        """Retorna a lista de medicamentos cadastrados."""
        return self.medications

    def buscar_endereco_por_cep(self, cep):
        """Busca o endereço de um paciente utilizando a API do ViaCEP."""
        cep = str(cep).replace("-", "").replace(" ", "")
        
        if len(cep) != 8 or not cep.isdigit():
            return {"success": False, "message": "Erro: CEP inválido. Deve conter 8 dígitos."}

        url = f"https://viacep.com.br/ws/{cep}/json/"
        
        try:
            resposta = requests.get(url)
            if resposta.status_code == 200:
                dados = resposta.json()
                if "erro" in dados:
                    return {"success": False, "message": "Erro: CEP não encontrado."}
                return {"success": True, "data": dados}
            else:
                return {"success": False, "message": "Erro ao conectar com a API de CEP."}
        except requests.exceptions.RequestException:
            return {"success": False, "message": "Erro de conexão com a internet."}