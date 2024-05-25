import nox


SRC_FOLDERS = ["client", "server", "common"]


@nox.session
def format(session: nox.Session):
    session.install("black", "isort")
    session.run("isort", *SRC_FOLDERS)
    session.run("black", *SRC_FOLDERS)

@nox.session
def test(session: nox.Session):
    session.install("-r", "requirements.txt")
    session.install("-e", ".[testing]")
    session.run("pytest", "-s")
