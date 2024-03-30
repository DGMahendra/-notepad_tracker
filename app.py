import os
from flask import Flask, request, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_note():
    note_content = request.form['note_content']
    file_name = request.form['file_name']
    
    # Write note content to a file
    with open(file_name, 'w') as file:
        file.write(note_content)
    
    # Commit changes using Git
    commit_message = f"Added/Updated note: {file_name}"
    subprocess.run(['git', 'add', file_name])
    subprocess.run(['git', 'commit', '-m', commit_message])
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
