from flask import Flask, request, render_template, redirect, url_for, flash, session, jsonify
import sqlite3
from datetime import datetime
from routes.entrenamientos import entrenamientos_bp
from routes.registros import registros_bp
from routes.inicios_sesion import inicios_sesion_bp
from routes.perfiles_usuarios import perfiles_bp

app = Flask(__name__) # Crea una instancia de la clase Flask, que es la App web en sí misma
app.secret_key = 'smart_fit_2024' # Utilizada por Flask para gestionar sesiones y mensajes flash

#----RUTAS------------------------------------------------------------------------------

# Ruta asociada a la URL raíz (index.html)
@app.route('/') 
def index():
    if 'nombre' in session: # Verifica si existe la clave "nombre" en la sesión (si hay un usuario logueado)
        usuario_logueado = session['nombre'] # Se asigna el nombre guardado en la clave de la sesión en la variable
    else: # Si no hay clave en la sesión, es porque el usuario no inició sesión
        usuario_logueado = None
    return render_template('index.html', usuario_logueado=usuario_logueado) # Renderiza la plantilla index.html y pasa la variable.

# Registra el blueprint de los registros
app.register_blueprint(registros_bp)

# Registra el blueprint de inicios y cierre de sesion
app.register_blueprint(inicios_sesion_bp)
    
# Registra el blueprint de entrenamientos
app.register_blueprint(entrenamientos_bp)

# Registra el blueprint de perfiles
app.register_blueprint(perfiles_bp)

if __name__ == '__main__':
    app.run(debug=True)