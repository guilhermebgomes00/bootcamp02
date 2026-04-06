from datetime import datetime

class ControladorMedicamentos:
    def __init__(self):
        self.medicamentos = []

    def adicionar_medicamento(self, nome, dosagem, horario, frequencia):
        """
        Adiciona um novo medicamento à lista de controle.
        
        Args:
            nome: Nome do medicamento
            dosagem: Dosagem (ex: "500mg", "1 comprimido")
            horario: Horário de ingestão (ex: "08:00", "14:30")
            frequencia: Frequência de ingestão (ex: "2x ao dia", "3x ao dia", "1x ao dia")
        """
        if not nome or not dosagem or not horario or not frequencia:
            raise ValueError("Todos os campos são obrigatórios.")
        
        try:
            # Validar formato do horário
            datetime.strptime(horario, "%H:%M")
        except ValueError:
            raise ValueError("Horário inválido. Use o formato HH:MM (ex: 08:00)")
        
        medicamento = {
            "nome": nome,
            "dosagem": dosagem,
            "horario": horario,
            "frequencia": frequencia,
            "tomado_hoje": False,
            "data_ultima_ingestao": None
        }
        self.medicamentos.append(medicamento)
        return f"Medicamento '{nome}' adicionado com sucesso!"

    def listar_medicamentos(self):
        """Lista todos os medicamentos cadastrados."""
        return self.medicamentos

    def marcar_como_tomado(self, indice):
        """Marca um medicamento como tomado."""
        if 0 <= indice < len(self.medicamentos):
            self.medicamentos[indice]["tomado_hoje"] = True
            self.medicamentos[indice]["data_ultima_ingestao"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            return True
        return False

    def desmarcar_medicamento(self, indice):
        """Desmarca um medicamento como tomado."""
        if 0 <= indice < len(self.medicamentos):
            self.medicamentos[indice]["tomado_hoje"] = False
            return True
        return False

    def remover_medicamento(self, indice):
        """Remove um medicamento da lista."""
        if 0 <= indice < len(self.medicamentos):
            nome = self.medicamentos[indice]["nome"]
            self.medicamentos.pop(indice)
            return f"Medicamento '{nome}' removido com sucesso!"
        return "Medicamento não encontrado."

    def obter_proximos_horarios(self):
        """Retorna os próximos horários de medicamentos a serem tomados."""
        agora = datetime.now()
        hora_atual = agora.strftime("%H:%M")
        
        proximos = []
        for i, med in enumerate(self.medicamentos):
            if med["horario"] > hora_atual and not med["tomado_hoje"]:
                proximos.append((i, med))
        
        return sorted(proximos, key=lambda x: x[1]["horario"])

    def obter_medicamentos_atrasados(self):
        """Retorna medicamentos que deveriam ter sido tomados e ainda não foram."""
        agora = datetime.now()
        hora_atual = agora.strftime("%H:%M")
        
        atrasados = []
        for i, med in enumerate(self.medicamentos):
            if med["horario"] <= hora_atual and not med["tomado_hoje"]:
                atrasados.append((i, med))
        
        return sorted(atrasados, key=lambda x: x[1]["horario"], reverse=True)

    def resetar_dia(self):
        """Reseta o status de todos os medicamentos para o novo dia."""
        for med in self.medicamentos:
            med["tomado_hoje"] = False


def menu():
    controlador = ControladorMedicamentos()
    
    while True:
        print("\n" + "="*50)
        print("   CONTROLE DE MEDICAMENTOS PARA IDOSOS")
        print("="*50)
        print("1. Adicionar Medicamento")
        print("2. Listar Medicamentos")
        print("3. Marcar Medicamento como Tomado")
        print("4. Desmarcar Medicamento")
        print("5. Remover Medicamento")
        print("6. Ver Próximos Horários")
        print("7. Ver Medicamentos Atrasados")
        print("8. Resetar Dia")
        print("9. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            try:
                nome = input("Nome do medicamento: ").strip()
                dosagem = input("Dosagem (ex: 500mg, 1 comprimido): ").strip()
                horario = input("Horário (HH:MM, ex: 08:00): ").strip()
                frequencia = input("Frequência (ex: 2x ao dia, 3x ao dia): ").strip()
                
                print(controlador.adicionar_medicamento(nome, dosagem, horario, frequencia))
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            medicamentos = controlador.listar_medicamentos()
            if not medicamentos:
                print("Nenhum medicamento cadastrado.")
            else:
                print("\n" + "-"*50)
                for i, med in enumerate(medicamentos):
                    status = "TOMADO" if med["tomado_hoje"] else "⏰ PENDENTE"
                    print(f"\n{i}. [{status}] {med['nome']}")
                    print(f"   Dosagem: {med['dosagem']}")
                    print(f"   Horário: {med['horario']}")
                    print(f"   Frequência: {med['frequencia']}")
                    if med["data_ultima_ingestao"]:
                        print(f"   Última ingestão: {med['data_ultima_ingestao']}")
                print("\n" + "-"*50)

        elif opcao == "3":
            medicamentos = controlador.listar_medicamentos()
            if not medicamentos:
                print("Nenhum medicamento cadastrado.")
            else:
                try:
                    indice = int(input("Digite o número do medicamento para marcar como tomado: "))
                    if controlador.marcar_como_tomado(indice):
                        print("Medicamento marcado como tomado!")
                    else:
                        print("Medicamento não encontrado.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")

        elif opcao == "4":
            medicamentos = controlador.listar_medicamentos()
            if not medicamentos:
                print("Nenhum medicamento cadastrado.")
            else:
                try:
                    indice = int(input("Digite o número do medicamento para desmarcar: "))
                    if controlador.desmarcar_medicamento(indice):
                        print("Medicamento desmarcado!")
                    else:
                        print("Medicamento não encontrado.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")

        elif opcao == "5":
            medicamentos = controlador.listar_medicamentos()
            if not medicamentos:
                print("Nenhum medicamento cadastrado.")
            else:
                try:
                    indice = int(input("Digite o número do medicamento para remover: "))
                    print(controlador.remover_medicamento(indice))
                except ValueError:
                    print("Entrada inválida. Digite um número.")

        elif opcao == "6":
            proximos = controlador.obter_proximos_horarios()
            if not proximos:
                print("Nenhum medicamento pendente para hoje!")
            else:
                print("\nPRÓXIMOS MEDICAMENTOS A SEREM TOMADOS:")
                print("-"*50)
                for i, (indice, med) in enumerate(proximos, 1):
                    print(f"{i}. [{med['horario']}] {med['nome']} - {med['dosagem']}")
                print("-"*50)

        elif opcao == "7":
            atrasados = controlador.obter_medicamentos_atrasados()
            if not atrasados:
                print("Nenhum medicamento atrasado!")
            else:
                print("\nMEDICAMENTOS ATRASADOS:")
                print("-"*50)
                for i, (indice, med) in enumerate(atrasados, 1):
                    print(f"{i}. [{med['horario']}] {med['nome']} - {med['dosagem']}")
                print("-"*50)

        elif opcao == "8":
            controlador.resetar_dia()
            print("Dia resetado! Todos os medicamentos marcados como pendentes.")

        elif opcao == "9":
            print("\nAté logo! Cuide-se bem!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
