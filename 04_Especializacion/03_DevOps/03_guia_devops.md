# DevOps y Automatización en Python

## 1. El Kit de Herramientas del SysAdmin
Python es el reemplazo moderno de Bash/Powershell para scripts complejos.

### `pathlib`
Olvídate de `os.path.join`. Usa `pathlib.Path`. Es orientado a objetos y multiplataforma.
`Path("carpeta") / "archivo.txt"`

### `subprocess`
Para ejecutar comandos del sistema (bash, git, docker).
`subprocess.run(["ls", "-l"], capture_output=True)`

### `argparse`
Para crear CLIs (Command Line Interfaces) profesionales con ayuda automática (`--help`).

## 2. Automatización Típica
1. Leer archivos de logs.
2. Conectarse a servidores (SSH con librerías como `paramiko` o `fabric`).
3. Mover/Copiar archivos (`shutil`).
4. Interactuar con APIs de Nube (AWS Boto3).
