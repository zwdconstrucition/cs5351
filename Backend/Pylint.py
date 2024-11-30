import os
import subprocess
import json
from flask import request
from workdir import WorkDir


def SetFunctions(app):

    @app.route("/pylintCheck", methods=("POST",))
    def pylintCheck():
        '''运行pylint对用户提交的代码进行审查，并返回结果'''
        user_name = request.form["userName"]  # 获取用户信息
        file_name = request.form["fileName"]  # 获取文件名

        with WorkDir(user_name):
            # 调用pylint进行代码审查
            command = f"pylint {file_name}"
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
            proc.wait()

            # 获取pylint输出结果
            stream_stdout = proc.stdout.read().decode('utf-8')
            stream_stderr = proc.stderr.read().decode('utf-8')

            # 如果stderr有输出，表示运行出现错误
            if stream_stderr:
                return f"Error running pylint: {stream_stderr}"

            
            pylint_results = parse_pylint_output(stream_stdout)

            return json.dumps(pylint_results, indent=4)

    def parse_pylint_output(output):
        '''解析pylint输出结果并整理为易于前端处理的格式'''
        lines = output.splitlines()
        results = []

        for line in lines:
            parts = line.split(":")
            if len(parts) >= 4:
                file_path = parts[0]
                line_num = parts[1]
                column_num = parts[2]
                msg_type = parts[3].strip().split(" ")[0] 
                message = " ".join(parts[3].strip().split(" ")[1:])  

                results.append({
                    "file": file_path,
                    "line": line_num,
                    "column": column_num,
                    "msg_type": msg_type,
                    "message": message
                })
        
        return results
