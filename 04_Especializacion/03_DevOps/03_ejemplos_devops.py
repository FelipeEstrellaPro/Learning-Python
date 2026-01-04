import argparse
import subprocess
import shutil
from pathlib import Path
from datetime import datetime

# 1. Configurar Argumentos (CLI)
parser = argparse.ArgumentParser(description="Herramienta de Backup Automático")
parser.add_argument("directorio", help="Directorio a respaldar")
parser.add_argument("--ext", default=".txt", help="Extension de archivos a buscar")

# Si se ejecuta como script
if __name__ == "__main__":
    args = parser.parse_args()
    
    source_dir = Path(args.directorio)
    if not source_dir.exists():
        print(f"Error: El directorio {source_dir} no existe.")
        exit(1)

    print(f"--- Iniciando Backup de *{args.ext} en {source_dir} ---")

    # 2. Pathlib para encontrar archivos
    archivos = list(source_dir.glob(f"*{args.ext}"))
    print(f"Encontrados {len(archivos)} archivos.")

    if archivos:
        # Crear carpeta de backup con timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = source_dir / f"backup_{timestamp}"
        backup_dir.mkdir()

        # 3. Shutil para copiar
        for archivo in archivos:
            shutil.copy(archivo, backup_dir)
            print(f"Copiado: {archivo.name}")

        print(f"Backup completado en: {backup_dir}")
        
        # 4. Comprimir (shutil.make_archive)
        shutil.make_archive(str(backup_dir), 'zip', backup_dir)
        print(f"Archivo ZIP creado: {backup_dir}.zip")

    print("\n--- Estado del Sistema (Subprocess) ---")
    try:
        # Ejecutar comando 'git status' si es un repo, o 'dir' en windows
        # Usamos 'ver' (version) de windows como ejemplo seguro
        res = subprocess.run(["ver"], shell=True, capture_output=True, text=True)
        print(f"Output del sistema:\n{res.stdout}")
    except Exception as e:
        print(f"No se pudo ejecutar comando: {e}")
