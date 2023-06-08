# Usa la imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos requeridos a /app
COPY src/app.py /app
COPY src/templates /app/templates

# Instala las dependencias de la aplicación Flask
RUN pip install flask requests

# Expone el puerto 8080 (el mismo que se utiliza en app.py)
EXPOSE 4000

# Define el comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
