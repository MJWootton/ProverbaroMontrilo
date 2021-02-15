# -*- coding: UTF-8 -*-
"""
Montru hazardan lineon el la Proverbaro
Mark Wootton

"""

# Alvoki modulojn
import os
import sys
import random
import textwrap
import shutil

def main():
    # Ŝanĝi la kurantan dosierujon al tiu de ĉi tiu programo
    if len(os.path.dirname(sys.argv[0])):
        os.chdir(os.path.dirname(sys.argv[0]))
    # Krei liston por teni la proverbojn
    proverbaro = []
    # Malfermi la dosieron, kiu enhavas la Proverbaron
    dosiero = open(os.path.join(os.getcwd(), 'proverbaro.txt'), 'r')
    # Legi dosieron kaj konservi la proverbojn
    for lineo in dosiero:
        proverbaro.append(lineo.strip('\n'))
    # Elekti hazardan proverbon kaj montri ĝin
    print(textwrap.fill(proverbaro[random.randint(0,len(proverbaro)-1)], shutil.get_terminal_size()[0]))
    # Fermi dosieron
    dosiero.close()

if __name__ == '__main__':
    main()
