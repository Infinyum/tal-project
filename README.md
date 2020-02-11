# Projet TAL
## I - Evaluation de l’analyse morpho-syntaxique
### 1. Convertir les tags du corpus annoté « pos_reference.txt.lima » en tags universels et sauvegarder le résultat dans le fichier « pos_reference.txt.univ ».

Commande à exécuter :
```python3 src/labelTranslation.py pos_reference.txt.lima pos_reference.txt.univ POSTags_PTB_Universal_Linux.txt```

Le premier paramètre est le fichier en entrée, le deuxième est le fichier de sortie et le troisième est le fichier contenant les correspondances entre les étiquettes PTB et universelles.

### 2. Utiliser le corpus annoté « pos_reference.txt.univ » pour extraire les phrases ayant servi pour produire ce corpus annoté et sauvegarder le résultat dans le fichier « pos_test.txt ». Dans ce corpus, une ligne vide indique la fin de la phrase courante.

Commande à exécuter :
```python3 src/extractCorpus.py pos_reference.txt.univ pos_test.txt```

Le premier paramètre est le fichier en entrée, le second est le fichier de sortie.

### 3. Lancer les trois POS taggers sur le fichier « pos_test.txt ».

```analyzeText -l eng -p main pos_test.txt > temp_pos.txt.lima```
```python3 src/formatLima.py temp_pos.txt.lima pos_test.txt.pos.lima```

```./stanford-postagger.sh models/english-left3words-distsim.tagger pos_test.txt > temp_pos.txt.stanford```
```python3 src/formatStanford.py temp_pos.txt.stanford pos_test.txt.pos.stanford```

```python3 src/nltkPOSTagger.py pos_test.txt pos_test.txt.pos.nltk```

### 4. Convertir les résultats des trois POS taggers en utilisant les étiquettes universelles.