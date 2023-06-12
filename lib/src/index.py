import datetime
import csv

def registrar_usuario(usuario, acao):
    timestamp = datetime.datetime.now().strifetime("%Y-%m-%d %H:%M:%S")
    with open('registro.csv', 'a', newline-'') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow([timestamp, usuario, acao])

        def desligar_usuario(usuario)
        # Coloque aqui o código para desligar o usuário no seu sistema (por exemplo, AD).
    # Certifique-se de que você tenha as permissões adequadas para executar essa ação.
    # ...
    # Após desligar o usuário, registre a ação.

      registrar_usuario(usuario, 'desligado')

      def montar_relatorio():
    with open('registro.csv', 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            print(f'Timestamp: {linha[0]}, Usuário: {linha[1]}, Ação: {linha[2]}')