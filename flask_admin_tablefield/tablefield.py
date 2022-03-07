# coding:utf8
from wtforms.fields.core import StringField
from jinja2 import Template

import os
import traceback
import json

import copy

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TableField(StringField):

	# 表头
	headers = []
	is_showing_btn = True

	def __new__(cls,*args,**kwargs):

		if kwargs.get('headers') is not None or (args and isinstance(args[0], list)):
			headers = kwargs.get('headers') or args[0]
			#clone = copy.deepcopy(cls)
			clone = type(str(abs(hash(str(headers)))),(cls,),{})
			clone.headers = headers
			if kwargs.get('is_showing_btn') is not None:
				clone.is_showing_btn = kwargs.get('is_showing_btn')
			return clone
		else:
			return super().__new__(cls,*args, **kwargs)

	def process_formdata(self, valuelist=None, **args):
		
		if valuelist:
			try:
				self.data = valuelist[0]
			except Exception as e:
				raise ValueError("数据格式加载出错！")
		else:
			self.data = "[]"

	def __call__(self, **kwargs):
		try:
			json_data = json.loads(self.data)
		except:
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
			is_showing_btn=self.is_showing_btn
		)
