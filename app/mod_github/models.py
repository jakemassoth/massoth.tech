from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from main import db


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, unique=True, nullable=True)
    last_commit = db.Column(db.DateTime, unique=False, nullable=False)
    stars = db.Column(db.Integer, unique=False, nullable=False)
    forks = db.Column(db.Integer, unique=False, nullable=False)
    language = db.Column(db.String(20), unique=False, nullable=False)
