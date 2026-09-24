# Compte Rendu de la Première Version Finale du Script

## Fils Conducteurs du Projet

Tout d'abord, la règle "toute chose en son temps". C'est-à-dire que la mise en place de chaque nouvelle idée doit être réalisée étape par étape, en commençant par la solution la plus simple.

## Principes du Projet

*   Chaque implémentation d'une nouvelle idée doit être testée avant d'être améliorée.
*   Le découpage en versions (1 à 4) pour faciliter la compréhension et la mise en place de chaque version.
*   Ne garder que les lignes de code qui sont explicites et compréhensibles.
*   Vérifier et faire des tests plutôt que de supposer et de modifier directement le script lorsqu'il y a un dysfonctionnement.

## Difficultés Réalisées

### Mise en Place des Versions de Python

*   La première difficulté était de comprendre et de mettre en place correctement les bonnes versions de Python.
*   J'ai décidé de prendre la version Python 3.14, qui représente un bon équilibre entre une version non obsolète et la dernière version, qui pourrait comporter des bugs.

### Mise en Place du SSH

*   La génération de clés pour simplifier le projet et automatiser l'ajout de fichiers sur mon Git.
*   La mise en place d'une clé SSH pour rendre le processus plus simple.

### Mise en Place du VENV

*   La mise en place du VENV et l'assurance qu'il est bien configuré pour comprendre tous les enjeux.

### Problèmes de CUDA et PyTorch

*   La détection des IA locales et l'alignement avec PyTorch pour que les IA locales puissent tourner sur mon matériel.

### Problèmes avec Whisper

*   La recherche de la transcription utilisée et le problème du chemin de Windows Path refusé par Whisper.
*   La nécessité de convertir en STR pour résoudre le problème.

### Problèmes de Distinction entre les Modèles d'IA Locaux et Cloud

*   La compréhension de la distinction entre les modèles d'IA locales et cloud.
*   La compréhension de quel modèle d'IA utilisé et importé en local pour la transcription et le reformatage en Markdown.

### Problèmes de Prompt Engineering

*   La compréhension de comment faire un prompt système efficace pour le modèle LAMA sélectionné.
*   La nécessité de utiliser des phrases courtes et anti-conversation.

### Problèmes d'Hallucination de Whisper

*   La compréhension de la raison pour laquelle Whisper essayait trop d'anticiper ce que j'allais dire et de remplir les pauses avec des phrases de type de traduction YouTube.
*   La réglement de l'hallucination de Whisper pour qu'il ne remplisse pas les pauses avec des phrases de traduction YouTube.

### Autres Difficultés Réalisées

*   L'amélioration de la gestion de l'enregistrement avec des touches, en utilisant la touche entrée pour faire pause et reprise.
*   L'apprentissage de la gestion du callback du stream, pour faire un enregistrement en continu qu'on peut interrompre de manière propre.
*   La mise en place d'un arrêt du script correct, en utilisant les bonnes commandes et en mettant en place les try except et le keyboard interrupt.

## Limites du Projet

*   Le système de pause reprise qui est imparfait et basique.
*   Le choix des modèles d'IA, qui pour l'instant sont LAMA et Whisper Medium, mais qui pourraient évoluer dans le futur.
*   La gestion des erreurs, qui n'est actuellement réalisée que pour la première partie du script, et qui devrait être améliorée pour prendre en compte les problèmes de micro, de Whisper, de OlaMa ou du Git.
# Bilan du premier script d'automatisation de mise en ligne sur mon GitHub de fichiers Markdown

## Pourquoi j'ai construit ce script

Je voulais créer un script pour faciliter la création de fichiers Markdown pour mon portfolio. Puisque j'allais avoir besoin de faire plusieurs comptes rendus à Markdown, j'ai décidé d'automatiser le processus de création de ces fichiers.

## La pipeline du script

La pipeline du script consiste à :

1. Enregistrer en train de parler à l'aide d'un micro et d'un script Python.
2. Utiliser la bibliothèque Sound Devices pour récupérer l'audio.
3. Utiliser Whispers en local pour faire une transcription de l'audio.
4. Envoyer la transcription au modèle Lama 3.1 qui est également en local pour corriger les fautes d'orthographe, ajouter de la ponctuation et reformater en Markdown.
5. Envoyer le fichier Markdown sur mon dépôt GitHub.

## Choix techniques

Voici les choix techniques que j'ai faits pour ce script :

* J'ai choisi Python 3.14 comme interpréteur Python, car il était à la fois récent et stable.
* J'ai choisi le modèle Medium de Whispers, car il était très utilisé et avait une grande communauté pour résoudre les problèmes.
* J'ai choisi le modèle Lama 3.1 en 8 milliards de paramètres, car il était très utilisé et performant.
* J'ai mis en place une connexion avec GitHub à l'aide d'une clé SSH pour faciliter l'utilisation et l'upload des fichiers.

## Difficultés rencontrées

Voici les difficultés que j'ai rencontrées et les corrections que j'ai apportées :

* Hallucinations de Whisper : J'ai baissé la qualité du modèle Whisper pour réduire les hallucinations.
* Compréhension de Lama : J'ai mis en place un prompt système très strict pour aider Lama à comprendre son objectif.
* Pause de l'enregistrement : J'ai mis en place un système pour ne pas fermer le stream de Sound Devices, mais simplement de ne plus l'enregistrer pendant la pause.

## Limites actuelles

Voici les limites actuelles du script :

* Capture des erreurs : J'ai une capture des erreurs pour la première partie du script, mais pas pour la partie transcription avec Whisper, l'AMA et le push sur GitHub.
* Whisper : Il est difficile pour l'instant de pouvoir utiliser des termes anglais ou des termes techniques car Whisper ne les reconnaît pas tous.
* Prompt système de LAMA : Il faudra améliorer le prompt système de LAMA pour qu'il prenne en compte les règles de prompt données.
* Gestion de l'enregistrement : Le script est rudimentaire sur la gestion de l'enregistrement, notamment avec les touches. Il faudra améliorer cela pour pouvoir utiliser et gérer plus facilement la manière dont on enregistre l'audio.
* Vérification et retouches de compte rendu : Il n'y a pas de moyen actuellement de vérifier et de faire des retouches de compte rendu avant qu'il soit envoyé sur mon GitHub.
