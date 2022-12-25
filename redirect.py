import os
import random
from flask import Flask, redirect, render_template, abort

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html', title = '404'), 404

@app.route('/')
def index():
    abort(404)

@app.route('/<string:list>')
def find_redirect(list):
    if f"{list}.list" not in os.listdir("url-lists"):
        abort(404)
    with open(f"url-lists/{list}.list", 'r') as f:
        urls = [url.strip() for url in f.readlines()]
        return redirect(random.choice(urls), code=307)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)
