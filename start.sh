#Docker compose commands
docker compose build
docker compose up

#Getting into the Cassandra Docker container
docker-compose exec cassandra /bin/bash
cqlsh
CREATE KEYSPACE IF NOT EXISTS my_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
USE my_keyspace;
CREATE TABLE IF NOT EXISTS students (id INT,name TEXT,PRIMARY KEY (id));
DESCRIBE tables;
INSERT INTO students (id, name) VALUES (1, 'John Doe');
SELECT * FROM students;

#Git
git add .
git commit -m ""
git push