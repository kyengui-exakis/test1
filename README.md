# Purpose

This repository is a starter kit template that allow squad to start developing databricks workflows following the best tech practices.

It provides
- A CI/CD that packages and deploy databricks workflows
- Example of job deployment
- Unit tests
- Integration tests
- SonarQube

Note: 
- This repository does not contain the infrastructure to provide a databricks workspace
- **dbx** has been deprecated and replaced by [Databricks Asset Bundles](https://docs.databricks.com/en/dev-tools/bundles/index.html), for more details read [here](https://docs.databricks.com/en/archive/dev-tools/dbx/index.html)

# System Requirements
- [Java](https://ubuntu.com/tutorials/install-jre#2-installing-openjdk-jre) (version >= 8)
- [Poetry](https://python-poetry.org/) (version > = 1.6.1)
- [Databricks-cli](https://docs.databricks.com/en/dev-tools/cli/install.html) (version > = 0.205)

# Devs tools

* Testing: [Pytest](https://docs.pytest.org/en/latest/)
* Linter and Formatter: [Ruff](https://docs.astral.sh/ruff/)
* Static type checker: [Mypy](https://mypy.readthedocs.io/en/stable/index.html)
* Security checks: [Skjold](https://pypi.org/project/skjold/)
* CLI Build helper: [Nox](https://nox.thea.codes/en/stable/)

# Getting Started:
## Install dependencies
```bash
make install
```

## Local Development

1. Generate a token for DEV profile from the databricks interface.
In the web interface of the workspace click on  : `User settings` -> `User` ->  `Developer` -> `Generate new token`.

2. Configure Databricks profiles : 

Option 1: 
- Edit `~/.databrickscfg`
```
[DEV]
host = https://adb-xxxxxxx.azuredatabricks.net/
token = xxxxxxxx
```
Option 2: 
- Use the following command line and fill the host name and the generated token:
```
databricks configure --profile DEV
```

You can verify your databricks auth profiles
```
databricks auth profiles
```
3. Deploy your first job to Databricks

```
databricks bundle deploy
```

and then run it

```
databricks bundle run multi_task_job
```

## Modifying your deployment

In order to modify your deployment and/or adding new jobs there are two important files **databricks.yml** and configuration files under **ressouces/** .

Before deploying the new bundle, you need to validate the yml file by :

```
databricks bundle validate
```
For a demo of how Databricks Asset Bundles Work, see [here](https://app.getreprise.com/launch/W68Ng9X/).

## Coding Standards:

Run the following command to format the code:

```bash
make format
```

Run the linter checks:
```bash
make lint
```
## Testing

### Running unit tests

For unit testing, run the following command:
```
make tests
```

Tests with coverage:
```
make tests-with-coverage
```

Please check the directory `tests/unit` for more details on how to use unit tests.
In the `tests/unit/conftest.py` you'll also find useful testing primitives, such as local Spark instance and DBUtils fixture.

#### Running integration tests
Deployment of integration tests are under ressources/integration_tests.yml.
Integration tests are deployed as regular jobs, so you can deploy/run them using:

```
databricks bundle run my_integration_test
```

## Do you want to contribute ?

This template must keep improving and evolving.
Plase find more details about how to contribute to this starter kit [here](https://github.com/TotalEnergiesCode/databricks-starter-kit/blob/main/CONTRIBUTING.md).

### Contacts' information:
Contact the Starter Kit Management Committee (SKMC) in case contributors have questions or need assistance.
[Houyem AYDI](mailto:houyem.aydi@totalenergies.com),
[Adrien HERENG](mailto:adrien.hereng@totalenergies.com),
[Mohammed TAHA EL AHMAR](mailto:mohammed-taha.el-ahmar@totalenergies.com)
