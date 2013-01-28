404 Django Project

## Prerequisites

- python &gt;= 2.5
- pip
- virtualenv

## Installation

### Clone the code

```bash
git clone git://git.constantvzw.org/osp.work.404.www
cd osp.work.404.www


### Creating the environment

Create a virtual python environment for the project.
If you're not using virtualenv you may skip this step.

```bash
virtualenv --no-site-packages zfz-env
source zfz-env/bin/activate
```

### Install the requirements

```bash
cd fzf
pip install -r requirements/common.txt
```

Depending on the your profile (development or production), install the extra
requirements.

In a development environment, run:

```bash
pip install -r requirements/dev.txt
```
In a production environment, run:

```bash
pip install -r requirements/prod.txt
```

### Configure the project

```bash
cp fzf/local_settings.example.py fzf/local_settings.py
vi fzf/local_settings.py
```

### Synchronize the database

```bash
python manage.py syncdb
```

## Run the project

```bash
python manage.py runserver
```

Open you browser at <http://localhost:8000>.
