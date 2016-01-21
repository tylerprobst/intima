from flask import Flask, Blueprint, render_template, redirect, session, g, request, send_from_directory

application = Flask(__name__)
application.config.from_object('config')

@application.route('/')
def index():
	return render_template('index.html')

@application.route('/assets/<path:path>')
def assets(path):
	return send_from_directory('assets', path)

@application.route('/uploads/<path:path>')
def uploads(path):
	return send_from_directory('uploads', path)

if __name__ =='__main__':
	application.run()