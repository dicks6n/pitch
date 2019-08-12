import unittest
from app.models import User

class TestUser(unittest):
    def setUp(self):
        self.user_Christine = User(username='Christine', password_hash="dec", email="christine@gmail.com", id=5, bio="I am a web designer", profile_pic_path="app/static/photos")

    def tearDown(self):
        User.query.delete()
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_Christine.id, 5)
        self.assertEquals(self.new_Christine.username. 'Christine')
        self.assertEquals(self.new_Christine.title, 'Wonderful')
        self.assertEquals(self.new_Christine.bio, '"I am a web designer')
        self.assertEquals(self.new_Christine.posted, '2019-05-27 14:15:43.587649')
        self.assertEquals(self.new_Christine.email, 'christine@gmail.com')
        self.assertEquals(self.new_Christine.profile_pic_path, 'app/static/photos')



    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('dec'))

if __name__ == "__main__":
    unittest.main()