from src.tracker import MedicationTracker

def test_add_medication_success():
    """Teste 1: Verifica se um medicamento é adicionado corretamente."""
    tracker = MedicationTracker()
    result = tracker.add_medication("Dipirona", "08:00")
    assert result["success"] is True
    assert len(tracker.list_medications()) == 1

def test_add_medication_invalid_time():
    """Teste 2: Verifica se o sistema rejeita horários impossíveis."""
    tracker = MedicationTracker()
    result = tracker.add_medication("Vitamina C", "25:60")
    assert result["success"] is False
    assert "Formato de hora inválido" in result["message"]

def test_add_medication_empty_name():
    """Teste 3: Verifica se o sistema impede nomes vazios (Caso limite)."""
    tracker = MedicationTracker()
    result = tracker.add_medication("   ", "10:00")
    assert result["success"] is False
    assert "nome do medicamento é obrigatório" in result["message"]