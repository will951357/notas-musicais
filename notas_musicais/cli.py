from typer import Argument, Typer
from rich.console import Console
from rich.table import Table
from notas_musicais.escalas import escala as _escala
from notas_musicais.acordes import acorde as _acorde
from notas_musicais.campo_harmonico import campo_harmonico as _campo_harmonico

console = Console()
app = Typer()

@app.command()
def escala(tonica: str = Argument('c'), tonalidade: str = Argument('maior')):
    table = Table()
    notas, graus = _escala(tonica, tonalidade).values()
    
    for grau in graus:
        table.add_column(grau)  

    table.add_row(*notas)
    console.print(table)


@app.command()
def acorde(cifra: str = Argument('c')):
    table = Table()
    notas, graus = _acorde(cifra).values()
    
    for grau in graus:
        table.add_column(grau)  

    table.add_row(*notas)
    console.print(table)

@app.command()
def campo_harmonico(tonica: str = Argument('c'), tonalidade: str = Argument('maior')):
    table = Table()
    notas, graus = _campo_harmonico(tonica, tonalidade).values()
    
    for grau in graus:
        table.add_column(grau)  

    table.add_row(*notas)
    console.print(table)