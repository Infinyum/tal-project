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
```python3 src/labelTranslationPOS.py pos_test.txt.pos.nltk pos_test.txt.pos.nltk.univ POSTags_PTB_Universal_Linux.txt```
```python3 src/labelTranslationPOS.py pos_test.txt.pos.stanford pos_test.txt.pos.stanford.univ POSTags_PTB_Universal_Linux.txt```
```python3 src/labelTranslationPOS.py pos_test.txt.pos.lima pos_test.txt.pos.lima.univ POSTags_PTB_Universal_Linux.txt```

### 5. Lancer l’évaluation des trois POS taggers
Stanford :
Word precision: 0.015882469724
Word recall: 0.0146991272393
Tag precision: 0.015882469724
Tag recall: 0.0146991272393
Word F-measure: 0.0152679040031
Tag F-measure: 0.0152679040031

nltk :
Word precision: 0.0156839388525
Word recall: 0.0145153881488
Tag precision: 0.0156839388525
Tag recall: 0.0145153881488
Word F-measure: 0.015077055203
Tag F-measure: 0.015077055203

### 6. Quelles conclusions vous pouvez avoir à partir des résultats d’évaluation des trois (ou deux) POS taggers ?

## II - Evaluation de la reconnaissance d’entités nommées
### Utiliser le corpus annoté « ne_reference.txt.conll » pour extraire les phrases ayant servi pour produire ce corpus annoté et sauvegarder le résultat dans le fichier « ne_test.txt ». Dans ce corpus, une ligne vide indique la fin de la phrase courante.
```python3 src/extractCorpus.py ne_reference.txt.conll ne_test.txt```