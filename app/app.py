from flask import Flask, render_template

app = Flask(__name__, template_folder="./templates")


@app.route('/aggregate')
def aggregate():
    images = ["aggregate1.png", "aggregate2.png"]
    return render_template("aggregate.html", images=images)


@app.route('/mapreduce')
def mapreduce():
    images = ["mapreduce1.png"]
    return render_template("mapreduce.html", images=images)


@app.route('/')
def main():
    return render_template("index.html")


def start():
    app.run(host="0.0.0.0")

if __name__ == "__main__":
    start()