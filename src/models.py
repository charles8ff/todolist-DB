from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, ForeignKey, Integer, String

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    task = db.relationship("Task", cascade="all, delete", lazy=True)

    def __repr__(self):
        return f'User {self.name}'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_name(cls, user_name):
        name = cls.query.filter_by(name= user_name).first()
        return name if name else "User not found :_("
      
    @classmethod
    def create_new_user(self):
        db.session.add(self)
        db.session.commit()
        return self.serialize()
    
    @classmethod
    def delete_user(cls, username):
        target = cls.query.filter_by(name = username).first()
        db.session.delete(target)
        db.session.commit()

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(250), unique=False, nullable=False)
    is_done = db.Column(db.Boolean(), unique=False, nullable=False)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Task: {self.label} status: {self.is_done} ID:{self.id}'

    def serialize(self):
        return {
            "label": self.label,
            "is_done": self.is_done,
        }
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self, label, is_done):
        print(self)
        self.label = label
        self.is_done = is_done
        db.session.commit()

    @classmethod
    def get_by_user(cls, userid):
        tasks= cls.query.filter_by(user_id= userid).all()
        return tasks

    @classmethod
    def get_single(cls, task_id):
        task= cls.query.filter_by(id= task_id).first()
        return task

    @classmethod
    def delete(cls, id):
        target = cls.query.filter_by(id = id).first()
        db.session.delete(target)
        db.session.commit()
