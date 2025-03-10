import nox


@nox.session
def tests(session: nox.Session) -> None:
    session.run("poetry", "run", "pytest", "tests/unit", external=True)


@nox.session
def tests_with_coverage(session: nox.Session) -> None:
    session.run(
        "poetry", "run", "pytest", "tests", "tests/unit", "--cov=.", "--cov-report", "xml:coverage.xml", external=True
    )


@nox.session
def format(session: nox.Session) -> None:
    session.run("poetry", "run", "ruff", "format", ".", external=True)


@nox.session
def lint(session: nox.Session) -> None:
    session.run("poetry", "run", "ruff", "check", "data_squad", "--fix", external=True)
    session.run("poetry", "run", "ruff", "check", "data_squad", external=True)
    session.run("poetry", "run", "ruff", "check", "tests", "--fix", external=True)
    session.run("poetry", "run", "ruff", "check", "tests", external=True)
    mypy(session)


@nox.session
def mypy(session: nox.Session) -> None:
    session.run("poetry", "run", "mypy", ".", "--install-types", "--non-interactive", external=True)


@nox.session
def security(session: nox.Session) -> None:
    session.run("bash", "-c", "poetry export -f requirements.txt | skjold -v audit -", external=True)
