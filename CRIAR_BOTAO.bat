@echo off
color 0A
title GERAR BOTAO - VECNA V9.6
cd /d "%~dp0"

echo [1/2] Forjando o atalho (botao) do sistema Vecna...
set "VBS_SCRIPT=%TEMP%\criar_botao_vecna.vbs"

echo Set oWS = WScript.CreateObject("WScript.Shell") > "%VBS_SCRIPT%"
echo sLinkFile = oWS.SpecialFolders("Desktop") ^& "\Mesa Vecna V9.6.lnk" >> "%VBS_SCRIPT%"
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> "%VBS_SCRIPT%"
echo oLink.TargetPath = "%~dp0INICIAR_MESA.bat" >> "%VBS_SCRIPT%"
echo oLink.WorkingDirectory = "%~dp0" >> "%VBS_SCRIPT%"
echo oLink.Description = "Terminal Principal da Mesa Operacional Vecna V9.6" >> "%VBS_SCRIPT%"
echo oLink.IconLocation = "cmd.exe, 0" >> "%VBS_SCRIPT%"
echo oLink.Save >> "%VBS_SCRIPT%"

echo [2/2] Injetando botao na Area de Trabalho...
cscript //nologo "%VBS_SCRIPT%"
del "%VBS_SCRIPT%"

echo.
echo [OK] O botao "Mesa Vecna V9.6" foi gerado com sucesso na sua Area de Trabalho!
echo.
echo === COMO FIXAR NA BARRA DE TAREFAS ===
echo 1. Va ate a sua Area de Trabalho.
echo 2. Clique com o botao direito no icone "Mesa Vecna V9.6".
echo 3. Selecione "Fixar na barra de tarefas".
echo ======================================
echo.
pause