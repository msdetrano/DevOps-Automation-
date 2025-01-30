import requests

LOG_FILE = "/tmp/teste.log"  # Caminho do log fictício
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/SEU-WEBHOOK"  # Substituir pelo seu webhook

def verificar_logs():
    with open(LOG_FILE, "r") as log:
        linhas = log.readlines()
    
    erros = [linha.strip() for linha in linhas if "ERROR" in linha]  # Remove espaços extras
    
    if erros:
        mensagem = f"🚨 *Erros encontrados:* \n" + "\n".join(erros[-5:])  # Exibe últimos 5 erros
        response = requests.post(SLACK_WEBHOOK_URL, json={"text": mensagem})
        
        if response.status_code == 200:
            print("✅ Alerta enviado com sucesso!")
        else:
            print(f"❌ Erro ao enviar alerta: {response.status_code}")

verificar_logs()
