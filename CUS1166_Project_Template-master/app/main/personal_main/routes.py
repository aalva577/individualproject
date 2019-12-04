from flask import render_template,  redirect, url_for
from app.main import bp
from app import db
from app.main.forms import TaskForm
from app.models import Appointments


@bp.route('/alvarez')
def index():
    return render_template("home.html")


@bp.route('/appointments', methods=['GET','POST'])
def todolist():
    form = TaskForm()

    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.
        new_appointment = Appointment()
        new_appointment.app_title =  form.app_title.data
        new_appointment.app_date =  form.app_date.data
        new_appointment.start_time = form.start_time.data
        new_appointment.app_duration = form.app_duration.data
        new_appointment.app_notes = form.app_notes.data
        new_appointment.app_status = form.app_status.data

        db.session.add(new_appointment)
        db.session.commit()

        # Redirect to this handler - but without form submitted - gets a clear form.
        return redirect(url_for('')) # Add route for the appointment list

    todo_list = db.session.query(Appointment).all()

    return render_template("main/todolist.html",todo_list = todo_list,form= form)  # edit for appointments list route


@bp.route('/appointment/edit/<int:appointment_id>', methods=['GET','POST'])
def edit_appointment(appointment_id):
    form = TaskForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():

        current_appointment.app_title =  form.app_title.data
        current_appointment.app_date =  form.app_date.data
        current_appointment.start_time = form.start_time.data
        current_appointment.app_duration = form.app_duration.data
        current_appointment.app_notes = form.app_notes.data
        current_appointment.app_status = form.app_status.data

        db.session.add(current_appointment)
        db.session.commit()
        # After editing, redirect to the view page.
        return redirect(url_for('')) #edit for appointments list route
