from flask import Flask, render_template
from data import db_session
from data import jobs, users

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"


@app.route("/", methods=["GET", "POST"])
def main():
    a = []
    lst = []
    db_session.global_init("db/mars_explorer.sqlite")
    session = db_session.create_session()
    for i in session.query(jobs.Jobs):
        a.append(i.id)
        a.append(i.job)
        for user in session.query(users.User).filter(i.team_leader == users.User.id):
            a.append((user.name, user.surname))
        a.append(i.work_size)
        a.append(i.collaborators)
        a.append(i.is_finished)
        lst.append(a)
        a = []
    return render_template("main.html", title="Jobs", list=lst)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
