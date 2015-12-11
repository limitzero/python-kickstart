##__Python Kick-Starter__
This is a sample repository for jump-starting TDD/BDD katas and other python-based projects via a small template.

####Before you start
1. Install the [python run-time](https://www.python.org/downloads/) and make sure that the path to the python.exe is included in your environment variables under the PATH entry. 
2. Install the python package manager (pip) via the instructions [here](https://pip.pypa.io/en/stable/installing/). If the install of python has the package manager, you can simply type "pip list" at any command prompt and it will display the version of pip and any python packages that you have installed. 
3. Next, using pip you will need to install [py.test](http://pytest.org/latest/) and [watchdog] (https://github.com/gorakhargosh/watchdog) as utilities to aid in the feed-back cycle for unit-testing. 
4. At the command prompt type "pip install py.test" to install the unit testing framework and "pip install watchdog" for the utility to watch files for changes. 

###Configuring py.test for specification testing
From the contents of the repository, py.test.init tells py.test how to find your tests for execution inside of its engine (full explanation of the configuration is found on the py.test website).  For specification testing, the file has been changed as follows:

[pytest]
python_files=*_specs.py   --> this tells the engine what files to look for (in a wildcard fashion)
python_classes=describe_* --> this tells the engine what classes make-up the testing suite
python_functions=it_*  --> this tells the engine what are the test methods in the test suite

For example a basic test in python can look like this:

```python
"""
module		: calculator_specs.py
description	: test suite for behavior involving a simple calculator
"""
from calculator import StringCalculator

class describe_calculator:
	"""
	"""
	def setup_class(self): # this is like a constructor xUnit style, you cannot use __init__ in py.test!!!
		self._calculator = StringCalculator()

	def it_should_return_zero_when_an_empty_string_is_submitted(self):
		assert self._calculator.add("") == 0
	

	def it_should_return_the_sum_of_a_series_of_delimited_numbers(self):
		assert self._calculator.add("1,2,3,4") ==  10


	def it_should_return_the_sum_of_a_series_of_delimited_numbers_with_newline(self):
		assert self._calculator.add("1\n2,3,4") == 10


	def it_should_select_the_delimiter_after_two_backslashes_and_sum_the_series(self):
		assert self._calculator.add("//;1;2;3;4") == 10
```
with the object "calculator" as follows (based on string calculator code kata):
```python
"""sample kata for a simple calculator
"""
class StringCalculator(object):
	"""
	"""
	def add(self, numbers):
		if numbers == "": return 0
		default_delimiter = ","
		custom_delimiter_marker = "//"

		numbers = numbers.replace("\n",default_delimiter)

		if custom_delimiter_marker in numbers:
			delimiter_with_series = numbers.split(custom_delimiter_marker)
			requested_delimiter = ""
			for character in delimiter_with_series[1]:
				if character.isdigit():
					break
				else:
					requested_delimiter += character
			default_delimiter = requested_delimiter

		if default_delimiter in numbers:
			digits = numbers.split(default_delimiter)
			sum = 0
			for digit in digits:
				if not digit.isdigit():
					continue
				else:
					sum += int(digit)
			return sum
```
### Setting up the feed-back cycle for testing 
In order to setup the feed-back cycle for testing, open a command prompt in the directory of your tests and type "watch".  A shell script will run that is looking for any changes to files that match the criteria in py.test.ini and after the files are found, the runner executes the tests in the test file that has changed.

Enjoy :)