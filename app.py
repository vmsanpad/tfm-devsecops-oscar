import subprocess

# Fallo 1: Secreto expuesto en texto plano (Detectado por Gitleaks)
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE1234567890abcdef"

# Fallo 2: Uso inseguro de shell=True en subprocesos (Detectado por Bandit - B602)
def ejecutar_comando(comando):
    subprocess.Popen(comando, shell=True)

if __name__ == "__main__":
    print("Módulo de pruebas")
    ejecutar_comando("ls -la")
