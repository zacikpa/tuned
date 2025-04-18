from . import base

class CPUListOnline(base.Function):
	"""
	Returns a CPU list containing the online CPUs from the given CPU list.

	====
	On a system with 8 CPUs where the first 4 CPUs (0 to 3) are offline,
	the following returns `4-6`:
	----
	${f:cpulist_online:0-6}
	----
	====
	"""
	def __init__(self):
		# arbitrary number of arguments
		super(CPUListOnline, self).__init__(0)

	def execute(self, args):
		if not super(CPUListOnline, self).execute(args):
			return None
		cpus = self._cmd.cpulist_unpack(",".join(args))
		online = self._cmd.cpulist_unpack(self._cmd.read_file("/sys/devices/system/cpu/online"))
		return ",".join(str(v) for v in cpus if v in online)
