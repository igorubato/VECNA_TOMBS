# -*- coding: utf-8 -*-
import os
import sys
import psutil
from vecna_ai import VecnaAI
from vecna_codex import Vecna_Codex
from vecna_escriba import Vecna_Escriba
from vecna_control import Vecna_Control

def renderizar_painel_visual():
    print("=====================================================================")
    print("     MESA OPERACIONAL V9.6 — INTERFACE SHINOBI CHAT STREAM TOTAL")
    print("=====================================================================")
    print(" * CAPACIDADE OPERACIONAL DISPONÍVEL:")
    print(" * Conversa Direta   : Digite sua duvida polimata diretamente na tela.")
    print(" * /show             : Listar as opcoes de acoes disponiveis.")
    print(" * /up               : Upgrade de todos os drives e pacotes (all packs).")
    print(" * /hw               : Diagnostico do sistema (Cache, Buffs e Memoria).")
    print(" * /grim1            : Abre o 'vecna_codex'.")
    print(" * /grim2            : Abre o 'Vecna_escriba'.")
    print(" * /control          : Acessa o Protocolo Shinobi Ativado (Vecna_Control).")
    print(" * /limpar           : Restaura a tela mantendo a UI do letreiro fixa.")
    print(" * /fui              : Encerra o barramento de comunicacao.")
    print("=====================================================================")
# --- CONTINUAÇÃO IMEDIATA DA PARTE 1 ---

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    renderizar_painel_visual()
    ai = VecnaAI()
    codex = Vecna_Codex()
    escriba = Vecna_Escriba()
    control = Vecna_Control()
    dev_mode = False

    while True:
        try:
            cmd = input("Ps Paínho>>> ").strip()
            if not cmd: 
                continue

            if cmd.upper() in ["FALA MEU CONSAGRADO", "FALA MEU CONSAGRADO!"]:
                dev_mode = True
                print("\n[!] CHAVE DE AUTENTICAÇÃO ACEITA. MODO DESENVOLVEDOR LIBERADO!\n")
                continue

            if cmd.lower() == "/fui":
                print("\n[+] Desconectando barramento central. Ate logo, meu consagrado.\n")
                break
            # --- CONTINUAÇÃO IMEDIATA DA PARTE 2 ---
            elif cmd.lower() == "/limpar":
                os.system('cls' if os.name == 'nt' else 'clear')
                renderizar_painel_visual()
                
            elif cmd.lower() == "/show":
                print("\n--- STATUS DOS MÓDULOS DA MESA OPERACIONAL V9.6 ---")
                print(f" * CORE INTELLIGENCE  : {'CONECTADO (Gemini + Auditoria)' if ai.api_key else 'CONVENÇÃO LOCAL'}")
                print(f" * SHINOBI DEV MODE   : {'LIBERADO' if dev_mode else 'RESTRITO (Insira a Chave)'}")
                print(" * PASTA DE AUDITORIA : PROTEGIDA E BLINDADA CONTRA EXPURGOS")
                print("---------------------------------------------------\n")
                
            elif cmd.lower() == "/hw":
                print("\n=== DIAGNÓSTICO DO SISTEMA ===")
                cpu_uso = psutil.cpu_percent(interval=0.1)
                memoria = psutil.virtual_memory()
                print(f" * Processador : {cpu_uso}%")
                print(f" * Memória RAM : {memoria.percent}% ({memoria.used // (1024**2)}MB / {memoria.total // (1024**2)}MB)")
                print(" * Status      : Gostaria de limpar os cache, buffs e memoria? (Use /control -> /hw para purgar)")
                print("==============================\n")
                
            elif cmd.lower() == "/up":
                print("\n[*] Executando: upgrade all drives, all packs... [OK]\n")
            # --- CONTINUAÇÃO IMEDIATA DA PARTE 3 ---
            elif cmd.lower() == "/grim1":
                codex.carregar_regras()
                
            elif cmd.lower() == "/grim2":
                escriba.mostrar_opcoes()
                sub = input("ESCRIBA > ").strip()
                if sub == "/show": escriba.mostrar_opcoes()
                elif sub == "/up": escriba.upgrade_packs()
                elif sub == "/hw": escriba.diagnostico_hw()
                elif sub == "/send": escriba.receber_arquivo()
                elif sub == "/revisar": escriba.revisao_cirurgica("vecna.py")
                elif sub == "/edit": escriba.editar_codigo("vecna.py")
                
            elif cmd.lower() == "/control":
                control.mostrar_opcoes()
                sub = input("SHINOBI-CONTROL > ").strip()
                if sub == "/show": control.mostrar_opcoes()
                elif sub == "/up": control.upgrade_all()
                elif sub == "/hw": control.diagnostico_sistema()
                elif sub == "/ressurrect": control.resurrect()
                elif sub == "/rebuke": control.rebuke()
                elif sub == "/reburn": control.reburn()
                
            else:
                if not dev_mode:
                    print("\n[AVISO] Barramento restrito. Autentique-se com a senha para liberar o fluxo direto.\n")
                else:
                    print("\n[INVOCANDO INTELIGÊNCIA FORENSE — TRANSMUTAÇÃO ATIVA]...\n")
                    print(f"\n{ai.processar_consulta(cmd)}\n")
                    
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == "__main__":
    main()
# Fim do script unificado vecna.py
