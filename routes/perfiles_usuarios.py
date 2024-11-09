from flask import Blueprint, render_template, redirect, request, session, jsonify
import sqlite3

# Definimos el blueprint para la ruta de perfil 
perfiles_bp = Blueprint('perfiles', __name__)

@perfiles_bp.route('/perfil')
def perfil():
    if 'id_usuario' in session:
        conn = sqlite3.connect('smartfit.db')
        c = conn.cursor()
        
        # Obtener la información del usuario
        c.execute("SELECT nombre, apellido, mail, calorias_quemadas FROM Usuarios WHERE id_usuario = ?", (session['id_usuario'],))
        usuario = c.fetchone()
        
        # Obtener los entrenamientos únicos completados por el usuario, con la ruta incluida
        c.execute("""
            SELECT DISTINCT e.nombre_entrenamiento, e.ruta_html 
            FROM Entrenamientos_usuarios eu
            JOIN Entrenamientos e ON eu.id_entrenamiento = e.id_entrenamiento
            WHERE eu.id_usuario = ?
        """, (session['id_usuario'],))
        entrenamientos = c.fetchall()
        
        conn.close()

        # Convertir el resultado en un diccionario para pasarlo a la plantilla
        usuario_data = {
            'nombre': usuario[0],
            'apellido': usuario[1],
            'mail': usuario[2],
            'calorias_quemadas': usuario[3] or 0
        }

        # Pasar entrenamientos y sus rutas
        return render_template(
            'perfil.html', 
            usuario=usuario_data, 
            entrenamientos=entrenamientos  # Lista de tuplas (nombre_entrenamiento, ruta_html)
        )
    else:
        return redirect('/')
    
@perfiles_bp.route('/actualizar_calorias_y_entrenamiento', methods=['POST'])
def actualizar_calorias_y_entrenamiento():
    if 'id_usuario' in session:
        datos = request.get_json()
        nuevas_calorias = datos.get('calorias', 0)
        entrenamiento_id = datos.get('entrenamiento_id')
        
        conn = sqlite3.connect('smartfit.db')
        c = conn.cursor()
        
        c.execute("UPDATE Usuarios SET calorias_quemadas = calorias_quemadas + ? WHERE id_usuario = ?", 
                  (nuevas_calorias, session['id_usuario']))

        c.execute("INSERT OR IGNORE INTO Entrenamientos_usuarios (id_usuario, id_entrenamiento) VALUES (?, ?)", 
                  (session['id_usuario'], entrenamiento_id))
        conn.commit()
        conn.close()
        
        return jsonify({"success": True}), 200  # Responder con éxito
    else:
        return jsonify({"error": "Usuario no autenticado"}), 401
