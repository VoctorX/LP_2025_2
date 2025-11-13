# --- app.py: CÓDIGO COMPLETO DE LA APLICACIÓN SIMPLE ---
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from sqlalchemy import func

# 1. Configuración
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'clave_super_secreta_facil' 
db = SQLAlchemy(app)

# 2. Modelos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    rol = db.Column(db.Integer, default=0) 
    password_hash = db.Column(db.String(128), nullable=False)
    
class Materia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    
class Asistencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    presente = db.Column(db.Boolean, default=False)
    estudiante_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    materia_id = db.Column(db.Integer, db.ForeignKey('materia.id'))
    materia = db.relationship('Materia', backref='asistencias') 

class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(100))
    estudiante_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    materia_id = db.Column(db.Integer, db.ForeignKey('materia.id'))
    materia = db.relationship('Materia', backref='notas') 

# 3. Funciones de Setup y Control de Acceso
def create_tables():
    db.create_all()
    # Cargar datos iniciales
    if Usuario.query.count() == 0:
        hashed_pass = generate_password_hash('123', method='pbkdf2:sha256') 
        db.session.add(Usuario(nombre='Harol', rol=1, password_hash=hashed_pass)) 
        db.session.add(Usuario(nombre='Ana Perez', rol=0, password_hash=hashed_pass))
        db.session.add(Materia(nombre='Programación Web'))
        db.session.commit()
        print("Datos iniciales de prueba cargados.")
        
def requires_login(role=None):
    # Decorador de login simplificado
    def decorator(f):
        def wrapper(*args, **kwargs):
            if 'user_id' not in session:
                flash("Necesitas iniciar sesión.", 'danger')
                return redirect(url_for('login'))
            if role is not None and session['rol'] != role:
                flash("Acceso denegado. Rol incorrecto.", 'danger')
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        wrapper.__name__ = f.__name__
        return wrapper
    return decorator

# 4. Rutas Generales y Login
@app.route('/')
def index():
    if 'user_id' in session:
        if session['rol'] == 1:
            return redirect(url_for('dashboard_profesor'))
        else:
            return redirect(url_for('dashboard_estudiante'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        password = request.form.get('password')
        usuario = Usuario.query.filter_by(nombre=nombre).first()
        if usuario and check_password_hash(usuario.password_hash, password):
            session['user_id'] = usuario.id
            session['rol'] = usuario.rol 
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Nombre de usuario o contraseña incorrectos.', 'danger')
    return render_template('index.html', title='Login', is_login=True)

@app.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado la sesión.', 'info')
    return redirect(url_for('login'))

# 5. Rutas del Profesor (Rol 1)
@app.route('/profesor/dashboard')
@requires_login(role=1)
def dashboard_profesor():
    materias = Materia.query.all()
    estudiantes = Usuario.query.filter_by(rol=0).all()
    return render_template('index.html', title='Profesor Dashboard', is_profesor=True, materias=materias, estudiantes=estudiantes)

@app.route('/profesor/cargar_nota', methods=['GET', 'POST'])
@requires_login(role=1)
def cargar_nota():
    materias = Materia.query.all()
    estudiantes = Usuario.query.filter_by(rol=0).all()
    if request.method == 'POST':
        try:
            estudiante_id = request.form.get('estudiante_id')
            materia_id = request.form.get('materia_id')
            valor = float(request.form.get('valor'))
            descripcion = request.form.get('descripcion')
            nueva_nota = Nota(estudiante_id=estudiante_id, materia_id=materia_id, valor=valor, descripcion=descripcion)
            db.session.add(nueva_nota)
            db.session.commit()
            flash('Nota cargada exitosamente.', 'success')
            return redirect(url_for('dashboard_profesor'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al cargar la nota: {e}', 'danger')
    return render_template('index.html', title='Cargar Nota', is_cargar_nota=True, materias=materias, estudiantes=estudiantes)

@app.route('/profesor/tomar_asistencia/', methods=['GET', 'POST'])
@requires_login(role=1)
def tomar_asistencia(materia_id):
    materia = Materia.query.get_or_404(materia_id)
    estudiantes = Usuario.query.filter_by(rol=0).all()
    fecha_actual = date.today()
    if request.method == 'POST':
        for estudiante in estudiantes:
            presente = request.form.get(f'asistencia_{estudiante.id}') == 'on'
            asistencia = Asistencia.query.filter_by(estudiante_id=estudiante.id, materia_id=materia_id, fecha=fecha_actual).first()
            if asistencia:
                asistencia.presente = presente
            else:
                asistencia = Asistencia(estudiante_id=estudiante.id, materia_id=materia_id, fecha=fecha_actual, presente=presente)
                db.session.add(asistencia)
        db.session.commit()
        flash('Asistencia registrada exitosamente.', 'success')
        return redirect(url_for('dashboard_profesor'))
    asistencias_hoy = {a.estudiante_id: a.presente for a in Asistencia.query.filter_by(materia_id=materia_id, fecha=fecha_actual).all()}
    return render_template('index.html', title='Tomar Asistencia', is_tomar_asistencia=True, materia=materia, estudiantes=estudiantes, fecha=fecha_actual, asistencias_hoy=asistencias_hoy)

@app.route('/profesor/ver_notas/')
@requires_login(role=1)
def ver_notas_estudiante(estudiante_id):
    estudiante = Usuario.query.get_or_404(estudiante_id)
    notas = Nota.query.filter_by(estudiante_id=estudiante_id).join(Materia).all()
    return render_template('index.html', title=f'Notas de {estudiante.nombre}', is_ver_notas=True, estudiante=estudiante, notas=notas)

# 6. Rutas del Estudiante (Rol 0)
@app.route('/estudiante/dashboard')
@requires_login(role=0)
def dashboard_estudiante():
    estudiante_id = session.get('user_id')
    estudiante = Usuario.query.get_or_404(estudiante_id)
    return render_template('index.html', title='Estudiante Dashboard', is_estudiante=True, estudiante=estudiante)

@app.route('/estudiante/mis_notas')
@requires_login(role=0)
def mis_notas():
    estudiante_id = session.get('user_id')
    estudiante = Usuario.query.get_or_404(estudiante_id)
    notas_por_materia = db.session.query(Materia.nombre.label('materia'), func.avg(Nota.valor).label('promedio')).join(Nota, Materia.id == Nota.materia_id).filter(Nota.estudiante_id == estudiante_id).group_by(Materia.nombre).all()
    notas_detalladas = Nota.query.filter_by(estudiante_id=estudiante_id).join(Materia).all()
    return render_template('index.html', title='Mis Notas', is_mis_notas=True, estudiante=estudiante, notas_por_materia=notas_por_materia, notas_detalladas=notas_detalladas)

@app.route('/estudiante/mi_asistencia')
@requires_login(role=0)
def mi_asistencia():
    estudiante_id = session.get('user_id')
    estudiante = Usuario.query.get_or_404(estudiante_id)
    asistencias = Asistencia.query.filter_by(estudiante_id=estudiante_id).join(Materia).all()
    return render_template('index.html', title='Mi Asistencia', is_mi_asistencia=True, estudiante=estudiante, asistencias=asistencias)

# 7. Ejecución
if __name__ == '__main__':
    with app.app_context():
        create_tables() 
    app.run(debug=True)