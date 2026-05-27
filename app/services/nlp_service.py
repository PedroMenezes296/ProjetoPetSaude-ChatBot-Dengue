from rapidfuzz import process, fuzz
from typing import List, Dict, Optional, Tuple
from app.utils.data_loader import DataLoader

class NLPService:
    def __init__(self):
        self.data_loader = DataLoader()
        self.threshold = 60.0

    def find_best_match(self, user_text: str) -> Tuple[Optional[Dict], float]:
        """
        Busca a melhor categoria baseada na similaridade entre o texto do usuário 
        e as palavras-chave de cada categoria.
        """
        data = self.data_loader.get_all()
        if not data:
            return None, 0.0

        best_score = 0.0
        best_match = None
        user_text = user_text.lower().strip()

        for item in data:
            # Comparamos o texto do usuário com cada palavra-chave da categoria
            # Usamos token_set_ratio para lidar com frases e palavras fora de ordem
            keywords = item.get('palavras_chave', [])
            
            # Também comparamos com o título
            targets = keywords + [item['titulo'].lower()]
            
            # Extraímos a melhor pontuação para este item específico
            result = process.extractOne(
                user_text, 
                targets, 
                scorer=fuzz.token_set_ratio
            )
            
            if result:
                score = result[1]
                if score > best_score:
                    best_score = score
                    best_match = item

        if best_score >= self.threshold:
            return best_match, best_score
        
        return None, best_score
