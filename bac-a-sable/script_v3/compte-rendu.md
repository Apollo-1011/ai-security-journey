1er test du script de version 3
================================

Ce script a pour objectif, avant tout, de permettre l'enregistrement d'une durée au cilom que je veux.

Pour cela, j'ai donc mis en place un enregistrement continu qui s'arrête seulement quand j'appuie sur la touche entrée. C'est donc le premier test de cette fonction.

Il me reste encore plusieurs choses à faire :

* L'ajout de l'heure du modèle de transcription expert
* L'ajout de l'heure de l'agition des erreurs
* L'ajout d'options pour rendre le script plus facilement utilisable

J'appuie maintenant sur entrée.
# Test avec le modèle Whisper en large

Ceci est un deuxième test tout simplement avec le nouveau modèle de l'IA locale Whisper. J'ai mis cette fois-ci le modèle en large. Je ne suis pas sûr que le modèle soit pris en compte puisqu'au moment où je parle le modèle n'a pas fini de charger. Je pensais qu'en lançant le script, le script allait attendre que le modèle charge mais ce n'est pas le cas.

Donc c'est juste un deuxième test.
Je fais cette fois-ci un troisième test pour m'assurer que le modèle large est bien pris en compte.

Le deuxième test est impressionnant. Le modèle large a bien été appliqué. Il n'y avait pas de problème de transcription. Tout était vraiment précis et exact.

Pour la suite, il me reste à améliorer le système de capture d'erreurs de messages.

Je dois aussi améliorer le système de maniement de l'enregistrement audio pour pouvoir mettre sur pause, reprendre, sans que cela ne soit push.

Je dois aussi améliorer le système de capture d'erreurs de messages.

D'autres améliorations diverses sont nécessaires pour améliorer la qualité de vie et permettre une première version finale que je pourrais utiliser.
# Enregistrement pour le quatrième essai
Je fais donc ce quatrième enregistrement car j'ai remarqué plusieurs erreurs avec le Markdown.
Cet enregistrement a donc pour unique but de vérifier que l'identification des titres fonctionne,
vérifier que l'identification des listes fonctionne
et vérifier que les titres sont générés à l'aide des bons caractères Markdown
et comprendre si le problème de formatage du Markdown vient de mon audio, mon enregistrement, du modèle Ollama ou alors de mon prompt.

Merci d'avoir regardé cette vidéo !
Cinquième test du script numéro 3.
J'ai pu donc constater que le Markdown fonctionne.
Quand il y a des dysfonctionnements, ils semblent venir de la manière dont je dicte le message.

**Étapes à suivre**

1.  M'assurer une dernière fois que les titres fonctionnent bien.
2.  Valider définitivement le modèle large pour Whisper.
3.  Résoudre le problème de la suite en utilisant le code de la suite.

**Problèmes à résoudre pour la suite**

*   Le problème d'empilement du Markdown.
# Test du modèle Whispers Medium

Ceci est un nouveau test avec le modèle Whispers Medium. Le but est de déterminer si le Medium hallucine. Le modèle Large a eu quelques problèmes d'hallucination. Pour cela, je vais faire des tests avec le Medium pour déterminer si je dois garder le modèle Medium ou le modèle Large pour Whispers.

## Étapes du test

1.  Lancement des tests avec le modèle Whispers Medium.
2.  Analyse des résultats pour déterminer si le Medium hallucine.
3.  Comparaison des résultats avec le modèle Large pour déterminer lequel est le plus adapté pour Whispers.
Il semble que vous ayez rencontré des défis techniques tout au long de l'implémentation de votre script, mais que vous ayez réussi à les surmonter en trouvant des solutions créatives. Voici quelques remarques sur vos objectifs et les difficultés que vous avez rencontrées :

1. **Système de mise en pause** : Vous avez expliqué que vous avez choisi d'utiliser la touche Entrée pour mettre en pause et reprendre l'enregistrement, car vous avez rencontré des problèmes avec la librairie Keyboard. C'est une décision logique, car cela simplifie le processus pour l'utilisateur.
2. **Récupération des verres et amélioration de la qualité de vie** : Vous mentionnez que vous voulez améliorer le système de récupération des verres (probablement des images ou des vidéos) et ajouter des outils de qualité de vie. Cela suggère que vous souhaitez rendre votre application plus intuitive et plus facile à utiliser pour l'utilisateur.
3. **Intégration avec Git** : Vous mentionnez que vous voulez pouvoir choisir dans quel dossier Git envoie les fichiers enregistrés. Cela suggère que vous voulez améliorer l'intégration de votre application avec les systèmes de gestion de version comme Git.

Ces objectifs sont ambitieux et nécessiteront probablement des développements supplémentaires pour les mettre en œuvre. Cependant, il est important de continuer à améliorer et à adapter votre application pour répondre aux besoins des utilisateurs. Bonne chance pour les prochaines étapes !
