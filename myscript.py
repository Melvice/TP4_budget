import os

#remarque pour entrer manuellement les commits dans 
#la ligne de commande, on pourrait plutôt faire comme suit: 
#import sys
#bad_commit = sys.argv[1]
#good_commit = sys.argv[2]

#Définition des commits
bad_commit = "c1a4be04b972b6c17db242fc37752ad517c29402"
good_commit = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"
#Excéctution des commandes git bisect
os.system('git bisect start %s %s' % (bad_commit, good_commit))
os.system('git bisect run python manage.py test ')
os.system('git bisect reset')

 
