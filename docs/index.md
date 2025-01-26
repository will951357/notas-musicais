![Logo do projeto](assets/logo.png){ width="300" .center}
# Notas Musicais

Notas musicais é um CLI para ajudar na formação de escalas  e acordes.
Temos dois comandos disponíveis 'escala' e 'acorde'

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