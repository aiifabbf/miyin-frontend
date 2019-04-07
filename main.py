import bottle

app = bottle.Bottle()

@app.get("/<filename:path>")
def getStatic(filename):
    return bottle.static_file(filename, root=".")

if __name__ == "__main__":
    app.run(server="tornado", host="0.0.0.0", port=8000)