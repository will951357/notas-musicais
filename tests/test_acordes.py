from pytest import mark
from notas_musicais.acordes import acorde


@mark.parametrize(
        'nota, esperado', 
        [
            ('C', ['C','E', 'G']),
            ('Cm', ['C', 'D#', 'G']),
            ('F#', ['F#','A#', 'C#']),
            ('C°', ['C', 'D#', 'F#']),
            ('C+', ['C', 'E', 'G#']),
        ]
)
def test_retornar_notas_correspondentes(nota, esperado):
    nota, _ = acorde(nota).values()
    assert nota == esperado


@mark.parametrize(
        'cifra, esperado', 
        [
            ('C', ['I', 'III', 'V']),
            ('Cm', ['I', 'III-', 'V']),
            ('C°', ['I', 'III-', 'V-']),
            ('C+', ['I', 'III', 'V+']),
        ]
)
def test_retornar_grau_correspondentes(cifra, esperado):
    _, graus = acorde(cifra).values()
    assert esperado == graus

