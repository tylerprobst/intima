from flask import Flask, Blueprint, render_template, redirect, session, g, request, send_from_directory

application = Flask(__name__)
application.config.from_object('config')

@application.route('/')
def index():
	return render_template('index.html')

if __name__ =='__main__':
	application.run()