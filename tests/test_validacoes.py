from services.validacoes import validar_cidade


def test_cidade_valida():
    assert validar_cidade("Rio de Janeiro") == True


def test_cidade_vazia():
    assert validar_cidade("") == False


def test_cidade_com_espacos():
    assert validar_cidade("   ") == False