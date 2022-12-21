-- settings.sql
CREATE DATABASE nostaldja;
CREATE USER tunruser WITH PASSWORD 'tunr';
GRANT ALL PRIVILEGES ON DATABASE nostaldja TO tunruser;
--only needed if -U postgres is needed
GRANT postgres TO tunruser;