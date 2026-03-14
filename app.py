from flask import Flask, render_template, request, redirect, url_for, flash
import csv
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "pixelmx_secret_key"

SUBMISSIONS_FOLDER = "submissions"
os.makedirs(SUBMISSIONS_FOLDER, exist_ok=True)

PARTNERSHIP_CSV = os.path.join(SUBMISSIONS_FOLDER, "partnership_requests.csv")
JOB_CSV = os.path.join(SUBMISSIONS_FOLDER, "job_applications.csv")
CONTACT_CSV = os.path.join(SUBMISSIONS_FOLDER, "contact_messages.csv")


def initialize_csv(file_path, headers):
    if not os.path.exists(file_path):
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(headers)


initialize_csv(PARTNERSHIP_CSV, ["timestamp", "name", "email", "phone", "restaurant_name", "message"])
initialize_csv(JOB_CSV, ["timestamp", "full_name", "email", "phone", "position", "experience", "message"])
initialize_csv(CONTACT_CSV, ["timestamp", "name", "email", "subject", "message"])


@app.route("/")
def home():
    return render_template("home.html", page_title="Home")


@app.route("/about")
def about():
    return render_template("about.html", page_title="About Us")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", page_title="Portfolio")


@app.route("/partnership", methods=["GET", "POST"])
def partnership():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        restaurant_name = request.form.get("restaurant_name")
        message = request.form.get("message")

        with open(PARTNERSHIP_CSV, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                name, email, phone, restaurant_name, message
            ])

        flash("Your partnership request has been submitted successfully!", "success")
        return redirect(url_for("partnership"))

    return render_template("partnership.html", page_title="Partnership")


@app.route("/jobs", methods=["GET", "POST"])
def jobs():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        position = request.form.get("position")
        experience = request.form.get("experience")
        message = request.form.get("message")

        with open(JOB_CSV, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                full_name, email, phone, position, experience, message
            ])

        flash("Your job application has been submitted successfully!", "success")
        return redirect(url_for("jobs"))

    return render_template("jobs.html", page_title="Jobs")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        with open(CONTACT_CSV, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                name, email, subject, message
            ])

        flash("Your message has been sent successfully!", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html", page_title="Contact Us")


if __name__ == "__main__":
    app.run(debug=True)