#Distributed Databases 2021 - Two Phase Commit
#Implementation of two-phase commit protocol
[diagram](https://github.com/Kuzma2012/2021-k2_pc/master/diagram.jpg)
# Description
- PostgreSQL database in Docker container
- Implementation on Python using psycopg2
# How to start:
docker-compose up --build

postgres-fly-booking    port 5432
postgres-hotel-booking  port 5433
postgres-account        port 5434