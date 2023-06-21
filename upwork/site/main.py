import sqlite3
import os
import chat_gpt_helpers
from flask import Flask, render_template, jsonify, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # read local .env file

# def get_db_connection():
#     conn = sqlite3.connect('database.db')
#     conn.row_factory = sqlite3.Row
#     return conn

def get_skill(skill_id):
    conn = get_db_connection()
    skill = conn.execute('SELECT * FROM skills WHERE id = ?',
                        (skill_id,)).fetchone()
    conn.close()
    if skill is None:
        abort(404)
    return skill


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['APP_SECRET_KEY']

@app.route('/', methods=('GET', 'POST'))
def home():
    print('enters here')
    print('request', request)
    if request.method == 'POST':

        prompt = request.form['prompt']
        res = {}
        
        res['answer'] = chat_gpt_helpers.generate_proposal(prompt)
        print('Result', res['answer'])
        return jsonify(res),200

    # conn = get_db_connection()
    # skills = conn.execute('SELECT * FROM skills').fetchall()
    # conn.close()
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/<int:skill_id>')
def skill(skill_id):
    skill = get_skill(skill_id)
    return render_template('skill.html', skill=skill)

@app.route('/create-job-proposal', methods=('GET', 'POST'))
def create_job_proposal():
    if request.method == 'POST':
        job_description = request.form['job_description']
        # content = request.form['content']

        if not job_description:
            flash('Job Description is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create-job-proposal.html')

if __name__ == '__main__':
    app.run(debug=True)