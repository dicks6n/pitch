from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you',validators= [Required()])
    submit = SubmitField("Submit")
    
class PitchForm(FlaskForm):
    
    pitch = TextAreaField('Pitch')
    category = SelectField('Pick a category',
    choices=[('INTERVIEW', 'INTERVIEW'),
    ('PRODUCT', 'PRODUCT'),
    ('PROMOTION', 'PROMOTION')])
   
    
    
    
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    
    title = StringField('Pitch')
    comment = TextAreaField('Please enter a comment')
    submit = SubmitField('Submit')
    

    
