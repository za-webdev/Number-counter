from flask import Flask ,render_template,request,redirect,session
app=Flask(__name__)

app.secret_key = 'ThisIsSecret'
app.number=0

@app.route('/')
def input():

	session['number']+=1

	return render_template('list.html', number=session['number'])


@app.route('/increment', methods=['post'])
def counter():

	session['number']+=1

	return redirect('/')


@app.route('/reset', methods=['post'])
def reset():

	session['number']=0

	return redirect("/")
	
	


app.run(debug=True)