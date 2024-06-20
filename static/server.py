from flask import Flask, render_template, send_from_directory, redirect, request, jsonify, url_for
from flask_ngrok import run_with_ngrok
import os
import webbrowser
import json



app = Flask(__name__, template_folder='../windows', static_folder='../static')
run_with_ngrok(app)

@app.route('/')
def index():
    return render_template('index.html')

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

# Настройки станции

@app.route('/stSet_EmergencyMode.html')
def stSet_EmergencyMode():
    return render_template('stSet_EmergencyMode.html')

@app.route('/stSet_EngineParameters.html')
def stSet_EngineParameters():
    return render_template('stSet_EngineParameters.html')

@app.route('/stSet_Options.html')
def stSet_Options():
    return render_template('stSet_Options.html')

@app.route('/stSet_PumpSettings.html')
def stSet_PumpSettings():
    return render_template('stSet_PumpSettings.html')

@app.route('/stSet_SensorSettings.html')
def stSet_SensorSettings():
    return render_template('stSet_SensorSettings.html')

@app.route('/stSet_PumpAdd.html')
def stSet_PumpAdd():
    return render_template('stSet_PumpAdd.html')

@app.route('/stSet_PumpRemove.html')
def stSet_PumpRemove():
    return render_template('stSet_PumpRemove.html')

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

@app.route('/dataRandomizer.py')
def randomizer(filename):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(os.path.join(root_dir, 'static'), filename)

# рандомайзер графика
os.system("python dataRandomizer.py")

if __name__ == "__main__":
    webbrowser.open_new('http://127.0.0.1:5000/')
    app.run()