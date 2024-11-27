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


### API:
http://127.0.0.1:8000/api/v1/

### Documentacion en swagger:
http://127.0.0.1:8000/docs


## Como usar
### Agregar libros
Realizar una peticion POST con la informacion del libro a agregar, al siguiente endpoint:
/api/v1/books

El cuerpo de la misma debe satisfacer el siguiente formato:
```json
{
  "id": int,
  "title": string,
  "author": string,
  "price": float,
  "is_available": boolean
}
```

### Obtener un libro
Realizar una request GET al siguiente endpoint:
/api/v1/books/{id}

Reemplazando {id} por el id del libro a obtener.

### Actualizar un libro
Realizar una peticion PUT al siguiente endpoint:
/api/v1/books/{id}

El cuerpo de la peticion debe contener el siguiente formato:
```json
{
  "id": int,
  "title": string,
  "author": string,
  "price": float,
  "is_available": boolean
}
```

Reemplazando {id} por el id del libro a obtener.

### Eliminar un libro
Realizar una peticion DELETE al endpoint:
/api/v1/books/{id}

Si el id existe, el libro sera eliminado.

