import re
from . import base

class RegexSearchTernary(base.Function):
	"""
	Ternary regex operator.

	It takes arguments in the following form:
	`STR1, REGEX, STR2, STR3`

	If `REGEX` is matched within `STR1`, returns `STR2`, otherwise returns `STR3`.
	"""
	def __init__(self):
		# 4 arguments
		super(RegexSearchTernary, self).__init__(4, 4)

	def execute(self, args):
		if not super(RegexSearchTernary, self).execute(args):
			return None
		if re.search(args[1], args[0]):
			return args[2]
		else:
			return args[3]
