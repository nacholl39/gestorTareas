from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea

app = Flask(__name__)


@app.route("/")
def home():
    lista_tareas = db.session.query(Tarea).all()
    for i in lista_tareas:
        print(i)
    return render_template("index.html", l_tareas = lista_tareas)

@app.route("/crear_tarea", methods=["POST"])
def crear():
    tarea = Tarea(contenido=request.form["contenido_tarea"], hecha=False)
    db.session.add(tarea)
    db.session.commit()
    db.session.close()
    return redirect(url_for("home"))

@app.route("/eliminar-tarea/<id>")
def eliminar(id):
    tarea_eliminada = db.session.query(Tarea).filter_by(id_tarea=id).delete()
    db.session.commit()
    db.session.close()
    return redirect(url_for("home"))

@app.route("/tarea-hecha/<id>")
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id_tarea=id).first()
    tarea.hecha = not(tarea.hecha)
    db.session.commit()
    db.session.close()
    return redirect(url_for("home"))


if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)
