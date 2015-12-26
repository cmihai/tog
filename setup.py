from setuptools import setup


setup(
	name='tog',
	version='1.0.0',
	py_modules=['tog'],
	install_requires=[
		'click',
	],
	entry_points='''
		[console_scripts]
		tog=tog:cli
	'''
)
