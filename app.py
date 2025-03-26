from flask import Flask, request, render_template, redirect, url_for, flash, jsonify, session
from functools import wraps
from datetime import datetime
from src_python.get_data import GET_DATA
app = Flask(__name__)
app.secret_key = 'supersecretkey'

def get_data_link():
    return GET_DATA().get_data_link()

@app.route('/<id>')
def data_link(id):
    data = get_data_link()
    link_data = next((item for item in data if item['id'] == id), None)
    if link_data:
        return render_template('link.html', link_data=link_data)
    else:
        flash('Không tìm thấy link!', 'danger')

# ...existing code...

debug_mode = os.getenv('FLASK_ENV') == 'development'
app.run(debug=debug_mode)
