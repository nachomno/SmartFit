from flask import Blueprint, render_template, request,session
from datetime import datetime
import sqlite3

# Definimos el blueprint para las rutas de registros
registros_bp = Blueprint('registros', __name__)

# Rutas asociadas a las páginas de registro
@registros_bp.route('/registro')
def registro():
    return render_template('registro.html')

@registros_bp.route('/registro_profesional')
def registro_profesional():
    return render_template('registro_profesional.html')

# rutas asociadas a las páginas para procesar los formularios (usuario común y profesional)
@registros_bp.route('/procesar_registro', methods=['POST']) 
def procesar_registro():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    mail = request.form['email']
    contraseña = request.form['contrasena']
    peso = request.form['peso']
    altura = request.form['altura']
    edad = request.form['edad']
    antecedente_quirurgico = request.form.get('antecedente_quirurgico', 'off') == 'on' # El valor será True o False
    resumen_antecedente_quirurgico = request.form['resumen_antecedente_quirurgico'] if antecedente_quirurgico else ''
    antecedente_medico = request.form.get('antecedente_medico', 'off') == 'on'
    resumen_antecedente_medico = request.form['resumen_antecedente_medico'] if antecedente_medico else ''
    fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Conectar a la base de datos e insertar los datos en la tabla Usuarios
    conn = sqlite3.connect('smartfit.db')
    c = conn.cursor()

    c.execute('''
        INSERT INTO Usuarios (nombre, apellido, edad, mail, contraseña, fecha_registro, altura, peso, antecedente_quirurgico, resumen_antecedente_quirurgico, antecedente_medico, resumen_antecedente_medico)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nombre, apellido, edad, mail, contraseña, fecha_registro, altura, peso, antecedente_quirurgico, resumen_antecedente_quirurgico, antecedente_medico, resumen_antecedente_medico))

    # Confirmar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

    # Se crea una sesión, con una nueva clave (nombre) guardando el nombre del usuario
    session['nombre'] = nombre    

    return render_template('index.html')

@registros_bp.route('/procesar_registro_profesional', methods=['POST']) 
def procesar_registro_profesional():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    biografia = request.form['biografia']
    mail = request.form['email']
    contraseña = request.form['contrasena']
    especialidad = request.form['especialidad']
    descripcion_especialidad = request.form['descripcion_especialidad']
    area = request.form['area']
    certificacion = request.form['certificacion']
    fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect('smartfit.db')
    c = conn.cursor()

    c.execute('''
        INSERT OR IGNORE INTO Especialidades (nombre, descripcion, area, certificacion)
        VALUES (?, ?, ?, ?)
    ''', (especialidad, descripcion_especialidad, area, certificacion))

    # Obtener el id de la especialidad insertada o existente
    c.execute('SELECT id_especialidad FROM Especialidades WHERE nombre = ?', (especialidad,))
    id_especialidad = c.fetchone()[0]

    c.execute('''
        INSERT INTO Profesionales (id_especialidad, nombre, apellido, biografia, mail, contraseña, fecha_registro)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (id_especialidad, nombre, apellido, biografia, mail, contraseña, fecha_registro))

    conn.commit()
    conn.close()

    # Crear una sesión para el profesional registrado y añadimos variables para identificar que es un profesional
    session['nombre'] = nombre
    session['tipo_usuario'] = "profesional"   
    session['es_profesional'] = True

    return render_template('index.html')