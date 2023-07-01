import json
from flask import Flask, render_template, request, jsonify, send_from_directory
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    #abrir index.html sem usar o comando render_template('index.html')
    if os.listdir('cordova_projects') == []:
        return Project()
    else:
        return ListProjects()

@app.route('/CreateProject')
def CreateProject():
    return render_template('CreateProject.html')
@app.route('/ListProjects')
def ListProjects():
    data = os.listdir('cordova_projects')

    return render_template('ListProjects.html', projects=data)
@app.route('/Project', methods=['GET'])
def Project():
    data_result = {
        'name': request.args.get('name'),
        'platforms': {
            'browser': False,
        }
    }
    name = request.args.get('name')

    #Verificar se pasta existe
    if(os.path.exists(f'cordova_projects/{name}/platforms/browser/') ):
        data_result['platforms']['browser'] = True
    else:
        data_result['platforms']['browser'] = False

    if(os.path.exists(f'cordova_projects/{name}/platforms/android/') ):
        data_result['platforms']['android'] = True
    else:
        data_result['platforms']['android'] = False

    if(os.path.exists(f'cordova_projects/{name}/platforms/electron/') ):
        data_result['platforms']['electron'] = True
    else:
        data_result['platforms']['electron'] = False


    project_config = data_result
    return render_template('Project.html', name=request.args.get('name'), project_config=project_config)

  
    



   


@app.route('/create_project', methods=['POST'])
def create_project():
    project = request.form['project']
    assinatura = request.form['assinatura']
    pasta = request.form['pasta']
    
    # Comando para criar o projeto Cordova
    cordova_cmd = f'cordova create cordova_projects/{project} {assinatura} {pasta}'

    try:
        # Executa o comando cordova create
        subprocess.run(cordova_cmd, shell=True, check=True)

        # Resto do código para fazer o upload do APK e retornar o link
        return jsonify({'success': True})

    except subprocess.CalledProcessError as e:
        return jsonify({'error': str(e)})

@app.route('/list_projects')
def list_projects():
    projects = os.listdir('cordova_projects')
    return jsonify(projects)

@app.route('/project', methods=['GET'])
def get_project():
    name = request.args.get('name')
    return render_template('project.html', name=name)

@app.route('/cmd_cordova', methods=['POST'])
def run_cordova_cmd():
    cmd = request.form['cmd']
    name = request.form['name']

    cordova_cmd = f'cd cordova_projects/{name} && {cmd}'

    try:
        # Executa o comando cordova run browser
        process = subprocess.Popen(cordova_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Obtém a saída e o erro do processo
        stdout, stderr = process.communicate()

        # Decodifica a saída e o erro para texto
        stdout = stdout.decode('utf-8')
        stderr = stderr.decode('utf-8')

        # Verifica se houve algum erro
        if process.returncode != 0:
            return jsonify({'error': f'Error executing command: {cmd}', 'stderr': stderr})

        # Retorna a saída do comando
        return jsonify({'success': True, 'cmd': cordova_cmd, 'stdout': stdout, 'stderr': stderr})

    except Exception as e:
        return jsonify({'error': str(e)})



@app.route('/get_info_project', methods=['GET'])
def get_info_project():
    name = request.args.get('name')

    data_result = {
        'name': name,
        'platforms': {
            'browser': False,
        }
    }

    if(os.listdir('cordova_projects/'+name+'/platforms/browser') == []):
        data_result['platforms']['browser'] = False
    else:
        data_result['platforms']['browser'] = True

    return jsonify(data_result)



@app.route('/config_project', methods=['GET'])
def config_project():
    name = request.args.get('name')
    options = request.args.get('options')
    options = json.loads(options)
   
    data_result = []

  
    
    if(options['platforms']['browser'] == True):
        cordova_cmd = f'cd cordova_projects/{name} && cordova platform add browser'

        try:
            # Executa o comando cordova run browser
            process = subprocess.Popen(cordova_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Obtém a saída e o erro do processo
            stdout, stderr = process.communicate()

            # Decodifica a saída e o erro para texto
            stdout = stdout.decode('utf-8')
            stderr = stderr.decode('utf-8')

            # Verifica se houve algum erro
            if process.returncode != 0:
                data_result.append({'error': f'Error executing command: {cordova_cmd}', 'stderr': stderr})
                data_result.append({'error': f'Error executing command: {cordova_cmd}', 'stderr': stderr})
            else:
                # Retorna a saída do comando
                data_result.append({'success': True, 'cmd': cordova_cmd, 'stdout': stdout, 'stderr': stderr})
                data_result.append({'success': True, 'cmd': cordova_cmd, 'stdout': stdout, 'stderr': stderr})

        except Exception as e:
            data_result.append({'error': str(e)})
            data_result.append({'error': str(e)})
    else:
        cordova_cmd = f'cd cordova_projects/{name} && cordova platform remove browser'

        try:
            # Executa o comando cordova run browser
            process = subprocess.Popen(cordova_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Obtém a saída e o erro do processo
            stdout, stderr = process.communicate()

            # Decodifica a saída e o erro para texto
            stdout = stdout.decode('utf-8')
            stderr = stderr.decode('utf-8')

            # Verifica se houve algum erro
            if process.returncode != 0:
                data_result.append({'error': f'Error executing command: {cordova_cmd}', 'stderr': stderr})
                data_result.append({'error': f'Error executing command: {cordova_cmd}', 'stderr': stderr})
            else:
                # Retorna a saída do comando
                data_result.append({'success': True, 'cmd': cordova_cmd, 'stdout': stdout, 'stderr': stderr})
                data_result.append({'success': True, 'cmd': cordova_cmd, 'stdout': stdout, 'stderr': stderr})

        except Exception as e:
            data_result.append({'error': str(e)})
            data_result.append({'error': str(e)})

    if(options['platforms']['android'] == True):
        cordova_cmd = f'cd cordova_projects/{name} && cordova platform add android'

        try:
            # Executa o comando cordova run browser
            process = subprocess.Popen(cordova_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Obtém a saída e o erro do processo
            stdout, stderr = process.communicate()

            # Decodifica a saída e o erro para texto
            stdout = stdout.decode('utf-8')
            stderr = stderr.decode('utf-8')

            # Verifica se houve algum erro
            if process.returncode != 0:
                data_result.append({'error': f'Error executing command: {cordova_cmd}', 'stderr': stderr})
                data_result.append({'error': f'Error executing command: {cordova_cmd}', 'stderr': stderr})
            else:
                # Retorna a saída do comando
                data_result.append({'success': True, 'cmd': cordova_cmd, 'stdout': stdout, 'stderr': stderr})
                data_result.append({'success': True, 'cmd': cordova_cmd, 'stdout': stdout, 'stderr': stderr})

        except Exception as e:
            data_result.append({'error': str(e)})
            data_result.append({'error': str(e)})
    else:
        cordova_cmd = f'cd cordova_projects/{name} && cordova platform remove android'

        try:
            # Executa o comando cordova run browser
            process = subprocess.Popen(cordova_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Obtém a saída e o erro do processo
            stdout, stderr = process.communicate()

            # Decodifica a saída e o erro para texto
            stdout = stdout.decode('utf-8')
            stderr = stderr.decode('utf-8')

            # Verifica se houve algum erro
            if process.returncode != 0:
                data_result.append({'error': f'Error executing command: {cordova_cmd}', 'stderr': stderr})
                data_result.append({'error': f'Error executing command: {cordova_cmd}', 'stderr': stderr})
            else:
                # Retorna a saída do comando
                data_result.append({'success': True, 'cmd': cordova_cmd, 'stdout': stdout, 'stderr': stderr})
                data_result.append({'success': True, 'cmd': cordova_cmd, 'stdout': stdout, 'stderr': stderr})

        except Exception as e:
            data_result.append({'error': str(e)})
            data_result.append({'error': str(e)})

    if(options['platforms']['electron'] == True):
        cordova_cmd = f'cd cordova_projects/{name} && cordova platform add electron'

        try:
            # Executa o comando cordova run browser
            process = subprocess.Popen(cordova_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Obtém a saída e o erro do processo
            stdout, stderr = process.communicate()

            # Decodifica a saída e o erro para texto
            stdout = stdout.decode('utf-8')
            stderr = stderr.decode('utf-8')

            # Verifica se houve algum erro
            if process.returncode != 0:
                data_result.append({'error': f'Error executing command: {cordova_cmd}', 'stderr': stderr})
                data_result.append({'error': f'Error executing command: {cordova_cmd}', 'stderr': stderr})
            else:
                # Retorna a saída do comando
                data_result.append({'success': True, 'cmd': cordova_cmd, 'stdout': stdout, 'stderr': stderr})
                data_result.append({'success': True, 'cmd': cordova_cmd, 'stdout': stdout, 'stderr': stderr})

        except Exception as e:
            data_result.append({'error': str(e)})
            data_result.append({'error': str(e)})
    else:
        cordova_cmd = f'cd cordova_projects/{name} && cordova platform remove electron'

        try:
            # Executa o comando cordova run browser
            process = subprocess.Popen(cordova_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Obtém a saída e o erro do processo
            stdout, stderr = process.communicate()

            # Decodifica a saída e o erro para texto
            stdout = stdout.decode('utf-8')
            stderr = stderr.decode('utf-8')

            # Verifica se houve algum erro
            if process.returncode != 0:
                data_result.append({'error': f'Error executing command: {cordova_cmd}', 'stderr': stderr})
                data_result.append({'error': f'Error executing command: {cordova_cmd}', 'stderr': stderr})
            else:
                # Retorna a saída do comando
                data_result.append({'success': True, 'cmd': cordova_cmd, 'stdout': stdout, 'stderr': stderr})
                data_result.append({'success': True, 'cmd': cordova_cmd, 'stdout': stdout, 'stderr': stderr})

        except Exception as e:
            data_result.append({'error': str(e)})
            data_result.append({'error': str(e)})


        
    return jsonify(data_result)



if __name__ == '__main__':
    app.run()
