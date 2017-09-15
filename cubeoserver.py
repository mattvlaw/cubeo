from flask import Flask
from cubeo import Cubeo


control_panel = '''<html>
						<body>
						<h3>%s</h3>
						<ul>
						<li><input type="range" min="0" max="7500" step="10"></li>
						<li><input type="range" min="0" max="7500" step="10"></li>
						<li><input type="range" min="0" max="7500" step="10"></li>
						<li><input type="range" min="0" max="7500" step="10"></li>
						<li><a href="/wave">Do the Wave</a></li>
						<li><a href="/breatheslow">Breathe Slowly</a></li>
						<li><a href="/breathemedium">Breathe Normally</a></li>
						<li><a href="/breathefast">Breath Fast</a></li>
						<li><a href="/breatheveryfast">Breathe VERY FAST</a></li>
						<a href="/breathestop">Stop Breathing</a></li>
						</ul>
						</body>
					<html>
'''

app = Flask(__name__)
cubeo = Cubeo("COM12")

@app.route("/")
def hello():
	return control_panel%"Welcome, choose a command:"
@app.route("/startpanel")
def startpanel():
	speed = int(request.args.get("speed"))
	servo = int(request.args.get("panel"))
	cubeo.start_panel(servo,speed)
	return "Panel: "+str(servo)+" Speed: "+str(speed)
@app.route("/stoppanel")
def stoppanel():
	servo = int(request.args.get("panel"))
	cubeo.stop_panel(servo)
	return "Panel: "+str(servo)+" Speed: 0"

@app.route("/wave")
def wave():
	cubeo.do_the_wave()
	return control_panel%"Doing the wave. Choose another command:"

@app.route("/breathefast")
def breathefast():
	cubeo.breathe_fast()
	return control_panel%"Breathing fast. Choose another command:"

@app.route("/breatheslow")
def breatheslow():
	cubeo.breathe_slow()
	return control_panel%"Breathing slowly. Choose another command:"

@app.route("/breathestop")
def breathestop():
	cubeo.stop_breathing()
	return control_panel%"Stopped breathing. Choose another command:"

@app.route("/breathemedium")
def breathemedium():
	cubeo.breathe_medium()
	return control_panel%"Breathing. Choose another command:"

@app.route("/breatheveryfast")
def breatheveryfast():
	cubeo.breathe_very_fast()
	return control_panel%"HYPERVENTILATING!!!!. PLEASE choose another command:"

if __name__ == "__main__":
	app.run()
