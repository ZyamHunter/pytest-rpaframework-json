import os
import pytest

if __name__ == "__main__":
    # Diretório onde os testes estão localizados
    test_directory = os.path.dirname(os.path.abspath(__file__))

    # Execução dos testes
    result = pytest.main([test_directory])

    print(result)
