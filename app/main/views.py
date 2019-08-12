from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Pitch, Comments
from .. import db, photos
from .forms import UpdateProfile, PitchForm, CommentForm
import markdown2 


#Views
@main.route('/',methods=['GET', 'POST'])
def index():
    
    form = PitchForm()
    if form.validate_on_submit():
        # post_by=form.posted_by.data
        pitch=form.pitch.data
        category=form.category.data

        new_pitch=Pitch(pitchname=pitch,category=category)
        new_pitch.save_pitch()

    
    pitches= Pitch.query.all()
    return render_template('index.html',pitches=pitches,pitch_form=form)


@main.route('/new/pitch', methods=['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        category = form.category.data
        pitchname = form.pitch.data
        
        new_pitch = Pitch(pitchname=pitchname, category=category)
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    return render_template('newpitch.html', form=form)
    

    


@main.route('/new/comment', methods=["GET", 'POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    pitch = Pitch.query.filter_by(id=id).first()
    if pitch is None:
        abort(404)
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data

    new_comment = Comments(comment_title= title,comment=comment, user_comment= user_comment)
      
    new_comment.save_comment()
    return redirect(url_for('.new_comment', id= pitch_id ))
    return render_template('comment.html',form=form, pitch=pitch)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    index = Pitch.query.all()
    if user is None:
        abort(404)
    posted_pitches= Pitch.query.filter_by(user_id=current_user.id).all()
    return render_template('profile/profile.html', user=user,pitches=posted_pitches)

@main.route("/user/<uname>/update",methods = ['GET','POST'])
@login_required 
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio =form.bio.data
        user.pitch_test=form.pitch.data

        db.session.add(user)
        db.session.commit()
        
    return redirect(url_for(".profile", uname=user.username))
    return render_template("profile/update.html", form=form)

@main.route("/user/<uname>/update/pic",methods=['GET','POST'])
@login_required
def update_pic(uname):
    user=User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename= photos.save(request.files['photo'])
        path =f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



@main.route('/pitches/<int:id>', methods=["GET", 'POST'])
def pitch(id):
    pitch=Pitch.query.filter_by(id=id).first()
    # get_comments=Comments.query.filter_by(pitch_id=id).all()
    comments =Comments.query.filter_by(pitch_id=pitch.id)
    form = CommentForm()
    if form.validate_on_submit():
        title=form.comment.data
        comment=form.comment.data

        new_comment=Comments(comment_title=title,comment=comment,pitch_id=id, posted_by=current_user.username)
        db.session.add(new_comment)
        db.session.commit()

    return render_template('pitch.html',pitch=pitch,comment=comments,comment_form=form)  