import requests
import sys

class IcqTestClient(object):

	CLIENT_LOGIN_URL = 'https://api.login.icq.net/auth/clientLogin'

	CONNECTION_TIMEOUT = 60 * 1000
	DEV_ID = 'ic1Ytjc4pxslFTEL'
	CLIENT_NAME = 'Mandarin Android'
	CLIENT_VERSION = '1.0'

	EXTERNAL_LOGIN_OK = 200
	EXTERNAL_LOGIN_ERROR = 330
	INTERNAL_ERROR = 10000

	def __init__(self, login, password):
		self.login = login
		self.password = password

	def _make_login_params(self):
		login_params = {
		'clientName': self.CLIENT_NAME,
		'clientVersion': self.CLIENT_VERSION,
		'devId': self.DEV_ID,
		'f': 'json',
		'idType': 'ICQ',
		'pwd': self.password,
		's': self.login
		}
		return login_params

	def do_login(self):
		try:
			response = requests.post(self.CLIENT_LOGIN_URL, data=self._make_login_params(), timeout=self.CONNECTION_TIMEOUT)
			if response.status == EXTERNAL_LOGIN_OK:
				# Do some handle with response attributes
				return EXTERNAL_LOGIN_OK, response
			else if:
				response.status == EXTERNAL_LOGIN_ERROR:
				return EXTERNAL_LOGIN_ERROR, response
		except requests.exceptions.Timeout:
			# Log traceback or do something else
			return INTERNAL_ERROR, {}

if __name__ == '__main__':
	c = IcqTestClient('291140261', 'password')
	c.do_login()


