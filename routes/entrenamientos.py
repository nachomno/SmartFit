from flask import Blueprint, render_template, session
import sqlite3

# Definimos el blueprint para las rutas de entrenamiento
entrenamientos_bp = Blueprint('entrenamientos', __name__)

@entrenamientos_bp.route('/P_A')
def principiante_abdomen():
    conn = sqlite3.connect('smartfit.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_ejercicio, descripcion_ejercicio, descripcion_dos_ejercicio, repeticiones, calorias, ruta_video FROM Ejercicios WHERE ruta_video LIKE '%1.ABDOMINALES%' AND nombre_ejercicio LIKE '%(Principiante)'")
    ejercicios = cursor.fetchall()
    conn.close()
    usuario_logueado = session.get('nombre', None)
    return render_template('entrenamientos/P_A.html', ejercicios=ejercicios, usuario_logueado=usuario_logueado)

@entrenamientos_bp.route('/P_B')
def principiante_brazos():
    conn = sqlite3.connect('smartfit.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_ejercicio, descripcion_ejercicio, descripcion_dos_ejercicio, repeticiones, calorias, ruta_video FROM Ejercicios WHERE ruta_video LIKE '%2.BRAZO%' AND nombre_ejercicio LIKE '%(Principiante)'")
    ejercicios = cursor.fetchall()
    conn.close()
    
    # Verifica si el usuario está logueado
    usuario_logueado = session.get('nombre', None)
    return render_template('entrenamientos/P_B.html', ejercicios=ejercicios, usuario_logueado=usuario_logueado)

@entrenamientos_bp.route('/P_E')
def principiante_espalda():
    conn = sqlite3.connect('smartfit.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_ejercicio, descripcion_ejercicio, descripcion_dos_ejercicio, repeticiones, calorias, ruta_video FROM Ejercicios WHERE ruta_video LIKE '%4.ESPALDA%' AND nombre_ejercicio LIKE '%(Principiante)'")
    ejercicios = cursor.fetchall()
    conn.close()
    
    # Verifica si el usuario está logueado
    usuario_logueado = session.get('nombre', None)
    return render_template('entrenamientos/P_E.html', ejercicios=ejercicios, usuario_logueado=usuario_logueado)

@entrenamientos_bp.route('/P_P')
def principiante_piernas():
    conn = sqlite3.connect('smartfit.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_ejercicio, descripcion_ejercicio, descripcion_dos_ejercicio, repeticiones, calorias, ruta_video FROM Ejercicios WHERE ruta_video LIKE '%3.PIERNA%' AND nombre_ejercicio LIKE '%(Principiante)'")
    ejercicios = cursor.fetchall()
    conn.close()
    
    # Verifica si el usuario está logueado
    usuario_logueado = session.get('nombre', None)
    return render_template('entrenamientos/P_P.html', ejercicios=ejercicios, usuario_logueado=usuario_logueado)

@entrenamientos_bp.route('/I_A')
def intermedio_abdomen():
    conn = sqlite3.connect('smartfit.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_ejercicio, descripcion_ejercicio, descripcion_dos_ejercicio, repeticiones, calorias, ruta_video FROM Ejercicios WHERE ruta_video LIKE '%1.ABDOMINALES%' AND nombre_ejercicio LIKE '%(Intermedio)'")
    ejercicios = cursor.fetchall()
    conn.close()
    usuario_logueado = session.get('nombre', None)
    return render_template('entrenamientos/I_A.html', ejercicios=ejercicios, usuario_logueado=usuario_logueado)

@entrenamientos_bp.route('/I_B')
def intermedio_brazos():
    conn = sqlite3.connect('smartfit.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_ejercicio, descripcion_ejercicio, descripcion_dos_ejercicio, repeticiones, calorias, ruta_video FROM Ejercicios WHERE ruta_video LIKE '%2.BRAZO%' AND nombre_ejercicio LIKE '%(Intermedio)'")
    ejercicios = cursor.fetchall()
    conn.close()
    
    # Verifica si el usuario está logueado
    usuario_logueado = session.get('nombre', None)
    return render_template('entrenamientos/I_B.html', ejercicios=ejercicios, usuario_logueado=usuario_logueado)

@entrenamientos_bp.route('/I_E')
def intermedio_espalda():
    conn = sqlite3.connect('smartfit.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_ejercicio, descripcion_ejercicio, descripcion_dos_ejercicio, repeticiones, calorias, ruta_video FROM Ejercicios WHERE ruta_video LIKE '%4.ESPALDA%' AND nombre_ejercicio LIKE '%(Intermedio)'")
    ejercicios = cursor.fetchall()
    conn.close()
    
    # Verifica si el usuario está logueado
    usuario_logueado = session.get('nombre', None)
    return render_template('entrenamientos/I_E.html', ejercicios=ejercicios, usuario_logueado=usuario_logueado)
@entrenamientos_bp.route('/I_P')
def intermedio_piernas():
    conn = sqlite3.connect('smartfit.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_ejercicio, descripcion_ejercicio, descripcion_dos_ejercicio, repeticiones, calorias, ruta_video FROM Ejercicios WHERE ruta_video LIKE '%3.PIERNA%' AND nombre_ejercicio LIKE '%(Intermedio)'")
    ejercicios = cursor.fetchall()
    conn.close()
    
    # Verifica si el usuario está logueado
    usuario_logueado = session.get('nombre', None)
    return render_template('entrenamientos/I_P.html', ejercicios=ejercicios, usuario_logueado=usuario_logueado)

@entrenamientos_bp.route('/A_A')
def avanzado_abdomen():
    conn = sqlite3.connect('smartfit.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_ejercicio, descripcion_ejercicio, descripcion_dos_ejercicio, repeticiones, calorias, ruta_video FROM Ejercicios WHERE ruta_video LIKE '%1.ABDOMINALES%' AND nombre_ejercicio LIKE '%(Avanzado)'")
    ejercicios = cursor.fetchall()
    conn.close()
    
    # Verifica si el usuario está logueado
    usuario_logueado = session.get('nombre', None)
    return render_template('entrenamientos/A_A.html', ejercicios=ejercicios, usuario_logueado=usuario_logueado)

@entrenamientos_bp.route('/A_B')
def avanzado_brazos():
    conn = sqlite3.connect('smartfit.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_ejercicio, descripcion_ejercicio, descripcion_dos_ejercicio, repeticiones, calorias, ruta_video FROM Ejercicios WHERE ruta_video LIKE '%2.BRAZO%' AND nombre_ejercicio LIKE '%(Avanzado)'")
    ejercicios = cursor.fetchall()
    conn.close()
    
    # Verifica si el usuario está logueado
    usuario_logueado = session.get('nombre', None)
    return render_template('entrenamientos/A_B.html', ejercicios=ejercicios, usuario_logueado=usuario_logueado)

@entrenamientos_bp.route('/A_E')
def avanzado_espalda():
    conn = sqlite3.connect('smartfit.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_ejercicio, descripcion_ejercicio, descripcion_dos_ejercicio, repeticiones, calorias, ruta_video FROM Ejercicios WHERE ruta_video LIKE '%4.ESPALDA%' AND nombre_ejercicio LIKE '%(Avanzado)'")
    ejercicios = cursor.fetchall()
    conn.close()
    
    # Verifica si el usuario está logueado
    usuario_logueado = session.get('nombre', None)
    return render_template('entrenamientos/A_E.html', ejercicios=ejercicios, usuario_logueado=usuario_logueado)

@entrenamientos_bp.route('/A_P')
def avanzado_piernas():
    conn = sqlite3.connect('smartfit.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_ejercicio, descripcion_ejercicio, descripcion_dos_ejercicio, repeticiones, calorias, ruta_video FROM Ejercicios WHERE ruta_video LIKE '%3.PIERNA%' AND nombre_ejercicio LIKE '%(Avanzado)'")
    ejercicios = cursor.fetchall()
    conn.close()
    
    # Verifica si el usuario está logueado
    usuario_logueado = session.get('nombre', None)
    return render_template('entrenamientos/A_P.html', ejercicios=ejercicios, usuario_logueado=usuario_logueado)