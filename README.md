# Introduction

This is a field for flask-admin. It can render a text(json) field into a table html that can be edited.

# Installation

```shell
pip install flask-admin-tablefield
```

# Usage

```python
from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text
from flask_bootstrap import Bootstrap
import os

basedir = os.path.abspath(os.getcwd())

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

db = SQLAlchemy()
bootstrap = Bootstrap()


app = Flask(__name__)

app.config.update({
	'SQLALCHEMY_DATABASE_URI':'sqlite:///' + os.path.join(basedir, 'tablefield.sqlite'),
	'SQLALCHEMY_TRACK_MODIFICATIONS':True,
	'SECRET_KEY':'xxx',
})
app_context = app.app_context()
app_context.push()

admin = Admin(
	app,
	name="tablefield-example",
	template_mode='bootstrap4',
)

class PlanModel(db.Model):
	__tablename__ = 'plan'

	id = Column(Integer, primary_key=True)
	plan = Column(Text(10800))

from flask_admin.contrib import sqla
from flask_admin_tablefield import TableField
class PlanAdmin(sqla.ModelView):

	column_labels = {'plan':'plan',}

	column_list = ['id',]

	form_overrides = {
		'plan':TableField([
			"#","Mon","Tue","Wed","Thu","Fri","Sat","Sun",
		]),
	}

admin.add_view(PlanAdmin(PlanModel, db.session, name=u'plan'))

db.init_app(app)
db.drop_all()
db.create_all()
db.session.commit()

bootstrap.init_app(app)

if __name__ == '__main__':
	app.run(debug=True)
```

Check http://localhost:5000/admin

![example](https://github.com/cllen/flask-admin-tablefield/blob/master/example.png?raw=true)

# Update

- [x] 2022年3月6日 add feature `TableField`
- [x] 2022年3月7日 add feature `TableCheckBoxField`
