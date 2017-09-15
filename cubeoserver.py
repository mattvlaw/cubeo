from flask import Flask
from cubeo import Cubeo


control_panel = '''<html>
	<head>
		<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.js"></script>
	</head>
	<body>
		<script type="text/javascript">
			var step = 50;
			$(document).keypress(function(event) {
				var char = event.charCode;
				var one = $("#one");
				var two = $("#two");
				var three = $("#three");
				var four = $("#four");
				var currentVal;

				switch(char){
					case 113: //char = q
						currentVal = parseInt(one.val());
						one.val(currentVal+=step);
						setSpeed(2,currentVal);
						break;
					case 97: //char = a
						currentVal = parseInt(one.val());
						one.val(currentVal-=step);
						setSpeed(2,currentVal);
						break;
					case 122: //char = z
						one.val(0);
						setSpeed(2,0);
						break;
					case 101: //char = e
						currentVal = parseInt(two.val());
						two.val(currentVal+=step);
						setSpeed(4,currentVal);
						break;
					case 100: //char = d
						currentVal = parseInt(two.val());
						two.val(currentVal-=step);
						setSpeed(4,currentVal);
						break;
					case 99: //char = c
						two.val(0);
						setSpeed(4,0);
						break;
					case 112: //char = p
						currentVal = parseInt(three.val());
						three.val(currentVal+=step);
						setSpeed(3,currentVal);
						break;
					case 108: //char = l
						currentVal = parseInt(three.val());
						three.val(currentVal-=step);
						setSpeed(3,currentVal);
						break;
					case 44: //char = ,
						three.val(0);
						setSpeed(3,0);
						break;
					case 93: //char = ]
						currentVal = parseInt(four.val());
						four.val(currentVal+=step);
						setSpeed(5,currentVal);
						break;
					case 39: //char = '
						currentVal = parseInt(four.val());
						four.val(currentVal-=step);
						setSpeed(5,currentVal);
						break;
					case 47: //char = /
						four.val(0);
						setSpeed(5,0);
						break;
				}
			});

			function setSpeed(servo, speed) {
				console.log("New Speed");
				if(speed != 0){
					$.get("http://cubeo.ngrok.io/startpanel?panel=" + servo + "&speed=" + speed, function(response){
						console.log(response);
					});
				}
				else{
					$.get("http://cubeo.ngrok.io/stoppanel?panel=" + servo, function(response){
						console.log(response);
					});
				}
			}
		</script>
		<h3>%s</h3>
		<ul>
			<li>2<input id="one" type="range" min="0" max="7500" step="10" value="0" onchange="setSpeed(2, this.value)"></li>
			<li>4<input id="two" type="range" min="0" max="7500" step="10" value="0" onchange="setSpeed(4, this.value)"></li>
			<li>3<input id="three" type="range" min="0" max="7500" step="10" value="0" onchange="setSpeed(3, this.value)"></li>
			<li>5<input id="four" type="range" min="0" max="7500" step="10" value="0" onchange="setSpeed(5, this.value)"></li>
			<li><a href="http://cubeo.ngrok.io/wave">Do the Wave</a></li>
			<li><a href="http://cubeo.ngrok.io/breatheslow">Breathe Slowly</a></li>
			<li><a href="http://cubeo.ngrok.io/breathemedium">Breathe Normally</a></li>
			<li><a href="http://cubeo.ngrok.io/breathefast">Breath Fast</a></li>
			<li><a href="http://cubeo.ngrok.io/breatheveryfast">Breathe VERY FAST</a></li>
			<li><a href="http://cubeo.ngrok.io/breathestop">Stop Breathing</a></li>
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
