import json
import os
from typing import List, Dict

class DataLoader:
    _instance = None
    _data = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataLoader, cls).__new__(cls)
            cls._instance._load_data()
        return cls._instance

    def _load_data(self):
        json_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'dengue.json')
        try:
            if os.path.exists(json_path):
                with open(json_path, 'r', encoding='utf-8') as f:
                    self._data = json.load(f)
            else:
                print(f"Aviso: {json_path} não encontrado.")
                self._data = []
        except Exception as e:
            print(f"Erro ao carregar dengue.json: {e}")
            self._data = []

    def get_all(self) -> List[Dict]:
        return self._data

    def reload(self):
        self._load_data()
