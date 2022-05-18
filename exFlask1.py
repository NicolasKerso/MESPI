# -*- coding: utf-8 -*-
"""
Created on Mon May 16 17:11:35 2022

@author: leleu
"""

from flask import *

# Create the application instance
app = Flask(__name__, template_folder="templates/")

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
        

    :return:        the rendered template 'home.html'
    """
    return render_template('exJson1.json')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='172.16.115.149' , port=5000)