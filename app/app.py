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
    import os
    os.system(
        "mongoimport --host mongodb_database --port 27017 -d test -c crimes --type csv --file /tmp/Chicago_Crimes_2001_to_2004.csv --headerline && rm /tmp/crimes.zip")

    os.system("python crimes_mr.py")
    os.system("python crimes_aggr.py")
    os.system("python not_arrested.py")
    os.system("python make_plots.py")
    app.run(host="0.0.0.0")


if __name__ == "__main__":
    start()
