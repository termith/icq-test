from icq_client import IcqTestClient
import unittest
import const


class TestIcqLogin(unittest.TestCase):
    def setUp(self):
        self.client = IcqTestClient('291140261', 'password')

    def test_correct_credentials(self):
        login_status, login_data = self.client.do_login()
        assert login_status != const.INTERNAL_ERROR_CODE, 'Internal error! See log for more details'
        assert login_status == const.EXTERNAL_LOGIN_OK, 'Cannot login with correct credentials'
        assert login_data.get('loginId', '') == self.client.login, 'Wrong login id returned in response'

    def test_incorrect_credentials(self):
        self.client.password = 'wrongpassword'
        login_status, _ = self.client.do_login()
        assert login_status != const.INTERNAL_ERROR_CODE, 'Internal error! See log for more details'
        assert login_status == const.EXTERNAL_LOGIN_ERROR, 'Incorrect login status'

    def test_empty_credentials(self):
        self.client.login = str()
        self.client.password = str()
        login_status, _ = self.client.do_login()
        assert login_status != const.INTERNAL_ERROR_CODE, 'Internal error! See log for more details'
        assert login_status == const.EXTERNAL_LOGIN_MISSING, 'Incorrect login status'


if __name__ == '__main__':
    unittest.main()
