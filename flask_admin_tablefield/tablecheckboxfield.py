from wtforms.fields.core import StringField
from jinja2 import Template
import copy
import json
import os

class TableCheckBoxField(StringField):

	first_head_cell = "#"

	def __new__(cls,*args,**kwargs):

		if kwargs.get('table_data') is not None or (args and isinstance(args[0], dict)):
			table_data = kwargs.get('table_data') or args[0]
			clone = type(str(abs(hash(str(table_data)))),(cls,),{})
			clone.init_data = table_data
			if kwargs.get('first_head_cell') is not None:
				clone.first_head_cell = kwargs.get('first_head_cell')
			return clone
		else:
			return super().__new__(cls,*args, **kwargs)

	def process_formdata(self, valuelist=None, **args):

		try:
			data = copy.deepcopy(self.init_data)
			if valuelist:
				for option in valuelist:
					_class,_day = option.split(":")
					data[_class][_day] = 1

			self.data = json.dumps(data)
		except Exception as e:
			raise e
			self.data = data
			raise ValueError("表数据格式错误！")

	def __call__(self, **kwargs):

		try:
			table_data = json.loads(self.data)
		except:
			table_data = copy.deepcopy(self.init_data)

		template = None
		with open(os.path.join(os.path.dirname(__file__),'templates','tablecheckboxfield.html'), 'r', encoding='utf-8') as f:
			html = f.read()
			template = Template(html)

		return template.render(
			first_head_cell=self.first_head_cell,
			table_data=table_data,
			field_id=self.id,
		)