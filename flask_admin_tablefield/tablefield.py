# coding:utf8
from wtforms.fields.core import StringField
from jinja2 import Template

import os
import traceback
import json


# import logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

class TableField(StringField):

	# 表头
	headers = []

	def __new__(cls,*args,**kwargs):

		if kwargs.get('headers') is not None or (args and isinstance(args[0], list)):
			cls.headers = kwargs.get('headers') or args[0]
			return cls
		else:
			# print('__new__')
			# print(cls)
			# print(args)
			# print(kwargs)
			return super().__new__(cls,*args, **kwargs)

	def process_formdata(self, valuelist=None, **args):

		# logger.debug('>>> process_formdata')
		# logger.debug(self.data)
		# logger.debug(valuelist)
		
		if valuelist:
			try:
				self.data = valuelist[0]
			except Exception as e:
				raise ValueError("数据格式加载出错！")
		else:
			self.data = "[]"

	def __call__(self, **kwargs):

		# logger.debug('>>> __call__')
		# logger.debug(self.headers)
		try:
			json_data = json.loads(self.data)
		except:
			# logger.debug('>> loads error!')
			# logger.debug(self.data)
			# logger.debug(traceback.format_exc())
			json_data = []

		table_id='table_'+self.id

		template = None
		with open(os.path.join(os.path.dirname(__file__),'templates','tablefield.html'), 'r', encoding='utf-8') as f:
			html = f.read()
			template = Template(html)

		return template.render(
			table_headers=self.headers,
			table_data=json_data,
			table_id=table_id,
			input_id=self.id,
		)
