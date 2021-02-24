# ProverbaroMontrilo
Promgrameto por Montri Hazardan Linion el la Proverbaro

## Bezonaĵoj

- [Python 3](https://www.python.org/)

## Uzado

Rulu terminale la programeton per:

```shell
$ python proverbo.py
```

Por montri plurajn proverbojn, oni povas skribi entjeran kvanton kiel komandlinian argumenton, ekzemple:

```shell
 $ python proverbo.py 10
```

Se oni volus uzi malsaman liston de proveroj, oni povas doni ilin per listo de tekstdosieroj post la etikedo `-f`, ekzemple:

```shell
$ python proverbo.py -f dosieroA.txt dosieroB.txt
```

Se oni donas la etikedon `-f` sen listo de dosieroj, la programeto serĉos la dosieron `proverbaro.txt` en sia propra dosierujo.

Mi kreis ĉi tiun programeton por montri proverbaranon, kiam nova terminala fenestro estas malfermita. En baŝo (*bash*) oni povas fari ĉi tion per la aldono al `~/.bashrc` de linio kiel:

```bash
python $HOME/user/git/ProverbaroMontrilo/proverbo.py
```

Memoru ŝanĝi la dosierindikon al la loko ĝusta por la propra komputilo.

## Ekzemplo

<p align="center">
  <img src='ekzemplo.png' width='500' title='Neofetch kaj ProverbarMontrilo'>
</p>

Ekzemplo de nova terminala fenestro kun rulo de [Neofetch](https://github.com/dylanaraps/neofetch) kaj ProverbaroMontrilo.

### Agnosko

Dankon al www.proverbaro.net pro la fonto de la proverboj.