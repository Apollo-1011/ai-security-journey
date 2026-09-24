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
