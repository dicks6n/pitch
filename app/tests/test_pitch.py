import unittest
from app.models import Pitch

id = db.Column(db.Integer, primary_key=True)
    pitch_title = db.Column(db.String)
    pitch_body = db.Column(db.String)
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    category = db.Column(db.String(255))
    pitch = db.relationship("Comment", backref="user_pitch", lazy="dynamic")

class TestUser(unittest):
    def setUp(self):
        self.new_pitch = Pitch(pitch='Web Designer', pitchname="Welcome Home.", posted="2019-05-27 14:15:43.590134", id=5, category="Promotion")

    def tearDown(self):
        User.query.delete()
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch, 'Web Designer')
        self.assertEquals(self.new_pitch.__name__, 'Welcome Home')
        self.assertEquals(self.new_pitch.posted, '2019-05-27 14:15:43.590134')
        self.assertEquals(self.new_pitch.id, '5')
        self.assertEquals(self.new_category, 'Promotion')
    

if __name__ == "__main__":
    unittest.main()