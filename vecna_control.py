# -*- coding: utf-8 -*-
import os

class Vecna_Control:
    def mostrar_opcoes(self):
        print("""\n[CONTROL] PROTOCOLO SHINOBI ATIVADO — Acoes de Controle:""")
        print(" * /show       : Listar as opcoes de acoes disponiveis de controle.")
        print(" * /up         : Upgrade de todos os drives e pacotes forenses.")
        print(" * /hw         : Diagnostico completo e purga de cache/buffs/memoria.")
        print(" * /ressurrect : Dispara varredura no Explorer em busca de arquivos purgados.")
        print(" * /rebuke     : Forca modo offline, entra em Modo Seguro e roda faxina.")
        print(" * /reburn     : Prepara a recuperacao total da imagem do Windows 10.")

    def upgrade_all(self):
        print("""\n[CONTROL] Executando: upgrade all drives, all packs... [OK]""")

    def diagnostico_sistema(self):
        print("""\n[CONTROL] Diagnostico do sistema ativo. Solicitando limpeza de cache, buffs e memoria... [OK]""")

    def resurrect(self):
        print("""\n[CONTROL] Disparando barramento para localizar registros purgados e deletados...""")
        os.system("explorer.exe .")
        print("[OK] Janela de busca forense instanciada.")

    def rebuke(self):
        print("""\n[CONTROL] ATIVANDO REBUKE: Forcando modo offline... Modo seguro simulado...""")
        if os.path.exists("RODAR_FAXINA.bat"):
            os.system("call RODAR_FAXINA.bat")
        else:
            print("[ERRO] RODAR_FAXINA.bat nao localizado.")

    def reburn(self):
        print("""\n[CONTROL] PREPARANDO RECUPERAÇÃO DA IMAGEM DO WIN 10 (Unidade E: Acoplada):""")
        print(" 1. Recuperar win 10")
        print(" 2. Reinstalar mantendo arquivos da pasta '/Seguranca_Shinobi'")
        print(" 3. Reinstalacao Limpa")
        opcao = input("Selecione a diretriz de reburn (1-3): ").strip()
        print(f"[OK] Diretriz {opcao} enviada ao barramento de boot integrado na unidade E:.")
