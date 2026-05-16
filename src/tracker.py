import datetime

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