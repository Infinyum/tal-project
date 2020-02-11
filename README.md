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