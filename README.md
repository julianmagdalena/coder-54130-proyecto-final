# coder-54130-proyecto-final
 
 julian magdalena opvision@gmail.com

# comandos
1. crear proyecto django
    ```bash
    django-admin startprojet "nombre del proyecto"
    ```

2. testear servidor
   ```bash
    python3 manage.py runserver
    ```
3. crear una "application" dentro de mi proyecto
    ```bash
    python3 manage.py startapp "nombre de la app"
    ```
4. creamos un archivo urls.py en <"coder_python/entrega_final/Plataforma/book">

# templetes

1. crear un <templete> y guardarlo en el lugar adecuado
2. utilizar la funcion <render>

## modelos

despues de agregar o modificar un modelo en 'models.py' tenemos que correr 2 comandos:

1. 'python3 manage.py makemigrations'
2. 'python3 manage.py migrate'