from flask import Flask, request, render_template, session, redirect
import os
from workdir import WorkDir


def SetFunctions(app):
    
    @app.route("/scrum-board")
    def scrum_board():
        '''scrum board html'''
        return app.send_static_file("scrum-board.html")
