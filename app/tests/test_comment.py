import unittest
from app.models import User, Comment
from flask_login import current_user
from app import db

class TestComments(unittest.TestCase):
    def setUp(self):        
        self.new_comment = Comment(id=10, comment_title='Wonderful', comment="Great work", posted="2019-05-27 14:15:43.12345", user_id=5)

    def tearDown(self):
        Comment.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id, 10)
        self.assertEquals(self.new_comment.title, 'Wonderful')
        self.assertEquals(self.new_comment.comment, 'Great work')
        self.assertEquals(self.new_comment.posted, '2019-05-27 14:15:43.12345')
        