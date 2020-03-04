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
On réutilise les outils des trois premiers TPs :
  
```analyzeText -l eng -p main pos_test.txt > temp_pos.txt.lima```
```python3 src/formatLima.py temp_pos.txt.lima pos_test.txt.pos.lima```
  
```./stanford-postagger.sh models/english-left3words-distsim.tagger pos_test.txt > temp_pos.txt.stanford```
```python3 src/formatStanford.py temp_pos.txt.stanford pos_test.txt.pos.stanford```
  
```python3 src/nltkPOSTagger.py pos_test.txt pos_test.txt.pos.nltk```

### 4. Convertir les résultats des trois POS taggers en utilisant les étiquettes universelles.
```python3 src/labelTranslationPOS.py pos_test.txt.pos.nltk pos_test.txt.pos.nltk.univ POSTags_PTB_Universal_Linux.txt```
  
```python3 src/labelTranslationPOS.py pos_test.txt.pos.stanford pos_test.txt.pos.stanford.univ POSTags_PTB_Universal_Linux.txt```
  
```python3 src/labelTranslationPOS.py pos_test.txt.pos.lima pos_test.txt.pos.lima.ptb POSTags_LIMA_PTB.txt```
```python3 src/labelTranslationPOS.py pos_test.txt.pos.lima.ptb pos_test.txt.pos.lima.univ POSTags_PTB_Universal_Linux.txt```
  
Le premier paramètre est le fichier en entrée, le deuxième est le fichier de sortie et le troisième est le fichier contenant les correspondances entre les étiquettes PTB et universelles. L'exception est pour l'outil lima où il faut d'abord convertir les étiquettes en PTB avant de les convertir en universelles.

### 5. Lancer l’évaluation des trois POS taggers
D'abord on retire les lignes vides du fichier référence (car elles ont été supprimées dans nos scripts) :
```python3 src/removeBlankLines.py pos_reference.txt.univ pos_reference.txt.univ.nb```
  
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
  
lima :  
Word precision: 0.0662835628654
Word recall: 0.0615059299439
Tag precision: 0.0662835628654
Tag recall: 0.0615059299439
Word F-measure: 0.0638054363376
Tag F-measure: 0.0638054363376 

### 6. Quelles conclusions vous pouvez avoir à partir des résultats d’évaluation des trois POS taggers ?
Les outils POS tagger de nltk et Stanford offrent des performances similaires. En revanche, celui de Lima est environ quatre fois plus précis que ces deux derniers. Il semble donc pertinent de s'orienter sur cet outil pour l'étape du POS tagging.

## II - Evaluation de la reconnaissance d’entités nommées
### 1. Utiliser le corpus annoté « ne_reference.txt.conll » pour extraire les phrases ayant servi pour produire ce corpus annoté et sauvegarder le résultat dans le fichier « ne_test.txt ». Dans ce corpus, une ligne vide indique la fin de la phrase courante.
```python3 src/extractCorpus.py ne_reference.txt.conll ne_test.txt```

Le premier paramètre est le fichier en entrée, le second est le fichier de sortie.

### 2. Lancer les trois NE recognizers sur le fichier « ne_test.txt ». Les résultats doivent avoir le format du corpus annoté « ne_reference.txt.conll » (2 colonnes séparées par une tabulation).
On réutilise les outils des trois premiers TPs :  
```java -mx600m -cp stanford-ner.jar:lib/* edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier classifiers/english.all.3class.distsim.crf.ser.gz -textFile ~/Documents/TAL_project/ne_test.txt > ~/Documents/TAL_project/ne_test.txt.ne.stanford.temp```
```python3 src/format_NE.py ne_test.txt.ne.stanford.temp ne_test.txt.ne.stanford```
  
```analyzeText -l eng -p main ne_test.txt > ne_test.txt.ne.lima.temp```
```python3 src/format_NE_lima.py ne_test.txt.ne.lima.temp ne_test.txt.ne.lima```
  
```python3 src/nltk_ne_recognizer.py ne_test.txt ne_test.txt.ne.nltk```

### 3. Convertir les résultats des trois NE recognizers en utilisant les étiquettes CoNLL-2003 (https://www.clips.uantwerpen.be/conll2003/ner/).
```python3 src/neTranslationConLL.py ne_test.txt.ne.lima ne_test.txt.ne.lima.conll```  
```python3 src/neTranslationConLL.py ne_test.txt.ne.stanford ne_test.txt.ne.stanford.conll```  
```python3 src/neTranslationConLL.py ne_test.txt.ne.nltk ne_test.txt.ne.nltk.conll```
  
Le premier paramètre est le fichier en entrée, le second est le fichier de sortie.

### 4. Lancer l’évaluation des trois NE recognizers
On retire d'abord les lignes vides du fichier référence (car elles ont été supprimées dans nos scripts) :
```python3 src/removeBlankLines.py ne_reference.txt.conll ne_reference.txt.conll.nb```
  
lima :
Word precision: 0.0114150555327
Word recall: 0.0115951112504
Tag precision: 0.0114150555327
Tag recall: 0.0115951112504
Word F-measure: 0.011504378919
Tag F-measure: 0.011504378919
  
Stanford :
Word precision: 0.00923718712753
Word recall: 0.00923718712753
Tag precision: 0.00923718712753
Tag recall: 0.00923718712753
Word F-measure: 0.00923718712753
Tag F-measure: 0.00923718712753
  
nltk :
Word precision: 0.0205601907032
Word recall: 0.0205601907032
Tag precision: 0.0205601907032
Tag recall: 0.0205601907032
Word F-measure: 0.0205601907032
Tag F-measure: 0.0205601907032
  
### 5. Quelles conclusions vous pouvez avoir à partir des résultats d’évaluation des trois NE recognizers.
Contrairement à l'évaluation des POS taggers, ici c'est l'outil nltk qui offre la meilleure précision (environ deux fois supérieure aux deux autres outils). On en conclut qu'il peut être intéressant d'utiliser des outils de différentes sources aux différents stades de la Traduction Automatique de la Langue afin de maximiser la précision du résultat final.