@echo off
REM Configurações iniciais
setlocal

REM Defina as pastas de origem e destino
set "pasta_origem=%cd%"
set "pasta_destino=%cd%\exportados"

REM Verifique se o Python está instalado
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python não está instalado. Por favor, instale o Python e tente novamente.
    pause
    exit /b
)

REM Verifique se o pacote deepl está instalado
pip show deepl >nul 2>&1
IF ERRORLEVEL 1 (
    echo O pacote "deepl" não está instalado. Instalando...
    pip install deepl
)

REM Solicitar chave da API do DeepL
set /p api_key=Digite sua chave da API do DeepL:

REM Certifique-se de que a pasta de destino exista
if not exist "%pasta_destino%" mkdir "%pasta_destino%"

REM Execute o script traduzir_srt.py
python traduzir_srt.py "%pasta_origem%" "%pasta_destino%" "%api_key%"

REM Mensagem final
echo Tradução concluída. Os arquivos traduzidos estão em: %pasta_destino%
pause