# Api de libros

## Primeros pasos
Clonar el repositorio.
```bash
git clone https://github.com/matias-ortubia/api-libros.git
````

Instalar las dependencias.
```bash
pip install -r requirements.txt
```

## Levantar el servidor
```bash
uvicorn app.main:app --reload
```

Luego, se podra acceder a las rutas:
http://127.0.0.1:8000/api/v1/books
http://127.0.0.1:8000/docs

