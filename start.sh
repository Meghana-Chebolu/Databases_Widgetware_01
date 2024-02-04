#Docker compose commands
docker compose build
docker compose up
#Open new terminal
docker ps
#Replace the below CONTAINER_ID with yours
docker cp "Features data set.csv" CONTAINER_ID:/Features\ data\ set.csv
docker-compose exec cassandra /bin/bash
cqlsh
CREATE KEYSPACE data
 WITH REPLICATION = {  
  'class' : 'NetworkTopologyStrategy',  
  'datacenter1' : 1  
  } ;

#Open new terminal
python main.py
COPY data.featurea (Store, Date, Temperature, Fuel_Price, MarkDown1, MarkDown2, MarkDown3, MarkDown4, MarkDown5, CPI, Unemployment, IsHoliday)
   ... FROM '/Features data set.csv' WITH DELIMITER=',' AND HEADER = TRUE AND NULL='NA';
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
