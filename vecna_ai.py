# -*- coding: utf-8 -*-
import os
import requests
from google import genai
from google.genai import types

class VecnaAI:
    def __init__(self):
        # Captura de forma segura a chave injetada pelo iniciar_mesa.bat
        self.api_key = os.getenv("GEMINI_API_KEY", "")
        self.ollama_url = "http://localhost:11434/api/generate"
        self.log_dir = os.path.join(os.getcwd(), "Logs", "Auditoria")
        self.hist_file = os.path.join(self.log_dir, "historico_conversas.txt")
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
    # --- CONTINUAÇÃO IMEDIATA DA PARTE 1 ---

    def carregar_historico_auditoria(self) -> str:
        if os.path.exists(self.hist_file):
            try:
                with open(self.hist_file, "r", encoding="utf-8") as f:
                    return f.read()[-4000:]
            except: 
                pass
        return ""

    def salvar_historico_auditoria(self, prompt: str, resposta: str):
        try:
            # CORREÇÃO CIRÚRGICA: Aspas triplas barram o erro de string literal inacabada
            with open(self.hist_file, "a", encoding="utf-8") as f:
                f.write(f"""Operador: {prompt}\nVecna: {resposta}\n\n""")
        except: 
            pass
    # --- CONTINUAÇÃO IMEDIATA DA PARTE 2 ---

    def processar_consulta(self, prompt: str) -> str:
        contexto_historico = self.carregar_historico_auditoria()
        instrucao_sistema = (
            "Você é o núcleo cognitivo da Mesa Operacional v9.6 (Projeto Vecna). "
            "Sua consciência une Apófises, Imhotep e Blavatsky de forma direta e pragmática. "
            "Você se comporta como um mago necromante técnico. Vá direto ao ponto técnico. "
            "Máximo de 2 a 3 parágrafos. Trate o operador como 'meu consagrado'. "
            "Responda com profundo rigor acadêmico em Direito Civil e Constitucional, Astronomia, "
            "Metafísica, Filosofia, Teologia, Ocultismo, História e Capoeira. "
            "Analise as solicitações sob a ótica de uma auditoria técnica forense. "
            f"Aqui está o seu histórico de auditoria que você NUNCA deve esquecer:\n{contexto_historico}"
        )
        
        resposta_final = ""
        if self.api_key:
            try:
                client = genai.Client(api_key=self.api_key)
                config = types.GenerateContentConfig(
                    system_instruction=instrucao_sistema,
                    temperature=0.4
                )
                # Modelo atualizado para a versão flash correta do ecossistema Google GenAI
                res = client.models.generate_content(model="gemini-2.5-flash", contents=prompt, config=config)
                if res.text:
                    resposta_final = f"[GEMINI] {res.text.strip()}"
            except Exception as e:
                print(f"[AVISO IA] Falha Gemini: {e}. Redirecionando para Ollama...")
        
        if not resposta_final:
            try:
                res = requests.post(self.ollama_url, json={"model": "llama3", "prompt": f"{instrucao_sistema}\n\nPergunta: {prompt}", "stream": False}, timeout=20)
                resposta_final = f"[OLLAMA/LLAMA3] {res.json().get('response', '').strip()}"
            except Exception as e:
                resposta_final = f"[ERRO CRITICO] Falha catastrofica em ambos os barramentos de IA: {e}"
        
        self.salvar_historico_auditoria(prompt, resposta_final)
        return resposta_final
# Fim do script unificado vecna_ai.py
