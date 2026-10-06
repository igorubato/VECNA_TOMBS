@echo off
color 0A
title MONTAR_MESA - VECNA
cd /d "%~dp0"

echo [🧬] Estabelecendo diretórios da Mesa Operacional...
if not exist "mods\editor" mkdir "mods\editor"
if not exist "Logs\Auditoria" mkdir "Logs\Auditoria"

if not exist "venv" (
    echo [*] Criando ambiente virtual venv...
    python -m venv venv
)

:: CORREÇÃO: Caractere 'a' restaurado para ativação correta do venv
call "%~dp0venv\Scripts\activate.bat"

echo [*] Atualizando gerenciador pip e instalando dependencias...
python -m pip install --upgrade pip --quiet
python -m pip install -r requirements.txt

echo.
echo ====================================================================
echo [OK] MESA OPERACIONAL MONTADA COM SUCESSO! DEPENDENCIAS PRONTAS.
echo ====================================================================
echo.
pause
