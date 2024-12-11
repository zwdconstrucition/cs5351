from flask import Flask, request, render_template, session, redirect
import os
from workdir import WorkDir


def SetFunctions(app):
    
    @app.route("/scrum-board", methods=("GET",))
    def scrum_board():
        '''scrum board html'''
        return render_template("scrum-board.html")
