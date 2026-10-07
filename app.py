from flask import Flask, render_template

app = Flask(__name__, template_folder=".")


@app.route("/")
def home():
    import pandas as pd

    data = pd.read_csv("books_data.csv")
    books = data.to_dict(orient="records")

    return render_template("index.html", books=books)


if __name__ == "__main__":
    app.run(debug=True)