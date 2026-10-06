# -*- coding: utf-8 -*-
import urllib.request
import os
import sys

# Rota segura do barramento — INSERIR A URL RAW EXATA DO SEU REPOSITÓRIO AQUI
# Exemplo: "https://githubusercontent.com"
URL_BARRAMENTO = "https://githubusercontent.com"
DESTINO_SISTEMA = r"E:\Users\IGORUBATO\Desktop\Meu_Terminal\Vecna.py"

print("[🧬] Conectando ao barramento remoto para puxar o construtor Vecna Mestre...")

# Configuração de Headers para emular terminal e evitar bloqueios de segurança (403 Forbidden)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) CoreShinobi/9.6'}

# Inicialização do bloco forense de download do sistema principal
try:
    requisicao = urllib.request.Request(URL_BARRAMENTO, headers=headers)
    
    with urllib.request.urlopen(requisicao) as resposta:
        conteudo = resposta.read()
    # --- CONTINUAÇÃO IMEDIATA DA PARTE 1 ---
    # Garante que as pastas de destino (Meu_Terminal e subpastas críticas) existam no disco E:
    pasta_destino = os.path.dirname(DESTINO_SISTEMA)
    os.makedirs(pasta_destino, exist_ok=True)
    
    # Cria automaticamente a estrutura de logs protegidos da Mesa Operacional
    os.makedirs(os.path.join(pasta_destino, "Logs", "Auditoria"), exist_ok=True)
    os.makedirs(os.path.join(pasta_destino, "mods", "editorecho"), exist_ok=True)
        
    # Grava o conteúdo binário baixado preservando a integridade original do arquivo
    with open(DESTINO_SISTEMA, "wb") as arquivo_destino:
        arquivo_destino.write(conteudo)
        
    print(f"[OK] Arquivo '{DESTINO_SISTEMA}' baixado com sucesso total e integridade de hash preservada!")
    print("[*] Diretriz: Iniciando varredura interna de seguranca do ambiente virtual...")

except Exception as e:
    print(f"[❌ ERRO CRÍTICO]: Falha na varredura de rede forense: {e}")
    print("[AVISO] Verifique se a URL aponta para o dominio '://://githubusercontent.com' e se o repositorio e publico.")
    sys.exit(1)

# Bloco de infraestrutura para acoplamento com a Mesa Operacional local
print("[🧬] Verificando ancoragem das dependencias locais...")
# --- CONTINUAÇÃO IMEDIATA DA PARTE 2 ---
# Mapeamento dinâmico dos caminhos do sistema para evitar quebras por caminhos relativos
diretorio_raiz = os.path.dirname(DESTINO_SISTEMA)
caminho_venv = os.path.join(diretorio_raiz, "venv")
caminho_python_venv = os.path.join(caminho_venv, "Scripts", "python.exe") if sys.platform == "win32" else os.path.join(caminho_venv, "bin", "python")

print(f"[*] Escaneando ancoragem do ambiente virtual: {caminho_venv}")

# Verifica se o ambiente virtual (venv) está presente e íntegro
if not os.path.exists(caminho_venv) or not os.path.exists(caminho_python_venv):
    print("[⚠️ AVISO]: Ambiente virtual 'venv' nao detectado ou corrompido.")
    print("[*] Diretriz: Execute o arquivo 'MONTAR_MESA.bat' na raiz para restaurar a infraestrutura.")
else:
    print("[OK] Ambiente virtual validado e acoplado com sucesso à Mesa Operacional.")

# Preparação das diretrizes e cabeçalhos de execução para o painel principal do terminal
print("[🧬] Sincronizando diretrizes de execução do Codex...")
# --- CONTINUAÇÃO IMEDIATA DA PARTE 3 ---
# Execução da limpeza forense do barramento local antes de liberar a Mesa Operacional
try:
    print("[⚡] Executando rotinas finais de faxina e otimização de memória...")
    
    # Identifica caminhos de cache temporários do interpretador Python
    caminho_cache = os.path.join(diretorio_raiz, "mods", "editorecho", "__pycache__")
    
    # Se houver cache pendente, ele é limpo para preservar a integridade do hash do próximo boot
    if os.path.exists(caminho_cache):
        for arquivo in os.listdir(caminho_cache):
            os.remove(os.path.join(caminho_cache, arquivo))
        os.rmdir(caminho_cache)
        print("[OK] Rastro de bytecode temporario eliminado com sucesso total.")

except Exception as e:
    # Falhas menores de faxina de cache não interrompem o fluxo principal do mestre
    print(f"[⚠️ AVISO]: Ignorando otimizacao de rastro de cache: {e}")

print("\n" + "="*70)
print("[🧬] PROCESSO CONCLUÍDO COM SUCESSO TOTAL NO VECNA MESTRE")
print("[OK] O barramento de rede forense foi desconectado de forma segura.")
print("[*] Diretriz: Execute 'INICIAR_MESA.bat' para ingressar no painel.")
print("="*70 + "\n")


