def validar_cidade(cidade):

    if not cidade:
        return False

    return len(cidade.strip()) > 0