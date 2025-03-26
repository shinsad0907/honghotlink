from flask import Flask, request, render_template, redirect, url_for, flash, jsonify, session
from functools import wraps
import requests
import os
import json
from datetime import datetime
from src_python.get_data import GET_DATA
app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Sử dụng thư mục tạm (thường áp dụng cho môi trường serverless như AWS Lambda)
UPLOAD_FOLDER = '/tmp/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

app.run(debug=True)
