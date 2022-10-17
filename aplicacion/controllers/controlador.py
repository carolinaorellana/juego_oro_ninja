from aplicacion import app
from flask import Flask, render_template, render_template, request, redirect, session
import random

@app.route('/')
def inicio():
    if 'oro' in session:
        # print(session['oro'])
        # print(session['actividad'])
        # print(session['contador'])
        # print(session['estado'])
        return render_template('index.html')
    else:
        session['estado']="1"
        session['contador'] = 15
        session['actividad']=[]
        session['oro'] = 0
        return render_template('index.html')

@app.route("/process_money", methods=['POST'])
def procesando_oro():

    #primero: si tienes mas de 199  oros y tienes intentos mayores a 0
    if session['oro']>199  and session['contador'] >0:
        session['estado']="3"
    elif session['oro']<200 and session['contador'] >1:
        if request.form['categoria'] == "granja":
            random1=random.randint(10, 20)
            session['oro'] += random1
            session['actividad'].append(f"<p class='text-success fw-bold'> Ganaste {random1} de oro</p>")
            session['contador'] -=1
        elif request.form['categoria'] == "cueva":
            random2=random.randint(5, 10)
            session['oro'] += random2
            session['actividad'].append(f"<p class='text-success fw-bold'> Ganaste {random2} de oro </p>")
            session['contador'] -=1
        elif request.form['categoria'] == "casa":
            random3=random.randint(2, 5)
            session['oro'] += random3
            session['actividad'].append(f"<p class='text-success fw-bold'> Ganaste {random3} de oro</p>")
            session['contador'] -=1
        else:
            random4=random.randint(-50, 50)
            session['oro'] += random4
            session['contador'] -=1
            if random4==0:
                session['actividad'].append("<p class='text-secondary fw-bold'>0 de oro, no pierdes ni ganas!</p>")
            if random4<0:
                session['actividad'].append(f"<p class='text-danger fw-bold'> Perdiste {random4} de oro</p>")
            else:
                session['actividad'].append(f"<p class='text-success fw-bold'>Ganaste {random4} de oro </p>")
    else:
        session['estado']="2"
    return redirect('/')

@app.route('/destruir_sesion', methods=['POST'])
def destruir_sesion():
    session.clear()
    return redirect('/')