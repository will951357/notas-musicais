from pytest import mark
from typer.testing import CliRunner
from notas_musicais.cli import app


runner = CliRunner()


def test_deve_retornar_0_ao_stdout():
    result = runner.invoke(app, ['escala'])
    assert result.exit_code == 0


@mark.parametrize(
        'nota', ['D', 'C', 'F', 'E']
)
def test_deve_conter_a_nota(nota):
    result = runner.invoke(app, ['escala', ])
    assert nota in result.stdout



