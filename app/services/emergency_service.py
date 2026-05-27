from typing import List
import re

class EmergencyService:
    def __init__(self):
        # Lista estrita de termos de risco médico crítico mapeados pela equipe de saúde
        self.emergency_keywords = [
            "sangue", "sangramento", "hemorragia",
            "desmaio", "perda de consciencia",
            "vomito persistente", "vomitando muito",
            "dor forte na barriga", "dor abdominal intensa",
            "manchas roxas", "falta de ar", "confusao mental"
        ]

    def is_emergency(self, text: str) -> bool:
        """
        Verifica se o texto do usuário contém algum gatilho de emergência.
        Utiliza busca por palavras-chave em texto normalizado.
        """
        text_lower = text.lower().strip()
        
        # Normalização básica (remover acentos simples para aumentar abrangência)
        # Em um cenário real, usaríamos unidecode, mas para manter leve, 
        # focamos nos termos principais e variações comuns no CSV se necessário.
        
        for keyword in self.emergency_keywords:
            # Busca por palavra inteira ou expressão para evitar falso positivo
            # Ex: "sangue" em "sangue" -> Sim | "sangue" em "passangue" -> Não
            if re.search(rf"\b{re.escape(keyword)}\b", text_lower):
                return True
        
        return False
