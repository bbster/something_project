--- DATABASE 생성
CREATE DATABASE someapi_postgresql;

--- User 생성
CREATE USER admin WITH PASSWORD 'password';
ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE admin WITH SUPERUSER;

--- DB에 대한 User 권한 부여
GRANT ALL PRIVILEGES ON DATABASE someapi_postgresql TO admin;