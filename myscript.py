import os
import sys

# Définition de la commande à exécuter
command = "git bisect start c1a4be04b972b6c17db242fc37752ad517c29402 e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

# Exécution de la commande
os.system(command)

# Définition de la commande à exécuter
command = "git bisect run python manage.py test"

# Exécution de la commande
os.system(command)

# Définition de la commande à exécuter
command = "git bisect reset"

# Exécution de la commande
os.system(command)