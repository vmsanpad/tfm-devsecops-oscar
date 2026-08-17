# Fallo 1: Uso de tag no específico/inseguro (DL3006 / DL3007)
FROM ubuntu:latest

# Fallo 2: Ejecución como root por omisión y sin limpiar caché de apt (DL3008 / DL3009)
RUN apt-get update && apt-get install -y curl

# Fallo 3: Uso de instrucción ADD en vez de COPY (DL3020)
ADD app.py /app/app.py

CMD ["python3", "/app/app.py"]
