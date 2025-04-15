from flask import Flask, render_template, request, redirect, url_for
from db import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    incidencias = conn.execute('SELECT * FROM incidencias').fetchall()
    conn.close()
    return render_template('index.html', incidencias=incidencias)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        fields = ['date', 'id_status', 'short_description', 'description',
                  'id_usuario', 'id_urgency', 'id_impact', 'id_prioridad']
        values = [request.form[field] for field in fields]

        conn = get_db_connection()
        conn.execute('''
            INSERT INTO incidencias (date, id_status, short_description, description,
            id_usuario, id_urgency, id_impact, id_prioridad)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', values)
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('form.html', accion='Crear')

@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit(id):
    conn = get_db_connection()
    incidencia = conn.execute('SELECT * FROM incidencias WHERE id_incidencia = ?', (id,)).fetchone()

    if request.method == 'POST':
        fields = ['date', 'id_status', 'short_description', 'description',
                  'id_usuario', 'id_urgency', 'id_impact', 'id_prioridad']
        values = [request.form[field] for field in fields] + [id]

        conn.execute('''
            UPDATE incidencias
            SET date = ?, id_status = ?, short_description = ?, description = ?,
                id_usuario = ?, id_urgency = ?, id_impact = ?, id_prioridad = ?
            WHERE id_incidencia = ?
        ''', values)
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('form.html', accion='Editar', incidencia=incidencia)

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM incidencias WHERE id_incidencia = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)