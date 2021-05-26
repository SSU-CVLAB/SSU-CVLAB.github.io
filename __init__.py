from flask import Flask, url_for, render_template, url_for, request, redirect, session
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import sqlite3
from easydict import EasyDict as edict

app = Flask(__name__, static_folder='static')
Bootstrap(app)
app.debug = True
app.config.update(DEBUG=True)

db_path = "./static/db/data.db"
con = sqlite3.connect(db_path)
cursor = con.cursor()
db_key = 'vision407'


@app.route('/')
def index():
    with sqlite3.connect(db_path) as con:
        cursor = con.cursor()
        cursor.execute("SELECT Name, Context FROM explains ORDER BY Number asc")
        contexts = cursor.fetchall()
        context = edict()
        for info in contexts:
            context[info[0]] = []
        for info in contexts:
            context[info[0]].append(info[1])

    return render_template('main.html', context=context)


@app.route('/member')
def member():
    with sqlite3.connect(db_path) as con:
        cursor = con.cursor()
        cursor.execute("SELECT Name, Position, Contact FROM member WHERE Alumni=0 and Grade=0")
        members = cursor.fetchall()

        master = {'total': len(members),
                  'image': [member[0] + '.jpg' for member in members],
                  'name': [member[0] for member in members],
                  'position': [member[1] for member in members],
                  'contact': [member[2] for member in members]}

        cursor.execute("SELECT Name, Position, Contact FROM member WHERE Alumni=1 and Grade=1")
        members = cursor.fetchall()

        alumni_phD = {'total': len(members),
                      'image': [member[0] + '.jpg' for member in members],
                      'name': [member[0] for member in members],
                      'position': [member[1] for member in members]}

        cursor.execute("SELECT Name, Position, Contact FROM member WHERE Alumni=1 and Grade=0")
        members = cursor.fetchall()

        alumni_MS = {'total': len(members),
                      'image': [member[0] + '.jpg' for member in members],
                      'name': [member[0] for member in members],
                      'position': [member[1] for member in members]}

    return render_template('member.html',
                           master_list=master,
                           alumni_phD_list=alumni_phD,
                           alumni_ms_list=alumni_MS)


# 게시물 생성 (Create)
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        password = request.form['password']
        if password is  db_key:
            return redirect(url_for('admin'))
        context = request.form['context']
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            cur.execute(context)
            con.commit()
        return redirect(url_for('admin'))

    else:
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM member ORDER BY Id ASC")
            members = cur.fetchall()
            cur.execute("SELECT * FROM explains ORDER BY Name ASC")
            explains = cur.fetchall()

        return render_template('admin.html', members=members, explains=explains)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
