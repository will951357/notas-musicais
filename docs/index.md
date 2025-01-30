![Logo do projeto](assets/logo.png){ width="300" .center}
# Notas Musicais

Notas musicais é um CLI para ajudar na formação de escalas, acordes e campos harmônicos.
Temos dois comandos disponíveis 'escala' e 'acorde'

Toda ação é baseada em um comando chamado 'nota-musicais'. Este comando tem um subcomando relacionado
a cada ação que a aplicação pode realizar.

## Como usar Escalas?

Você pode usar as escalas via linha de comando. Por exemplo:

```bash
poetry run notas-musicais escala

┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

### Alteração na Tonica da escala

Você também pode alterar a tonalidade da escala. Por exemplo

```bash
poetry run notas-musicais escala G# maior

┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ G# │ A# │ C   │ C# │ D# │ F  │ G   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

## Como usar acordes?
Uso basico
```bash
poetry run notas-musicais acorde F#

┏━━━━┳━━━━━┳━━━━┓
┃ I  ┃ III ┃ V  ┃
┡━━━━╇━━━━━╇━━━━┩
│ F# │ A#  │ C# │
└────┴─────┴────┘
```

Variações na sifra

```bash
poetry run notas-musicais acorde F#+

┏━━━━┳━━━━━┳━━━━┓
┃ I  ┃ III ┃ V+ ┃
┡━━━━╇━━━━━╇━━━━┩
│ F# │ A#  │ D  │
└────┴─────┴────┘
```

## Como usar campos harmônicos
Você pode chamar os campos harmônicos via o subcomando `campo-harmonico`. Como por exemplo:

```bash
poetry run notas-musicais campo-hamonico


┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━━┓
┃ I ┃ ii ┃ iii ┃ IV ┃ V ┃ vi ┃ vii° ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━━┩
│ C │ Dm │ Em  │ F  │ G │ Am │ B°   │
└───┴────┴─────┴────┴───┴────┴──────┘
```

Por padrão os parâmetros utilizados são a tônica de `C` e o campo hamônico `maior`.

### Alterações nos campos harmônicos
Você pode alterar os parâmetros da tônica e da tonalidade da seguinte forma:

```bash
    notas-musicais campo-harmonico [TONICA] [TONALIDADE]
```

## Informações sobre o CLI

```bash
notas-musicais [OPTIONS] COMMAND [ARGS]...

╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion   Install completion for the current shell.                                              │
│ --show-completion      Show completion for the current shell, to copy it or customize the installation.       │
│ --help                 Show this message and exit.                                                            │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ escala                                                                                                         │
│ acorde                                                                                                         │
│ campo-harmonico                                                                                                │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```