import subprocess

comando_npm = 'cd cordova_projects/teste && cordova platforms'

resultado = subprocess.run(comando_npm, shell=True, capture_output=True, text=True)

retorno = resultado.stdout

print(retorno)
