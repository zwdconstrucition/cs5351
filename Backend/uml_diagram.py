import os 
import subprocess
import traceback
from flask import Flask, request, jsonify

def SetFunctions(app):
    @app.route("/uml-diagram", methods=["GET"])
    def uml_diagram():
        """
        Serve the uml-diagram.html page
        """
        return app.send_static_file("uml-diagram.html")
    
    @app.route("/generateUML", methods=["POST"])
    def generate_uml():
        try:
            code = request.form.get("code")
            if not code:
                return jsonify({"error": "No code provided"}), 400

            # Save the code to a temporary file
            temp_file = "temp_code.py"
            with open(temp_file, "w") as f:
                f.write(code)

            # Run pyreverse to generate UML diagram
            subprocess.run(
                ["pyreverse", "-o", "dot", "-p", "diagram", temp_file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            # Use the correct .dot file path
            dot_file = "./classes_diagram.dot"
            if not os.path.exists(dot_file):
                print(f"Error: {dot_file} not found!")
                return jsonify({"error": f"{dot_file} not found"}), 500

            # Convert .dot to .png
            output_file = os.path.join(app.static_folder, "uml_diagrams", "class_diagram.png")
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            #如果系统环境变量配置困难，可以在代码中指定 dot 的绝对路径: subprocess.run([r"C:\Program Files\Graphviz\bin\dot", "-Tpng", dot_file, "-o", output_file], check=True)
            subprocess.run([r"E:\Graphviz\bin\dot", "-Tpng", dot_file, "-o", output_file], check=True)

            # Clean up temporary file
            os.remove(temp_file)

            return jsonify({"url": f"/static/uml_diagrams/class_diagram.png"}), 200
        except subprocess.CalledProcessError as e:
            print("Subprocess error:", e.stderr)
            return jsonify({"error": f"UML generation failed: {e.stderr}"}), 500
        except Exception as e:
            print("Unexpected error:", traceback.format_exc())
            return jsonify({"error": str(e)}), 500
