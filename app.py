from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary database (Python list)
expenses = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Temporary Login
        if username == "admin" and password == "1234":
            return redirect(url_for("expense_page"))
        else:
            return render_template(
                "login.html",
                message="Invalid Username or Password"
            )

    return render_template("login.html")


@app.route("/expenses", methods=["GET", "POST"])
def expense_page():

    if request.method == "POST":

        expense = {
            "title": request.form["title"],
            "amount": request.form["amount"],
            "category": request.form["category"]
        }

        expenses.append(expense)

        return redirect(url_for("expense_page"))

    total = sum(float(item["amount"]) for item in expenses) if expenses else 0

    return render_template(
        "expenses.html",
        expenses=expenses,
        total=total
    )


@app.route("/delete/<int:index>")
def delete(index):

    if index < len(expenses):
        expenses.pop(index)

    return redirect(url_for("expense_page"))


if __name__ == "__main__":
    app.run(debug=True)
    