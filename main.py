from services.clima import consultar_clima
from utils.csv_handler import salvar_historico, mostrar_historico
from services.validacoes import validar_cidade


def exibir_clima(dados):
    print(f"Cidade: {dados['cidade']}")
    print(f"Temperatura: {dados['temperatura']}°C")
    print(f"Sensação térmica: {dados['sensacao']}°C")
    print(f"Umidade: {dados['umidade']}%")
    print(f"Condição: {dados['condicao']}")

while True:
    
    print("\n===== CONSULTA CLIMA =====")
    print("1 - Consultar clima")
    print("2 - Ver histórico")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        
        cidade = input("Digite o nome da cidade:")
        
        if not validar_cidade(cidade):
            print("Cidade inválida. Por favor, digite um nome de cidade válido.")
            continue

        dados = consultar_clima(cidade)
        
        if not dados:
            print("Não foi possível obter os dados do clima para a cidade informada.")
            continue
        
        exibir_clima(dados)
        
        salvar_historico(dados)
        
        print("Dados do clima salvos no histórico.")
    elif opcao == "2":
        
        mostrar_historico()
        
    elif opcao == "3":
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")