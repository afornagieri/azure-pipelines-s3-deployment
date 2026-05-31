from livereload import Server
import subprocess

def build():
    subprocess.run(["python3", "build.py"])

build()

server = Server()

server.watch("src/*", build)
server.watch("static/*/*", build)
server.watch("templates/*", build)

server.serve(root="dist")
