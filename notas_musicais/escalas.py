NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escalas(tonica: str, tonalizade: str):
    """
    Gera uma escala a partir de uma tônica e uma tonalidade.

    Args:
        tonica: Nota que será a tônica da escala
        tonica: Tonalidade da escala
    
    Examples:
        >>> escalas('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escalas('A', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

    """
    intervalos = ESCALAS[tonalizade]
    tonica_pos = NOTAS.index(tonica)
    temp = []

    for intervalo in intervalos:    
        # O resto da divisão possibilita trabalhar com os valores de forma modular
        # r = a - b * q (r=resto, a=dividendo, b=divisor e q=quocinete)
        nota = (tonica_pos + intervalo) % 12
        temp.append(NOTAS[nota])

    return {
        'notas': temp, 
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    }

