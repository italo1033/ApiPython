from flask import Flask
app=Flask("__nane__")
@app.route("/")
def olaMundo():
    return "Ola mundo"
app.run(host="0.0.0.0", port=2000, debug=False)