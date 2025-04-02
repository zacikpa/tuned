#!/usr/bin/env python3

import argparse
import sys
import inspect
from tuned.utils.class_loader import ClassLoader
from tuned.plugins.base import Plugin
from tuned.profiles.functions.base import Function


class PluginDocLoader(ClassLoader):
	def __init__(self):
		super(PluginDocLoader, self).__init__()

	def _set_loader_parameters(self):
		self._namespace = "tuned.plugins"
		self._prefix = "plugin_"
		self._interface = Plugin


class FunctionDocLoader(ClassLoader):
	def __init__(self):
		super(FunctionDocLoader, self).__init__()

	def _set_loader_parameters(self):
		self._namespace = "tuned.profiles.functions"
		self._prefix = "function_"
		self._interface = Function


CLASS_LOADER_MAP = {
	"plugins": PluginDocLoader,
	"functions": FunctionDocLoader
}


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("type")
	parser.add_argument("intro")
	parser.add_argument("out")
	args = parser.parse_args()

	try:
		doc_loader = CLASS_LOADER_MAP[args.type]()
	except IndexError:
		print("Invalid class specified.", file=sys.stderr)
		sys.exit()

	with open(args.intro, "r") as intro_file:
		intro = intro_file.read()

	all_classes = sorted(doc_loader.load_all_classes(), key=lambda x: x.__module__)

	with open(args.out, "w") as out_file:
		out_file.write(intro)
		for class_obj in all_classes:
			class_file = inspect.getfile(class_obj)
			out_file.write("\n")
			out_file.write("== **%s**\n" % class_obj.__module__.split(".")[-1].split("_", 1)[1])
			out_file.write(inspect.cleandoc(class_obj.__doc__))
			out_file.write("\n")
