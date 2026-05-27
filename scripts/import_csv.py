import csv
import json
import os
import sys

def import_csv_to_json(csv_path: str, json_output_path: str):
    """
    Converte a planilha CSV de conteúdo para o arquivo JSON consumido pela API.
    Realiza validações básicas de consistência.
    """
    if not os.path.exists(csv_path):
        print(f"Erro: Arquivo CSV não encontrado em {csv_path}")
        sys.exit(1)

    data = []
    required_columns = ['titulo', 'texto', 'palavras_chave', 'fonte']

    try:
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            # Validação de colunas
            if not all(col in reader.fieldnames for col in required_columns):
                missing = [col for col in required_columns if col not in reader.fieldnames]
                print(f"Erro: Colunas obrigatórias ausentes: {missing}")
                sys.exit(1)

            for row in reader:
                # Validação de campos vazios
                if not all(row[col].strip() for col in required_columns):
                    print(f"Aviso: Pulando linha com campos obrigatórios vazios: {row['titulo']}")
                    continue

                # Processamento de palavras_chave (string para lista)
                row['palavras_chave'] = [p.strip().lower() for p in row['palavras_chave'].split(',')]
                
                data.append({
                    'titulo': row['titulo'].strip(),
                    'texto': row['texto'].strip(),
                    'palavras_chave': row['palavras_chave'],
                    'fonte': row['fonte'].strip()
                })

        # Escrita do JSON
        os.makedirs(os.path.dirname(json_output_path), exist_ok=True)
        with open(json_output_path, mode='w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"Sucesso: {len(data)} categorias importadas para {json_output_path}")

    except Exception as e:
        print(f"Erro inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    CSV_FILE = 'conteudo_petsaude.csv'
    JSON_FILE = os.path.join('app', 'data', 'dengue.json')
    import_csv_to_json(CSV_FILE, JSON_FILE)
