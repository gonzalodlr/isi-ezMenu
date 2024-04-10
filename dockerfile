FROM python:3.10

# Crea la estructura de carpetas necesaria
RUN mkdir -p /isi-ezMenu/backend

# Establece el directorio de trabajo en /isi-ezMenu
WORKDIR /isi-ezMenu

# Copia todos los archivos al directorio /isi-ezMenu
COPY . .

# Instala las dependencias
RUN pip install -r requirements.txt

# Cambia al directorio backend
WORKDIR /isi-ezMenu/backend

# Establece la variable de entorno FLASK_APP
ENV FLASK_APP=app.py

# Expone el puerto 5000
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0"]
