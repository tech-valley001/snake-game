# 🐍 Snake Game - Pygame

Un jeu classique de **Snake** développé en Python à l'aide de la bibliothèque **Pygame**. 

Le serpent grandit lorsqu'il mange de la nourriture et le jeu intègre une mécanique de **traversée des bords** : au lieu de mourir en touchant les murs, le serpent réapparaît de l'autre côté de l'écran !

---

## 📋 Fonctionnalités

* **Commandes fluides :** Contrôle du serpent avec les touches directionnelles du clavier.
* **Mécanique de croissance :** Chaque fruit mangé augmente la taille du serpent et fait progresser le score.
* **Traversée des bordures (Wrap-around) :** Le serpent traverse les bords de l'écran pour réapparaître de l'côté opposé.
* **Système de score :** Affichage du score actuel en temps réel.
* **Gestion du Game Over :** Écran de fin de partie lorsque le serpent se mord la queue, avec possibilité de recommencer.

---

## 🛠️ Prérequis et Installation

Assurez-vous d'avoir **Python** installé sur votre machine (version 3.x recommandée).

1. Clonez ce dépôt ou téléchargez les fichiers du projet.
2. Installez la bibliothèque **Pygame** via votre terminal ou invite de commande :
   ```bash
   pip install pygame
