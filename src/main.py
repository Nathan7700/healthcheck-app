from tracker import MedicationTracker

def main():
    tracker = MedicationTracker()
    print("--- HealthCheck: Organizador de Medicamentos ---")
    
    while True:
        print("\n1. Adicionar Medicamento")
        print("2. Listar Agendamentos")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome do medicamento: ")
            hora = input("Horário (HH:MM): ")
            resultado = tracker.add_medication(nome, hora)
            print(resultado["message"])
            
        elif opcao == "2":
            lista = tracker.list_medications()
            if not lista:
                print("Nenhum medicamento agendado.")
            for med in lista:
                print(f"[{med['time']}] - {med['name']}")
                
        elif opcao == "3":
            print("Saindo... Cuide-se bem!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()