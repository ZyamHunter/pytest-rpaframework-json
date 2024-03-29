import json
import shutil
import tempfile
import os
from RPA.JSON import JSON

class JsonOperations:
    @staticmethod
    def calculate_total_spending(json_data, client_name):
        total_spending = 0
        for client in json_data["clients"]:
            if client["name"] == client_name:
                for order in client["orders"]:
                    total_spending += order["price"]
        return total_spending

    @staticmethod
    def load_json_from_file(file_path):
        json_file_path = os.path.abspath(file_path)
        """
        Carrega um JSON de um arquivo.
        """
        with open(json_file_path, "r", encoding="utf-8") as file:
            data = file.read()
            return JSON().convert_string_to_json(data)
            # return  json.load(file)

    @staticmethod
    def get_key_in_json_data(key):
        try:
            # Abre o arquivo JSON para leitura e carrega seu conteúdo em um dicionário
            with open('data.json', 'r') as file:
                dados = json.load(file)

            # Verifica se a key existe no dicionário
            if key in dados:
                return dados[key]
            else:
                return None  # A key não foi encontrada
        except FileNotFoundError:
            print(f'Arquivo {"data.json"} não encontrado.')
        except json.JSONDecodeError:
            print(f'Erro ao decodificar o arquivo JSON.')
        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')

    @staticmethod
    def update_json_data(key, new_value):
        try:
            # Abre o arquivo JSON para leitura e carrega seu conteúdo em um dicionário
            with open('data.json', 'r') as file:
                dados = json.load(file)
            
            # Atualiza o valor associado à key fornecida
            dados[key] = new_value

            # Abre o arquivo JSON para escrita e sobrescreve os dados atualizados
            with open('data.json', 'w') as file:
                json.dump(dados, file, indent=4)
            
            print(f'Chave "{key}" atualizada com sucesso para o valor "{new_value}" em {"data.json"}.')
        except FileNotFoundError:
            print(f'Arquivo {"data.json"} não encontrado.')
        except json.JSONDecodeError:
            print(f'Erro ao decodificar o arquivo JSON.')
        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')

    @staticmethod
    def load_invalid_json_file():
        try:
            with open('invalid_json_file.json', 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            raise json.JSONDecodeError('Erro ao decodificar o arquivo JSON.')
