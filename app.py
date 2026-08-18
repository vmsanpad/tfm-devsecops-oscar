import os
import subprocess

# Corrección 1: Las credenciales se leen de variables de entorno, no en texto plano
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", "default_safe_value")

# Corrección 2: Ejecución segura pasando argumentos como lista y sin shell=True
def ejecutar_comando():
    subprocess.run(["echo", "Módulo ejecutado correctamente"], check=True)

if __name__ == "__main__":
    print("Módulo de pruebas corregido")
    ejecutar_comando()
