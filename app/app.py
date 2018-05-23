from flask import Flask, render_template

app = Flask(__name__, template_folder="./templates")


@app.route('/aggregate')
def aggregate():
    images = ["test.jpg"]
    return render_template("aggregate.html", images=images)


@app.route('/mapreduce')
def mapreduce():
    images = []
    return render_template("mapreduce.html", images=images)


@app.route('/')
def main():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
