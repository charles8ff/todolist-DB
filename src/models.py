from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, ForeignKey, Integer, String

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    task = db.relationship("Task", lazy=True)

    def __repr__(self):
        return f'User {self.name}'

    def serialize(self):
        return {
            "name": self.name,
        }

    def add(self):
        db.session.add(self)
        db.session.commit()

    # def get_user_list(self):
    #     my_list = User.query.all()
    #     print(my_list)
    #     if my_list:
    #         return my_list
    #     return "No users in database"

    @classmethod
    def get_by_name(cls, user_name):
        name = cls.query.filter_by(name= user_name).first()
        return name if name else "User not found :_("
      
    @classmethod
    def create_new_user(self):
        db.session.add(self)
        db.session.commit()
        return self.serialize()

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(250), unique=False, nullable=False)
    is_done = db.Column(db.Boolean(), unique=False, nullable=False)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Task: {self.label} status: {self.is_done}'

    def serialize(self):
        return {
            "label": self.label,
            "is_done": self.is_done,
        }
