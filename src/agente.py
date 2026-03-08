import pandas as pd
import json
import os

def carregar_dados_joao():
    try:
        # Pega a pasta onde este arquivo (agente.py) está
        pasta_atual = os.path.dirname(__file__)
        
        # Sobe um nível e entra na pasta 'data'
        caminho_transacoes = os.path.join(pasta_atual, '..', 'data', 'transacoes.csv')
        caminho_perfil = os.path.join(pasta_atual, '..', 'data', 'perfil_investidor.json')

        # Carrega os dados reais
        transacoes = pd.read_csv(caminho_transacoes)
        with open(caminho_perfil, 'r', encoding='utf-8') as f:
            perfil = json.load(f)
        
        print(f"✅ Sucesso! Atena acessou os dados de: {perfil['nome']}")
        print(f"✅ Histórico financeiro: {len(transacoes)} transações encontradas.")
        
        return transacoes, perfil
    
    except Exception as e:
        print(f"❌ Erro ao acessar a base de dados: {e}")
        return None, None

if __name__ == "__main__":
    carregar_dados_joao()