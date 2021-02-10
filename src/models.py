from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    task = db.relationship("Task", lazy=True)

    def __repr__(self):
        return f'User: {self.name}'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(120), unique=True, nullable=False)
    is_done = db.Column(db.Boolean(), unique=False, nullable=False)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Task: {self.label}'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.label,
            # do not serialize the password, its a security breach
        }
