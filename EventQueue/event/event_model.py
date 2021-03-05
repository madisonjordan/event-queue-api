from EventQueue import db

class Event(db.Model):
    __tablename__ = "event"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    date = db.Column(db.DateTime)
    location= db.Column(db.String(120))
    description = db.Column(db.String(1000))

    def __repr__(self):
      return "<Event %r>" % self.name
    