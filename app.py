from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Insert, String

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


# with app.app_context():
#     result = db.session.execute(db.select(Project))
#     print(result.scalar())




@app.route('/')
def index():
    result = db.session.execute(db.select(Project))
    projects = result.scalars()
    # for d in data:
    #     print(d.title)
    return render_template('index.html', projects=projects)


if __name__ == '__main__':
    app.run(debug=True)
