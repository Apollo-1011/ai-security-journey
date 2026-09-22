# Ceci est le premier test de la version 4 du script

Cette version apporte différentes modifications.

La modification majeure est le fait de pouvoir choisir le dossier dans lequel j'enregistre le fichier Markdown.
Le deuxième point est le fait de pouvoir choisir le nom du fichier Markdown.
Le troisième point est la mise en place d'un try/except pour pouvoir faire un control C correct pendant le script si jamais je veux arrêter le script.
Le except met donc en place une fermeture du stream d'enregistrement du son correct pour être sûr qu'il n'y ait pas de corruption au niveau du micro et que le prochain enregistrement se passe correctement.

J'ai donc fait des tests d'interruption au moment de choisir le dossier et j'ai fait un control C à ce moment là.
Le control C a fonctionné.
J'ai fait un control C pendant l'enregistrement, ça a fonctionné, il n'y a pas eu de téléversements en Markdown qui a été fait sur le début de l'enregistrement que j'avais fait.
Donc tout semble être fonctionnel.

Le dernier test est de s'assurer que tout fonctionne toujours correctement pour la suite du programme.
