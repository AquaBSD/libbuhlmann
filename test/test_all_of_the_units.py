import unittest
import gen_dive
from StringIO import StringIO


class TestGenDiveMethod(unittest.TestCase):
	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		# check that s.split fails when the separator is not a string
		with self.assertRaises(TypeError):
			s.split(2)

	def test_gen_dive(self):
		btime = 20
		maxdepth = 20
		gases = []
		decogasses = []
		dict = {}
		dict['depth'] = 0.0
		dict['o2'] = .21
		dict['he'] = 0.0
		gases.append(dict)
		strout = StringIO()
		gen_dive.generate_dive(btime, maxdepth, gases, decogasses, strout)
		listtest = strout.getvalue().strip().split('\n')
		#test first value of the dive generated
		self.assertEqual(listtest[0],"0.00 1.00 0.21 0.00")
		self.assertEqual(listtest[0],"0.00 1.00 0.21 0.00")


if __name__ == '__main__':
    unittest.main()