from flask import Flask, render_template, send_from_directory, redirect, request, jsonify, url_for, session
from flask_ngrok import run_with_ngrok
import os
import webbrowser
import json
import logging


# Текущая директория, где находится скрипт
basedir = os.path.abspath(os.path.dirname(__file__))

# Абсолютные пути к директориям шаблонов и статики
template_dir = os.path.join(basedir, 'windows')
static_dir = os.path.join(basedir, 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
run_with_ngrok(app)

logging.basicConfig(level=logging.DEBUG)

users_file = os.path.join(static_dir, 'users.json')

try:
    with open(users_file) as f:
        users = json.load(f)
except Exception as e:
    app.logger.error(f"Error loading users.json: {e}")
    users = {}

# Проверка наличия файлов в директории шаблонов
app.logger.info(f"Contents of template directory ({template_dir}): {os.listdir(template_dir)}")

@app.route('/')
def index():
    if 'user' not in session:
        session['user'] = 'guest'
    return render_template('index.html', current_user=session['user'])

@app.route('/<template_name>.html')
def render_template_route(template_name):
    try:
        return render_template(f'{template_name}.html')
    except Exception as e:
        app.logger.error(f"Error rendering template {template_name}: {e}")
        return "Template rendering error", 500
    
@app.route('/settings.html')
def settings():
    return render_template('settings.html')

@app.route('/backup.html')
def backup():
    return render_template('backup.html')

@app.route('/contacts.html')
def contacts():
    return render_template('contacts.html')

@app.route('/engineeringMenu.html')
def engineeringMenu():
    return render_template('engineeringMenu.html')

@app.route('/installationScheduler.html')
def installationScheduler():
    return render_template('installationScheduler.html')

@app.route('/journal.html')
def journal():
    return render_template('journal.html')

@app.route('/keypad.html')
def keypad():
    return render_template('keypad.html')

@app.route('/monitoring.html')
def monitoring():
    return render_template('monitoring.html')

@app.route('/panelSettings.html')
def panelSettings():
    return render_template('panelSettings.html')

@app.route('/pid.html')
def pid():
    return render_template('pid.html')

@app.route('/pumps.html')
def pumps():
    return render_template('pumps.html')

@app.route('/stationSettings.html')
def stationSettings():
    return render_template('stationSettings.html')

@app.route('/trendsOnline.html')
def trendsOnline():
    return render_template('trendsOnline.html')


@app.route('/scriptKeypad.js/<filename>')
def criptKeypad(filename):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(os.path.join(root_dir, 'static'), filename)


@app.route('/scriptMain.js/<filename>')
def scriptMain(filename):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(os.path.join(root_dir, 'static'), filename)


@app.route('/usersJs.js/<filename>')
def usersJs(filename):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(os.path.join(root_dir, 'static'), filename)



@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']
        if username in users and users[username]['password'] == password:
            session['user'] = username
            return jsonify(success=True, role=users[username]['role'], level=users[username]['level'])
        return jsonify(success=False)
    except Exception as e:
        app.logger.error(f"Error during login: {e}")
        return jsonify(success=False)

@app.route('/logout', methods=['POST'])
def logout():
    session['user'] = 'guest'
    return redirect(url_for('index'))


if not os.path.isfile(os.path.join(template_dir, 'index.html')):
    app.logger.error("index.html not found in templates directory")
else:
    app.logger.info("index.html found in templates directory")

if __name__ == "__main__":
    app.debug = True
    app.logger.setLevel(logging.DEBUG)
    webbrowser.open_new('http://127.0.0.1:5000/')
    app.run()