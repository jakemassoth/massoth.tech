from app import db, ma


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)
    last_commit = db.Column(db.DateTime, unique=False, nullable=False)
    stars = db.Column(db.Integer, unique=False, nullable=False)
    forks = db.Column(db.Integer, unique=False, nullable=False)
    language = db.Column(db.String(20), unique=False, nullable=False)
    url = db.Column(db.String(120), nullable=False)

    def __init__(self, name, description, last_commit, stars,
                 forks, language, url):
        self.name = name
        self.description = description
        self.last_commit = last_commit
        self.stars = stars
        self.forks = forks
        self.language = language
        self.url = url


class ProjectSchema(ma.ModelSchema):
    class Meta:
        model = Project
