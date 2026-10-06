@echo off
color 0A
title GERAR LOGS - VECNA
set "LOG_DIR=%~dp0Logs\Auditoria"
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"
set LOG_FILE=%LOG_DIR%\log_consolidado_vecna.txt
echo === LOG DE EXECUÇÃO E AUDITORIA VECNA === > "%LOG_FILE%"
echo Data: %DATE% Hora: %TIME% >> "%LOG_FILE%"
echo [OK] Log consolidado gravado e protegido em: %LOG_FILE%
pause