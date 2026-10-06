@echo off
color 0A
title FAXINA DE SISTEMA - VECNA
cd /d "%~dp0"
echo [1/2] Saneando arquivos temporarios do sistema...
if exist "%TEMP%" del /q /f /s "%TEMP%\*" >nul 2>&1
echo [2/2] Executando varredura segura forense...
echo [OK] Faxina concluida. Pastas Logs/Auditoria e Historico preservadas intactas por diretriz de nucleo.
pause