# IA Pau Data Battle

## Quick start
```
docker start <nom du conteneur mysql>
cd backend
venv/bin/uvicorn main:app --reload
```

## API

L'API est essentielle dans cette application. C'est elle qui va se connecter à la base de données et seulement elle, cela permet de factoriser le code, que l'on puisse tous bénéficier des données qu'un autre utilise en une seule fois sans avoir à écrire tous notre requête SQL. Cela permet aussi d'uniformiser les données et toujours avoir le même format JSON.

### Lancer l'API en mode développement (1ère fois)

1. Créer un environnement virtuel Python (à faire seulement la première fois):

```shell
cd backend
python3 -m venv venv 
```

2. Activer l'environnement Python :
```shell
source venv/bin/activate
```

3. Installer les dépendances :
```shell
pip install -r requirements.txt
```

4. Installer le modèle spaCy pour le français :
```shell
python3 -m spacy download fr_core_news_sm
```

5. Lancer le serveur Python :
```shell
uvicorn main:app --reload
```

Cela va lancer un serveur Python grâce à Uvicorn sur le port 8000.

### Lancer l'API en mode développement (! seulement si le fichier requirements.txt n'a pas changé !)

```shell
cd backend
venv/bin/uvicorn main:app --reload
```

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

## Frontend

Créer un fichier `.env` dans le dossier `frontend` dont le contenu est le suivant :
```
REACT_APP_PROXY=http://localhost:8000
```

```shell
cd frontend
```

Installation des dépendances :
```shell
npm install
```

Lancer le serveur en mode de développement :
```shell
npm start
```

Pour accéder à l'application, accédez à http://localhost:3000