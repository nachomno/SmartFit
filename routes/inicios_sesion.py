from flask import Blueprint, request,session, flash, redirect
import sqlite3

# Definimos el blueprint para las rutas de inicios y cierre de sesiones
inicios_sesion_bp = Blueprint('inicios y cierre de sesion', __name__)

# Rutas para procesar los inicios de sesión (usuario común y profesional)
@inicios_sesion_bp.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    email = request.form['email']
    password = request.form['password']

    # Conectar a la base de datos
    conn = sqlite3.connect('smartfit.db')
    c = conn.cursor()

    # Buscar el correo en la base de datos
    c.execute("SELECT id_usuario, nombre, mail, contraseña FROM Usuarios WHERE mail = ?", (email,))
    usuario = c.fetchone()

    conn.close()

    # Verificar si el correo existe y la contraseña es correcta
    if usuario and usuario[3] == password:  # Comparar la contraseña
        # Iniciar sesión guardando el nombre del usuario en la sesión
        session['id_usuario'] = usuario[0]
        session['nombre'] = usuario[1]
        session['tipo_usuario'] = 'usuario'  # Identificar como usuario regular <------------------
        return redirect('/')  # Redirigir a la página de bienvenida
    else:
        flash('Correo o contraseña incorrectos')  # Mensaje de error
        return redirect('/')  # Volver al index si falló el inicio de sesión
    
@inicios_sesion_bp.route('/iniciar_sesion_profesional', methods=['POST'])
def iniciar_sesion_profesional():
    email = request.form['email']
    password = request.form['password']

    conn = sqlite3.connect('smartfit.db')
    c = conn.cursor()

    # Buscar el correo en la base de datos de profesionales
    c.execute("SELECT id_profesional, nombre, mail, contraseña FROM Profesionales WHERE mail = ?", (email,))
    profesional = c.fetchone()

    conn.close()

    # Verificar si el correo existe y la contraseña es correcta
    if profesional and profesional[3] == password:  # Comparar la contraseña
        # Iniciar sesión guardando el nombre del profesional y tipo en la sesión
        session['id_profesional'] = profesional[0]
        session['nombre'] = profesional[1]
        session['tipo_usuario'] = 'profesional'  # Identificar como profesional
        session['es_profesional'] = True  # Añadir la variable para ocultar secciones para profesionales
        return redirect('/')  # Redirigir a la página de bienvenida
    else:
        flash('Correo o contraseña incorrectos')  # Mensaje de error
        return redirect('/')  # Volver al index si falló el inicio de sesión

# Ruta para cerrar sesión
@inicios_sesion_bp.route('/cerrar_sesion')
def cerrar_sesion():
    session.clear()  # Limpia todos los datos de la sesión
    return redirect('/')