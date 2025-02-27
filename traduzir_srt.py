import os
import sys
import deepl

def traduzir_arquivos_srt(pasta_origem, pasta_destino, api_key):
    """
    Traduz todos os arquivos .srt em uma pasta e mantém a estrutura de diretórios usando a API do DeepL.

    :param pasta_origem: Caminho para a pasta de origem contendo os arquivos .srt.
    :param pasta_destino: Caminho para a pasta de destino onde os arquivos traduzidos serão salvos.
    :param api_key: Chave da API do DeepL.
    """
    tradutor = deepl.Translator(api_key)

    for root, _, files in os.walk(pasta_origem):
        for file in files:
            if file.endswith('.srt'):
                caminho_arquivo = os.path.join(root, file)
                with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                    conteudo = f.readlines()

                # Processa cada linha para traduzir apenas o texto
                conteudo_traduzido = []
                for linha in conteudo:
                    if linha.strip().isdigit() or "-->" in linha or linha.strip() == "":
                        # Mantém números de sequência, timestamps e linhas em branco
                        conteudo_traduzido.append(linha)
                    else:
                        # Tradução de texto usando o DeepL
                        traducao = tradutor.translate_text(linha.strip(), target_lang='PT-BR')
                        conteudo_traduzido.append(traducao.text + "\n")  # Use .text para acessar o texto traduzido

                # Cria o diretório correspondente na pasta de destino
                subdir = os.path.relpath(root, pasta_origem)
                pasta_saida = os.path.join(pasta_destino, subdir)
                os.makedirs(pasta_saida, exist_ok=True)

                # Salva o arquivo traduzido
                caminho_saida = os.path.join(pasta_saida, file)
                with open(caminho_saida, 'w', encoding='utf-8') as f:
                    f.writelines(conteudo_traduzido)
                print(f"Arquivo traduzido salvo em: {caminho_saida}")

if __name__ == '__main__':
    # Verificar se a chave da API foi fornecida
    if len(sys.argv) != 4:
        print("Uso: python traduzir_srt.py <pasta_origem> <pasta_destino> <api_key>")
        sys.exit(1)

    pasta_origem = sys.argv[1]
    pasta_destino = sys.argv[2]
    api_key = sys.argv[3]
    traduzir_arquivos_srt(pasta_origem, pasta_destino, api_key)
