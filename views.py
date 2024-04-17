from flask import Blueprint, render_template, request,flash, jsonify
from flask_login import login_required,current_user
from models import Note
from app import db
import json
from flask import url_for,redirect
from datetime import datetime, timedelta  # Import datetime module
from sqlalchemy.orm import validates


#creating blueprint named views
views = Blueprint('views', __name__)

#creating a route "/" in views aka home page which requires login to access
@views.route('/',methods=['GET','POST'])
@login_required

def home():
    current_date = datetime.now().date()  # Ensure current_date is a date object
    tomorrow_date = current_date + timedelta(days=1)

    if request.method == 'POST':
        note = request.form.get('note')
        due_date_str = request.form.get('duedate')

        if len(note) < 1:
            pass
        else:
            try:
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()  # Convert to date object
                validate_due_date( None, due_date)
            except ValueError as e:
                flash(str(e), 'error')
                return redirect(url_for('views.home'))

            new_note = Note(data=note, due_date=due_date, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            return redirect(url_for('views.home'))

    return render_template("index.html", user=current_user, current_date=current_date, tomorrow_date=tomorrow_date)

@validates('due_date')
def validate_due_date(key, due_date):
    if due_date < datetime.now().date():  # Ensure datetime.now().date() is a date object
        raise ValueError('Due date cannot be in the past.')
    return due_date


#we create another route which just takes the post method
@views.route('delete-note', methods=['POST'])
def delete_note():
    
    # we store the note to be deleted in a veriable called note
    note=json.loads(request.data)
    noteId = note['note']
    note = Note.query.get(noteId)
    #if the note exists and if the note's user_id is the same as current users id we delete the note and commit
    if note:
        if note.user_id==current_user.id:
            db.session.delete(note)
            db.session.commit()
            return jsonify({})
        
@views.route('/toggle-completed', methods=['POST'])
@login_required
def toggle_completed():
    data = json.loads(request.data)
    note_id = data['noteId']
    completed = data['completed']
    
    note = Note.query.get(note_id)
    if note and note.user_id == current_user.id:
        note.completed = completed
        db.session.commit()
        return jsonify({'message': 'Note completed status updated successfully'})
    else:
        return jsonify({'error': 'Note not found or unauthorized'})