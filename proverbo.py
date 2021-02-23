#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Montru hazardan linion el la Proverbaro
Mark Wootton
"""

# Import modulojn
import os
import random
import shutil
import sys
import textwrap


def main():
    # Ŝanĝi la kurantan dosierujon al tiu de ĉi tiu programo
    if len(os.path.dirname(sys.argv[0])):
        os.chdir(os.path.dirname(sys.argv[0]))
    # Krei liston por teni la proverbojn
    proverbaro = []
    # Malfermi la dosieron, kiu enhavas la Proverbaron
    dosiero = open(os.path.join(os.getcwd(), 'proverbaro.txt'), 'r', encoding='utf8')
    # Legi dosieron kaj konservi la proverbojn
    for lineo in dosiero:
        proverbaro.append(lineo.strip('\n'))
    # Trovi kiam da proverboj estas dezirate
    n = 1
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    for _ in range(n):
        # Elekti hazardan proverbon kaj montri ĝin
        print(textwrap.fill(proverbaro[random.randint(0, len(proverbaro)-1)], shutil.get_terminal_size()[0]))
    # Fermi dosieron
    dosiero.close()


if __name__ == '__main__':
    main()
