# Gestionnaire de Tâches en Python (Codecamp)

## Description
Ce projet a été réalisé dans le cadre du Codecamp de rentrée.  
L'objectif est de développer, en groupe, un logiciel de gestion de tâches simple en Python, sous la forme d’une interface en ligne de commande (CLI).  

L’utilisateur peut ajouter, modifier, supprimer et afficher des tâches sauvegardées dans un fichier texte.


##lien live share 
https://prod.liveshare.vsengsaas.visualstudio.com/join?6CA9E55E0BE52198A41B41BB0AD801E4D963
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
### Modifier une tâche 
Remplace la description de la tâche d’identifiant id dans lestaches.txt, renvoie un message d’erreur si la tâche n’est pas trouvée
### Supprimer une tâche
Retire la ligne du fichier lestaches.txt contenant la tâche d’identifiant id, renvoie un message d’erreur si la tâche n’est pas trouvée
### Afficher les tâche
Affiche la liste des tâches du fichier en les triant par leurs identifiants
