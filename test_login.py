from icq_client import IcqTestClient
import unittest

class TestIcqLogin(unittest.TestCase):

	def setUp(self):
		client = IcqTestClient(str(), str())

	def test_correct_credentials(self):
		# Can log in with correct creds
		# Server availaible
		assert True

	def test_incorrect_credentials(self):
		# Cannot log in with incorrect creds
		# Correct status returned
		assert True

	def test_empty_credentials(self):
		# Cannot log in with incorrect creds
		# Correct status returned		
		assert True

if __name__ == '__main__':
	unittest.main()

