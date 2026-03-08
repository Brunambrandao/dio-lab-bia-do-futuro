import os
from dotenv import load_dotenv

# Carrega as variáveis salvas no arquivo .env
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# Puxa a chave de API
API_KEY = os.getenv("GEMINI_API_KEY")

# Validação simples para evitar erros
if not API_KEY:
    print("⚠️ Atenção: Chave de API não encontrada no arquivo .env!")
    