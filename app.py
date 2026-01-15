from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = "arya_secret"

services = [
    {"id": 1, "name": "Rakesh Electrician", "category": "Electrician", "location": "Borivali", "availability": "Available", "rating": 4.5,"process": [
            {"step": "Inspection", "desc": "Electrician will inspect the problem."},
            {"step": "Required repair/installation", "desc": "The required work will be done after inspection using proper tools."},
            {"step": "Clean Up", "desc": "After completing work, area will be cleaned."}
        ]},
    {"id": 2, "name": "Moco Plumber", "category": "Plumber", "location": "Borivali", "availability": "Busy", "rating": 4.2,"process": [
            {"step": "Inspection", "desc": "The plumber will inspect the issue carefully."},
            {"step": "Required Required Repair / Installation", "desc": "After inspection, the work will be done with proper tools."},
            {"step": "Clean Up", "desc": "Area will be cleaned after completing the work."}
        ]},

    {"id": 3, "name": "A1 Home Cleaning", "category": "Cleaning", "location": "Borivali", "availability": "Available", "rating": 4.7,"process":[
            {"step": "Inspection", "desc": "Cleaning staff inspects the house and Understand the requirments."},
            {"step": "Required Cleaning Service", "desc": "Once inspection is done, the work will be done carefully."},
            {"step": "Clean Up", "desc": "Area will be cleaned after completing service."}
        ]},     
    {"id": 4, "name": "Maths Tutor", "category": "Tutor", "location": "Borivali", "availability": "Busy", "rating": 4.2,"process": [
            {"step": "Student Evaluation", "desc": "Tutor checks the student's learning level."},
            {"step": "Teaching & Practice", "desc": "Tutor will explain the concepts and try to improve student's learning."},
            {"step": "Doubt Solving", "desc": "Tutor will clear all the doubts of student."}
        ]},
    {"id": 5, "name": "MBA Mechanic", "category": "Mechanic", "location": "Borivali", "availability": "Available", "rating": 4.0,"process": [
            {"step": "Vehicle Inspection", "desc": "Vehicle will be inspected by mechanic."},
            {"step": "Repair & Maintenance", "desc": "Servicing will be done after inspection with proper tools."},
            {"step": "Clean Up", "desc": "Area will be cleaned after completing work."}
        ]},
    {"id": 6, "name": "Bolt Electrician", "category": "Electrician", "location": "Kandivali", "availability": "Busy", "rating": 4.7,"process": [
            {"step": "Inspection", "desc": "Electrician will inspect the problem."},
            {"step": "Required repair/installation", "desc": "The required work will be done after inspection using proper tools."},
            {"step": "Clean Up", "desc": "After completing work, area will be cleaned."}
        ]},
    {"id": 7, "name": "Flexi Plumber", "category": "Plumber", "location": "Kandivali", "availability": "Busy", "rating": 4.0,"process": [
            {"step": "Inspection", "desc": "The plumber will inspect the issue carefully."},
            {"step": "Required Required Repair / Installation", "desc": "After inspection, the work will be done with proper tools."},
            {"step": "Clean Up", "desc": "Area will be cleaned after completing the work."}
        ]},

    {"id": 8, "name": "Vantra Cleaning", "category": "Cleaning", "location": "Kandivali", "availability": "Available", "rating": 4.5,"process":[
            {"step": "Inspection", "desc": "Cleaning staff inspects the house and Understand the requirments."},
            {"step": "Required Cleaning Service", "desc": "Once inspection is done, the work will be done carefully."},
            {"step": "Clean Up", "desc": "Area will be cleaned after completing service."}
        ]},     
    {"id": 9, "name": "Arya Tutor", "category": "Tutor", "location": "Kandivali", "availability": "Offline", "rating": 4.6,"process": [
            {"step": "Student Evaluation", "desc": "Tutor checks the student's learning level."},
            {"step": "Teaching & Practice", "desc": "Tutor will explain the concepts and try to improve student's learning."},
            {"step": "Doubt Solving", "desc": "Tutor will clear all the doubts of student."}
        ]},
    {"id": 10, "name": "Extra Mile", "category": "Mechanic", "location": "Kandivali", "availability": "Available", "rating": 4.3,"process": [
            {"step": "Vehicle Inspection", "desc": "Vehicle will be inspected by mechanic."},
            {"step": "Repair & Maintenance", "desc": "Servicing will be done after inspection with proper tools."},
            {"step": "Clean Up", "desc": "Area will be cleaned after completing work."}
        ]},
    {"id": 11, "name": "Pika Electrician", "category": "Electrician", "location": "Borivali", "availability": "Busy", "rating": 4.3,"process": [
            {"step": "Inspection", "desc": "Electrician will inspect the problem."},
            {"step": "Required repair/installation", "desc": "The required work will be done after inspection using proper tools."},
            {"step": "Clean Up", "desc": "After completing work, area will be cleaned."}
        ]},
    {"id": 12, "name": "Alok Plumber", "category": "Plumber", "location": "Borivali", "availability": "Available", "rating": 4.7,"process": [
            {"step": "Inspection", "desc": "The plumber will inspect the issue carefully."},
            {"step": "Required Required Repair / Installation", "desc": "After inspection, the work will be done with proper tools."},
            {"step": "Clean Up", "desc": "Area will be cleaned after completing the work."}
        ]},

    {"id": 13, "name": "Disah Home Cleaning", "category": "Cleaning", "location": "Borivali", "availability": "Offline", "rating": 4.7,"process":[
            {"step": "Inspection", "desc": "Cleaning staff inspects the house and Understand the requirments."},
            {"step": "Required Cleaning Service", "desc": "Once inspection is done, the work will be done carefully."},
            {"step": "Clean Up", "desc": "Area will be cleaned after completing service."}
        ]},     
    {"id": 14, "name": "Physics Tutor", "category": "Tutor", "location": "Borivali", "availability": "Available", "rating": 4.5,"process": [
            {"step": "Student Evaluation", "desc": "Tutor checks the student's learning level."},
            {"step": "Teaching & Practice", "desc": "Tutor will explain the concepts and try to improve student's learning."},
            {"step": "Doubt Solving", "desc": "Tutor will clear all the doubts of student."}
        ]},
    {"id": 15, "name": "Tim Mechanic", "category": "Mechanic", "location": "Borivali", "availability": "Available", "rating": 4.6,"process": [
            {"step": "Vehicle Inspection", "desc": "Vehicle will be inspected by mechanic."},
            {"step": "Repair & Maintenance", "desc": "Servicing will be done after inspection with proper tools."},
            {"step": "Clean Up", "desc": "Area will be cleaned after completing work."}
        ]},
    {"id": 16, "name": "Vinod Electrician", "category": "Electrician", "location": "Kandivali", "availability": "Offline", "rating": 4.4,"process": [
            {"step": "Inspection", "desc": "Electrician will inspect the problem."},
            {"step": "Required repair/installation", "desc": "The required work will be done after inspection using proper tools."},
            {"step": "Clean Up", "desc": "After completing work, area will be cleaned."}
        ]},
    {"id": 17, "name": "Neeraj Plumber", "category": "Plumber", "location": "Kandivali", "availability": "Offline", "rating": 4.1,"process": [
            {"step": "Inspection", "desc": "The plumber will inspect the issue carefully."},
            {"step": "Required Required Repair / Installation", "desc": "After inspection, the work will be done with proper tools."},
            {"step": "Clean Up", "desc": "Area will be cleaned after completing the work."}
        ]},

    {"id": 18, "name": "Top Home Cleaning", "category": "Cleaning", "location": "Kandivali", "availability": "Available", "rating": 4.8,"process":[
            {"step": "Inspection", "desc": "Cleaning staff inspects the house and Understand the requirments."},
            {"step": "Required Cleaning Service", "desc": "Once inspection is done, the work will be done carefully."},
            {"step": "Clean Up", "desc": "Area will be cleaned after completing service."}
        ]},     
    {"id": 19, "name": "Vision Tutor", "category": "Tutor", "location": "Kandivali", "availability": "Available", "rating": 4.7,"process": [
            {"step": "Student Evaluation", "desc": "Tutor checks the student's learning level."},
            {"step": "Teaching & Practice", "desc": "Tutor will explain the concepts and try to improve student's learning."},
            {"step": "Doubt Solving", "desc": "Tutor will clear all the doubts of student."}
        ]},
    {"id": 20, "name": "FIx Mechanic", "category": "Mechanic", "location": "Kandivali", "availability": "Offline", "rating": 4.5,"process": [
            {"step": "Vehicle Inspection", "desc": "Vehicle will be inspected by mechanic."},
            {"step": "Repair & Maintenance", "desc": "Servicing will be done after inspection with proper tools."},
            {"step": "Clean Up", "desc": "Area will be cleaned after completing work."}
        ]}

]

@app.route("/")
def home():
    return render_template("home.html")  

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/submit", methods=["POST"])
def submit():
    email = request.form["email"]
    password = request.form["password"]

    if email == "tanish@gmail.com" and password == "123":
        session["user"] = email
        return redirect("/home")
    return redirect("/login")


@app.route("/home")
def index():
    if "user" not in session:
        return redirect("/login")
    return render_template("home.html")


@app.route("/services")
def get_services():
    return jsonify(services)


@app.route("/service/<int:id>")
def service_detail(id):
    service = next((s for s in services if s["id"] == id), None)
    return render_template("service_detail.html", service=service)

if __name__ == "__main__":
    app.run(debug=True)
