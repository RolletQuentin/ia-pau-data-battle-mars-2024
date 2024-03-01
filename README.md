# IA Pau Data Battle

## Connexion à la base de données

Pour se connecter à la base de données, nous utilisons un conteneur Docker. Lors du développement, il suffit de run le conteneur Docker de MySQL. Voici comment faire.

### Construire l'image

Cette étape est à faire seulement la première fois, où s'il y a une modification dans le Dockerfile (Vous serez mis au courant).

1. Aller dans le dossier mysql
```shell
cd mysql
```

2. Construire l'image Docker
```shell
docker build -t ia-pau-data-battle-mars-2024-mysql .
```

Vous pouvez remplacer `ia-pau-data-battle-mars-2024-mysql` par le nom que vous voulez.

### Run l'image

Pour lancer la conteneur Docker :
```shell
docker run -d -p 3306:3306 ia-pau-data-battle-mars-2024-mysql
```

Paramètres :
- `-d` : detach mode -> lancer le conteneur en arrière plan (non-obligatoire)
- `-p` : port -> chosir le port sur lequel accéder à l'application

### Visualisation des données

Pour visualiser la base de donnée, il faut installer un autre logiciel. On va utiliser MySQL Workbench, libre à vous d'utiliser autre chose.

Installation (pour un système Arch, désolé Val) :
```shell
sudo pacman -S mysql-workbench 
```

Lancer l'application :
```shell
mysql-workbench
```

Une fois sur l'application, connectez-vous à la database grâce au credentials suivant :
- username : myuser
- password : mypassword

Il faut ensuite aller dans l'onglet `Structures` et bienvenue sur la base de données !