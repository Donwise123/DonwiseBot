from flask import Flask from threading import Thread

app = Flask(name)

@app.route('/') def home(): return "DonwiseBot is running!"

def run(): app.run(host='0.0.0.0', port=8080)

def keep_alive(): t = Thread(target=run) t.start()

