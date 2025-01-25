"""
Método de teste AAA
Arrenge - Act - Assert
Arrumar - Agir - Garantir
"""
from pytest import mark, raises
from notas_musicais.escalas import NOTAS, ESCALAS,  escala


def test_escala_notas_minusculas():
    # Arrange
    tonica = 'c'
    tonalidade = 'maior'

    # Act
    result = escala(tonica, tonalidade)

    # Assert
    assert result

def test_nota_nao_existe():
    # Arrange
    tonica = 'X'
    tonalidade = 'maior'

    mensagem_erro = f"Essa nota não existe, tente uma dessas {NOTAS}"

    with raises(ValueError) as error:
        escala(tonica, tonalidade)
    
    assert mensagem_erro == error.value.args[0]

def test_escala_nao_existe():
    tonica = 'c'
    tonalidade = 'xpto'

    mensagem_erro = f'Essa tonalidade não existe ou não foi implemetada. Tente uma dessa {list(ESCALAS.keys())}'

    with raises(KeyError) as error:
        escala(tonica, tonalidade)

    assert mensagem_erro == error.value.args[0]

@mark.parametrize(
        'tonica,esperado', 
        [
            ('c', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
            ('c#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
            ('F', ['F', 'G', 'A', 'A#', 'C', 'D', 'E'])
        ],
)
def test_deve_retornar_notas_corretas(tonica, esperado):
    resultado = escala(tonica, 'maior')
    assert resultado['notas'] == esperado