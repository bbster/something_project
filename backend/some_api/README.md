# Spec
---
- FastAPI
- Uvicorn
- Postgresql
- Docker
---
### set up package
- poetry add fastapi
- poetry add hypercorn
- poetry add uvicorn

---
### run server
- uvicorn main:app --reload

---
### DB Docker setting
- cd scripts
- sh ./fastapi_postgresql.sh -> docker postgresql set up
- sh ./create_database.sh -> docker postgresql db 생성
- sh ./connect_docker_postgresql.sh -> docker postgresql 접속
