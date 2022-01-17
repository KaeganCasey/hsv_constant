"""
Extension classes enhance TouchDesigner components with python. An
extension is accessed via ext.ExtensionClassName from any operator
within the extended component. If the extension is promoted via its
Promote Extension parameter, all its attributes with capitalized names
can be accessed externally, e.g. op('yourComp').PromotedFunction().

Help: search "Extensions" in wiki
"""

from TDStoreTools import StorageManager
import TDFunctions as TDF

class HSVConstantExt:
	"""
	HSVConstantExt description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.source_params = self.collect_params(
			sourceOP=self.ownerComp, 
			param_list=['H', 'S', 'V', 'A']
			)

		print('init')

	def collect_params(self, sourceOP, param_list):
		return [sourceOP.par[i] for i in param_list]


	def collect_tuple_params(self, sourceOP, param_prefix, num_params=4, offset=1):
		return [sourceOP.par[param_prefix + str(i + offset)] for i in range(num_params)]

	def OnHsvChange(self):
		targetOP = op('constant2')
		target_params = self.collect_tuple_params(
			sourceOP=targetOP, 
			param_prefix='value', 
			num_params=4, 
			offset=0
			)

		hsv_values = [i.val for i in self.source_params]
		rgb_values = mod.colorsys.hsv_to_rgb(*hsv_values[:3])
		rgb_values_list = list(rgb_values)
		rgb_values_list.append(hsv_values[3])

		for idx, val in enumerate(rgb_values_list):
			target_params[idx].val = val


