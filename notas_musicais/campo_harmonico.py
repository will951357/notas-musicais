from notas_musicais.acordes import triade
from notas_musicais.escalas import escala

def _triade_na_escala(nota: str, notas_escala: list):
    """
    Saber se a nota está na escala

    Args:
        nota: ...
        notas_escala: ...

    Examples:
        >>> _triade_na_escala('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'C'
    """
    tonica, terca, quinta = triade(nota, 'maior')

    match terca in notas_escala, quinta in notas_escala:
        case True, True:
            return tonica
        case False, True:
            return f'{tonica}m'
        case False, False:
            return f'{tonica}°'

def _converte_graus(cifra: str, grau: str):
    """
    Converte graus relativo à cifra

    Args:
        cifra: Uma cifra de um acorde
        grau: Grau em forma maior

    Examples:
        >>> _converte_graus('C', ''I')
        'I'
        >>> _converte_graus('Cm', 'I')
        'i'
        >>> _converte_graus('C°', 'I')
        'i°'
    """

    if 'm' in cifra:
        return grau.lower()
    
    if '°' in cifra:
        return grau.lower() + '°'
    
    return grau


def campo_harmonico(tonica: str, tonalidade: str) -> dict[str, list[str]]:

    """
    Gera um campo harmônico com base em uma tônica e uma tonalidade

    Args:
        tonica: Primeiro grau do campo harmonico
        tonalidade: Tonalidade do campo (maior, menor, ...)

    Returns:
        Um campo harmônico

    Examples:
        >>> campo_harmonico('c', 'maior')
        {'acordes': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'B°'], 'graus': ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°']}
    """

    notas, _graus = escala(tonica, tonalidade).values()
    acordes = [_triade_na_escala(nota, notas) for nota in notas]
    graus = [
        _converte_graus(acorde, grau) for acorde, grau in zip(acordes, _graus)
    ]

    return {'acordes': acordes, 'graus': graus}