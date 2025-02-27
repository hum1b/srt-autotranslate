
# Tradutor automático usando DeepL API

Este projeto é um tradutor automático que utiliza a API da **DeepL** para traduzir arquivos de legenda no formato `.srt`. Ele foi projetado para facilitar a tradução de múltiplos arquivos de uma vez, salvando os resultados em uma pasta chamada `exportados`. Para simplificar a execução, incluímos um arquivo `.bat` que automatiza todo o processo.

---

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter o seguinte instalado:

- **Python 3.x**: O script foi desenvolvido para Python 3. Se você não tem o Python instalado, baixe e instale a partir do [site oficial](https://www.python.org/).
- **Biblioteca `requests`**: Usada para fazer chamadas HTTP à API. Pode ser instalada via `pip`.

---

## Passo a Passo para Instalar e Executar o Projeto

### 1. Clone o Repositório

Primeiro, clone este repositório para o seu computador:

```bash
git clone https://github.com/hum1b/srt-autotranslate.git
cd srt-autotranslate
```

### 2. Configure o Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv myenv
```

### 3. Instale as Dependências

Ative o ambiente virtual e instale a biblioteca `requests`:

- No Windows:
  ```bash
  myenv\Scripts\activate
  ```
- No macOS/Linux:
  ```bash
  source myenv/bin/activate
  ```

Depois, instale as dependências:

```bash
pip install requests
```

### 4. Configure a API Key

Obtenha sua chave de API da DeepL. Você pode se inscrever para uma chave gratuita ou paga no [site da DeepL](https://www.deepl.com/pro-api). Substitua o valor de `API_KEY` no arquivo `traduzir_srt.py`:

```python
API_KEY = "sua_chave_api_aqui"
```

### 5. Adicione os Arquivos `.srt` à Pasta

Coloque os arquivos de legenda (formato `.srt`) que deseja traduzir na pasta raiz do projeto ou em subpastas. O script é capaz de localizar e traduzir arquivos `.srt` em qualquer nível de subpastas.

### 6. Execute o Projeto Usando o Arquivo `.bat`

No Windows, basta clicar duas vezes no arquivo `executar_traduzir_srt.bat` para executar o tradutor. O arquivo `.bat` fará o seguinte:
1. Ativará o ambiente virtual automaticamente (se não estiver ativado).
2. Solicitará que você insira sua chave de API da DeepL (caso não tenha configurado no script).
3. Percorrerá todos os arquivos `.srt` na pasta raiz e em subpastas.
4. Traduzirá cada arquivo e salvará os resultados em uma pasta chamada `exportados`, mantendo a estrutura de subpastas original.

Se preferir, você também pode executar o arquivo `.bat` diretamente pelo terminal:

```bash
executar_traduzir_srt.bat
```

---

## Como o Arquivo `.bat` Funciona

O arquivo `executar_traduzir_srt.bat` é um script de lote do Windows que automatiza o processo de tradução. Aqui está o que ele faz passo a passo:

1. **Ativação do Ambiente Virtual**:
   - Verifica se o ambiente virtual está ativado. Se não estiver, ele o ativa automaticamente.

2. **Solicitação da Chave de API**:
   - Se a chave de API não estiver configurada no script, ele solicitará que você a insira.

3. **Tradução dos Arquivos `.srt`**:
   - Percorre todos os arquivos `.srt` na pasta raiz e em subpastas.
   - Traduz o conteúdo de cada arquivo usando a API da DeepL.
   - Salva os arquivos traduzidos na pasta `exportados`, mantendo a estrutura de subpastas original.

4. **Finalização**:
   - Exibe uma mensagem de conclusão no terminal.
   - Mantém o terminal aberto para que você possa ver o resultado do processo.

---

## Estrutura do Projeto

Após a execução, a estrutura do projeto ficará assim:

```
srt-autotranslate/
├── myenv/                  # Ambiente virtual
├── exportados/             # Pasta com os arquivos traduzidos (mantendo a estrutura de subpastas)
├── pasta1/                 # Subpasta com arquivos .srt originais
│   ├── arquivo1.srt
│   └── arquivo2.srt
├── pasta2/                 # Outra subpasta com arquivos .srt originais
│   └── arquivo3.srt
├── traduzir_srt.py         # Script Python principal
├── executar_traduzir_srt.bat # Script de lote para execução no Windows
└── README.md               # Este arquivo
```

---

## Personalização

- **Idiomas Suportados**: A DeepL suporta uma ampla variedade de idiomas. Consulte a [documentação oficial da DeepL](https://www.deepl.com/docs-api) para ver a lista completa de idiomas suportados.
- **Interface Gráfica**: Você pode adicionar uma interface gráfica usando bibliotecas como `Tkinter` ou integrar o script em um aplicativo web com `Flask` ou `Django`.

---

## Donate

Se você achou este projeto útil e gostaria de apoiar meu trabalho, considere fazer uma doação no meu **Ko-fi**. Sua contribuição ajuda a manter projetos como este e a criar novas ferramentas incríveis!

[![Donate on Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/hum1b)

---

## Contribuições

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

---

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Contato

Se você tiver dúvidas ou precisar de ajuda, entre em contato:

- **Nome**: Humberto Cabral Padilha
- **Email**: humberto.cabral.padilha@gmail.com
- **GitHub**: [hum1b](https://github.com/hum1b)

---

### Observações sobre a API da DeepL

A API da DeepL é uma das ferramentas de tradução mais precisas disponíveis atualmente. Ela suporta traduções de alta qualidade entre diversos idiomas e é amplamente utilizada em aplicações profissionais. Certifique-se de verificar o [plano de preços](https://www.deepl.com/pro-api) e os limites de uso antes de integrar a API em projetos comerciais.
