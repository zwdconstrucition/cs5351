from flask import Flask, request, render_template, session, redirect
import os
from workdir import WorkDir
import subprocess
import sys

def install_pyflowchart():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyflowchart"])
        print("pyflowchart module installed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error installing pyflowchart:", e)
        return False
    return True

def SetFunctions(app):
    
    @app.route("/flowchart",methods=("GET",))
    def flowchart():
        '''输出特定代码的flowchart的markdown格式'''
        user_name = session["userName"]
        file_name = request.args.get("fileName")
        # Check if pyflowchart is installed, and install it if necessary
        try:
            import pyflowchart
        except ImportError:
            print("pyflowchart module not found. Installing...")
            if not install_pyflowchart():
                return "Error: pyflowchart module could not be installed.", 500
        ret_code = None
        with WorkDir(user_name):
            with os.popen(f"python -m pyflowchart {file_name}") as f: # 获取该命令的输出
                ret_code = f.read()
        return render_template("flowchart.html",code=ret_code)
