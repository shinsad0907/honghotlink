from flask import Flask, request, render_template, redirect, url_for, flash, jsonify, session
from functools import wraps
from datetime import datetime
import os

try:
    from src_python.get_data import GET_DATA
except ImportError:
    print("Không thể import GET_DATA từ src_python/get_data.py. Kiểm tra lại đường dẫn.")
    exit(1)

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
        return redirect(url_for('home'))  # Chuyển hướng về trang chủ hoặc trang khác

# Trang chủ hoặc một route mặc định khác
@app.route('/')
def home():
    return "Welcome to the Home Page!"

if __name__ == '__main__':
    app.run(debug=False)
