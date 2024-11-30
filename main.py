import os
import sqlite3
import json
from flask import Flask, request, render_template, session, redirect,jsonify
import user_login
import run_code
import FlowChart
import scrum_board
import pylintCheck
import uml_diagram



BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'D://code_edit//CodeWalker//Frontend//templates'),
    static_folder=os.path.join(BASE_DIR, 'D://code_edit//CodeWalker//Frontend//static')
)

user_login.SetFunctions(app)  # login
run_code.SetFunctions(app)    # run python code
FlowChart.SetFunctions(app)   # flowchart
scrum_board.SetFunctions(app) # scrum board
pylintCheck.SetFunctions(app) # pylint
uml_diagram.SetFunctions(app) # uml diagram

# Handle errors globally
@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error occurred", "details": str(e)}), 500


if __name__ == "__main__":
    app.secret_key = 'ca 0c 86 04 98@ 02b 1b7 8c 88] 1b d7"+ e6px@ c3#\\'
    app.run(host="0.0.0.0", port=80, debug=False)
