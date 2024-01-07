# MIDLCOIN

 Ce projet a pour but de réaliser une simulation de cryptomonnaie (Midlcoin) noté ϻ.
## On y implémente une version simplifiée du bitcoin qui comporte :
  - Des transactions signées
  - Des blocs de transactions pouvant être minés
  - Une blockchain comme une liste de blocs
  - Une interface permettant d'utiliser la simulation
## Quelques fonctionnalités supplémentaires que nous avons implémenté :
  - Augmentation de la taille du hash en 256 bits
  - Des récompenses pour les mineurs avec système de halving
  - Augmentation de la difficulté de minage
  - Une initialisation de la simulation avec une blockchain vide
  - Les mineurs peuvent être en concurrence et miner en même temps grâce au threading
## Comment utiliser notre simulation
Premièrement, installer le dossier code et éxécuter le fichier main.py.
Si tout se passe bien, une interface devrait se lancer, vous pourrez créer des utilisateurs, vous connecter à leur profils via leur identifiant et réaliser des virements, créer des blocs, les miner, etc...
A noter, la simulation démarre sans aucun utilisateur, et chaque utilisateur créé n'aura aucun MIDLCOIN, il faudra en miner (avec un bloc vide) avant de pouvoir réaliser des virements.
##### Ce projet est réalisé par Damien Bonzom et Martin Sueur
