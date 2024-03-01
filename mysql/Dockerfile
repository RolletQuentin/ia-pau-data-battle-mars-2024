# Utilisation de l'image officielle MySQL
FROM mysql:8.0

# Définition des variables d'environnement
ENV MYSQL_DATABASE=mydatabase \
    MYSQL_USER=myuser \
    MYSQL_PASSWORD=mypassword \
    MYSQL_ROOT_PASSWORD=rootpassword

# Copie du script SQL dans le conteneur
COPY db_backup_plateforme_2024-01-10_010001.sql /docker-entrypoint-initdb.d/

# Exposition du port MySQL
EXPOSE 3306

# Commande pour démarrer le serveur MySQL
CMD ["mysqld"]
