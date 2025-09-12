[# Gestionnaire de Tâches en Python (Codecamp)

## Description
Ce projet a été réalisé dans le cadre du Codecamp de rentrée.  
L'objectif est de développer, en groupe, un logiciel de gestion de tâches simple en Python, sous la forme d’une interface en ligne de commande (CLI).  

L’utilisateur peut ajouter, modifier, supprimer et afficher des tâches sauvegardées dans un fichier texte.


---

## Règles du projet
- Développement en groupe (6 à 7 étudiants, groupes constitués par tirage au sort).
- Chaque fonctionnalité doit être validée en interne (au moins deux membres du groupe).
- Validation finale par un membre d’une autre équipe.
- Extensions possibles une fois l’étape courante validée.
- Objectif : produire un code simple, lisible et robuste en utilisant principalement la bibliothèque standard de Python.
- L’utilisation de bibliothèques externes comme Pandas est interdite.

---

## Fonctionnalités de la version initiale
Le programme `task` permet les actions suivantes :

### Ajouter une tâche
Ajoute au fichier lestaches.txt la ligne de la tâche, retourne son identifiant
```bash
python src/main.py tests/lestaches.txt add --description <DESCRIPTION> --project <NOM PROJET>
```

### Modifier une tâche 
Remplace la description de la tâche d’identifiant id dans lestaches.txt, renvoie un message d’erreur si la tâche n’est pas trouvée
```bash
python src/main.py tests/lestaches.txt modify <ID> --description <NEW DESCRIPTION> --project <NEW PROJECT NAME>
```
### Supprimer une tâche
Retire la ligne du fichier lestaches.txt contenant la tâche d’identifiant id, renvoie un message d’erreur si la tâche n’est pas trouvée
```bash 
python src/main.py tests/lestaches.txt r
```

### Afficher les tâche
Affiche la liste des tâches du fichier en les triant par leurs identifiants
```bash 
python src/main.py tests/lestaches.txt rm <ID>
```




](https://prod.liveshare.vsengsaas.visualstudio.com/join?A4CB10AFDEEE5C4287D535D8071D9E4AD8CC
# Gestionnaire de Tâches en Python (Codecamp)

## Description
Ce projet a été réalisé dans le cadre du Codecamp de rentrée.  
L'objectif est de développer, en groupe, un logiciel de gestion de tâches simple en Python, sous la forme d’une interface en ligne de commande (CLI).  

L’utilisateur peut ajouter, modifier, supprimer et afficher des tâches sauvegardées dans un fichier texte.


---

## Règles du projet
- Développement en groupe (6 à 7 étudiants, groupes constitués par tirage au sort).
- Chaque fonctionnalité doit être validée en interne (au moins deux membres du groupe).
- Validation finale par un membre d’une autre équipe.
- Extensions possibles une fois l’étape courante validée.
- Objectif : produire un code simple, lisible et robuste en utilisant principalement la bibliothèque standard de Python.
- L’utilisation de bibliothèques externes comme Pandas est interdite.

---

## Fonctionnalités de la version initiale
Le programme `task` permet les actions suivantes :

### Ajouter une tâche
Ajoute au fichier lestaches.txt la ligne de la tâche, retourne son identifiant
```bash
python src/main.py tests/lestaches.txt add --description <DESCRIPTION> --project <NOM PROJET> --done_on <OPTIONAL, by default TBD>
```

### Modifier une tâche 
Remplace la description de la tâche d’identifiant id dans lestaches.txt, renvoie un message d’erreur si la tâche n’est pas trouvée
```bash
python src/main.py tests/lestaches.txt modify <ID> --description <NEW DESCRIPTION> --project <NEW PROJECT NAME> --due <DEADLINE JJ/MM/AAAA>
```
### Supprimer une tâche
Retire la ligne du fichier lestaches.txt contenant la tâche d’identifiant id, renvoie un message d’erreur si la tâche n’est pas trouvée
```bash 
python src/main.py tests/lestaches.txt rm <ID>
```

###  Marquer une tache commme accomplie 
```bash 
python src/main.py realized tests/lestaches.txt <ID> --date <JJ/MM/AAAA>


```
###  Recherche (ALL PARAMETERS ARE OPTIONAL)
```bash
python src/main.py search --projet <NOM PROJET> --description <NOM TASK> --before <DATE ECHEANCE> --after <DATE ECHEANCE> --isRealized <0 or 1>

```
### Afficher les tâche
Affiche la liste des tâches du fichier en les triant par leurs identifiants
```bash 
python src/main.py tests/lestaches.txt show
```


MARBOEUF Kéwan
ETTAIEB Montadhar
DHOUIB Amal
MAO Xiang you
NEHLIL Kamel