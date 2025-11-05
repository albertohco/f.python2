"""Exemplo de import do pacote `extra` usando um caminho relativo robusto.

Este arquivo está em `mod/aula1/main2.py` e o pacote `extra` fica em
`/home/local_us/python2/extra`. Para garantir que o import funcione
independentemente do diretório de trabalho atual, adicionamos ao
`sys.path` a raiz do projeto (duas pastas acima deste arquivo).
"""
from pathlib import Path
import sys

# raiz do projeto: ../../ (a partir deste arquivo)
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import extra.iota

print(extra.iota.FunI())
print(ROOT)
print(sys.path[0])