@echo off
color 0A
title VECNA V9.6 - TERMINAL PRINCIPAL
cd /d "%~dp0"

:: Injeção da Chave de API identificada no barramento
set "GEMINI_API_KEY=AQ.Ab8RN6KgzvJ0cxDR1TSkR3rEQzn0CpGBTswI8jLXPioaPfb-yA"
set "PYTHON_VENV=%~dp0venv\Scripts\python.exe"

if not exist "%PYTHON_VENV%" (
    echo [❌ ERRO] Ambiente virtual nao encontrado. Execute MONTAR_MESA.bat primeiro.
    pause
    exit /b
)

echo [🧬] Inicializando barramento do painel principal na raiz...
:: CORREÇÃO: Executa o script correto diretamente na pasta raiz Meu_Terminal
"%PYTHON_VENV%" vecna.py
pause
