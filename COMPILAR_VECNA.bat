@echo off
color 0A
title COMPILAR_VECNA
cd /d "%~dp0"

set "RAIZ_SISTEMA=E:\Users\IGORUBATO\Desktop\Meu_Terminal"
set "PYTHON_VENV=%~dp0venv\Scripts\python.exe"

echo [🧬] Iniciando validacao de ambiente para compilacao do painel...

if not exist "%RAIZ_SISTEMA%" (
    echo [❌ ERRO]: Diretorio base nao encontrado.
    pause
    exit /b
)

if not exist "%PYTHON_VENV%" (
    echo [❌ ERRO]: Ambiente virtual 'venv' nao detectado. Execute MONTAR_MESA.bat primeiro.
    pause
    exit /b
)

echo [🧬] Iniciando varredura e pre-compilacao forense do modulo Vecna...
"%PYTHON_VENV%" -m compileall mods\editorecho

if %errorlevel% equ 0 (
    echo [OK] Compilacao forense concluida com sucesso.
) else (
    echo [❌ ERRO]: Falha critica na compilacao do modulo editorecho.
    pause
    exit /b
)

echo [🧬] Verificando logs e caminhos da Mesa Operacional...
if not exist "%~dp0dist" mkdir "%~dp0dist"
if not exist "%~dp0Logs\Auditoria" mkdir "%~dp0Logs\Auditoria"

echo [*] Sincronizando dependencias internas do ecossistema...
"%PYTHON_VENV%" -m pip install --upgrade pip --quiet

echo [⚡] Executando diretriz final do construtor Vecna...
if exist "mods\editorecho\__pycache__" (
    del /q /s "mods\editorecho\__pycache__" >nul 2>&1
)

echo.
echo ====================================================================
echo [🧬] PROCESSO CONCLUIDO NA MESA OPERACIONAL
echo [OK] O barramento de compilacao foi encerrado com sucesso total.
echo [*] Diretriz: Inicialize via 'iniciar_mesa.bat' para rodar o painel.
echo ====================================================================
echo.
pause
