#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Montru hazardan linion el la Proverbaro
Mark Wootton
"""

# Importi modulojn.
import argparse
from pathlib import Path
import random
import shutil
import textwrap


def akiri_argumentojn():
    argumento_tenilo = argparse.ArgumentParser(
        description='Montras hazardan proverbon en Esperanto'
    )
    argumento_tenilo.add_argument(
        'nombro', nargs='?', default=1, type=int, help='Nombro da probervoj montri.'
    )

    return argumento_tenilo.parse_args()


def ekfunkcio(argumentoj):
    # Trovi la dosierujon, kie estas ĉi-tiu programo.
    programo_dosierujo = Path(__file__).parent
    # Trovi la dosieron, kiu enhavas la Proverbaron.
    proverbaro_dosiero = programo_dosierujo / 'proverbaro.txt'

    # Malfermi la dosieron kun la proverboj.
    with open(proverbaro_dosiero, 'r', encoding='utf8') as dosiero:
        # El la dosiero, legi proverbojn, forigante la novlinio-signo (\n).
        proverbaro = [lineo.strip() for lineo in dosiero]

    # Elekti tiom da proverboj, kiom estas dezirataj de la uzanto.
    proverboj_printendaj = random.sample(proverbaro, argumentoj.nombro)

    # Printi ĉiujn proverbojn.
    for proverbo in proverboj_printendaj:
        # Ordigi la tekst-formon kaj printi.
        print(textwrap.fill(proverbo, shutil.get_terminal_size()[0]))


if __name__ == '__main__':
    ekfunkcio(akiri_argumentojn())
