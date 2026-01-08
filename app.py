from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Insert, String
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_ID = os.getenv('EMAIL_ID')
PASSWORD = os.getenv('PASSWORD')


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.secret_key = 'bd83y7dhbh81w21q'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
db.init_app(app)


class Project(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    link: Mapped[str] = mapped_column(unique=True, nullable=False)
    image: Mapped[str] = mapped_column(nullable=False)


@app.route('/')
def index():
    result = db.session.execute(db.select(Project))
    projects = result.scalars()
    return render_template('index.html', projects=projects)


@app.route('/connect', methods=['POST'])
def connect():
    if request.method == 'POST':
        data = request.form
        # print(data['name'], data['email'], data['phone'], data['message'])
        status = send_mail(data['name'], data['email'], data['phone'], data['message'])
        # print(status)
        if status == 'failed':
            flash('Error sending message!', 'danger')
        else:
            flash('Message sent successfully.', 'success')

        return redirect(url_for('index'))


def send_mail(name, email, phone, msg):
    email_msg = f"Subject: New Message\n\nName: {name}\nemail_id: {email}\nPhone No. {phone}\nMessage: {msg}\n"
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(EMAIL_ID, PASSWORD)
            connection.sendmail(EMAIL_ID, EMAIL_ID, email_msg)
        return 'success'

    except Exception as e:
        print(e)
        return 'failed'
    

@app.route('/admin')
def admin():
    result = db.session.execute(db.select(Project))
    projects = result.scalars()
    
    return render_template('admin.html', projects=projects)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        data = request.form
        project = db.get_or_404(Project, id)
        project.title = data['title']
        project.description = data['description']
        project.link = data['link']
        project.image = data['image']
        db.session.commit()
        flash('Project updated successfully.', 'success')
        return redirect(url_for('admin'))
    
    project = db.get_or_404(Project, id)
    return render_template('edit.html', project=project)



if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
