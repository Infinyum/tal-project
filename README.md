# tal-project
## I - Evaluation de l’analyse morpho-syntaxique
### 1. Convertir les tags du corpus annoté « pos_reference.txt.lima » en tags universels et sauvegarder le résultat dans le fichier « pos_reference.txt.univ ».
Commande à exécuter :
python3 src/labelTranslation.py pos_reference.txt.lima pos_reference.txt.univ POSTags_PTB_Universal_Linux.txt

Le premier paramètre est le fichier en entrée, le deuxième est le fichier de sortie et le troisième est le fichier contenant les correspondances entre les étiquettes PTB et universelles.