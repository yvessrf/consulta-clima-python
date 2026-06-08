import os
import csv
from datetime import datetime

def salvar_historico(dados):

    arquivo_existe = os.path.exists("historico_clima.csv")

    with open(
        "historico_clima.csv",
        "a",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        if not arquivo_existe:
            escritor.writerow([
                "cidade",
                "temperatura",
                "umidade",
                "condicao",
                "data_consulta"
            ])

        data_consulta = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        escritor.writerow([
            dados["cidade"],
            dados["temperatura"],
            dados["umidade"],
            dados["condicao"],
            data_consulta
        ])

def mostrar_historico():

    if not os.path.exists("historico_clima.csv"):
        print("Nenhum histórico encontrado.")
        return

    with open(
        "historico_clima.csv",
        "r",
        encoding="utf-8"
    ) as arquivo:

        leitor = csv.DictReader(arquivo)

        print("\n===== HISTÓRICO =====\n")

        for linha in leitor:

            print(
                f"{linha['cidade']} | "
                f"{linha['temperatura']}°C | "
                f"{linha['data_consulta']}"
            )