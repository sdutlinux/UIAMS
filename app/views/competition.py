# coding=utf-8
from flask import render_template, session, redirect, url_for, request
from ..models import CompetitionProject, Grade, Unit, Major, Student, User, Participants, Competition
from flask.ext.login import login_required

from .. import app, db
import os
from werkzeug import secure_filename

@app.route('/competition/individual', methods=['GET', 'POST'])
@login_required
def individual():
    competitionProjects = CompetitionProject.query.order_by('id').all()
    grades = Grade.query.order_by('id').all()
    acachemys = Unit.query.filter_by(unit_id=0).order_by('id').all()
    units = Unit.query.order_by('id').all()
    if request.method == "POST":
        student = Student(request.form['student_id'], request.form['student_name'], request.form['grade'], request.form['acachemy'], request.form['major'])
        db.session.add(student)
        achievement_name = request.form['achievement_name']
        winning_level = request.form['winning_level']
        rate = request.form['rate']
        winning_time = request.form['winning_time']
        awards_unit = request.form['awards_unit']

        competition = Competition(achievement_name, winning_level, rate, awards_unit,winning_time)
        competition.student = student
        competition.id_competitionproject = request.form['competitionproject']
        competition.id_teacher_1 = request.form['teacher1']
        competition.id_teacher_2 = request.form['teacher2']

        db.session.add(competition)
        db.session.commit()

        return render_template('/competition/individual.html',competitionProjects=competitionProjects, grades = grades)

    return render_template('/competition/individual.html',competitionProjects=competitionProjects, grades = grades)

@app.route('/competition/team')
@login_required
def team():
    return render_template('/competition/team.html')
