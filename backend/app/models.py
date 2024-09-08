from . import db  # This should work now without causing a circular import

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    author = db.Column(db.String(50))
    channel = db.Column(db.String(50))
    youtube_url = db.Column(db.String(255))
    is_valid = db.Column(db.Boolean, default=False)
    name_of_song = db.Column(db.String(200), nullable=True)
    is_downloaded = db.Column(db.Boolean, default=False)
