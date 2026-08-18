# Corrección 1: Versión fija y específica en lugar de latest
FROM ubuntu:22.04

# Corrección 2: Instalación limpia sin paquetes recomendados y purgando listas temporales
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    python3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Corrección 3: Uso de COPY en lugar de ADD
COPY app.py /app/app.py

# Corrección 4: Uso de usuario no privilegiado
USER 1000

CMD ["python3", "/app/app.py"]
