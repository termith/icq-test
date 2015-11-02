import requests
import traceback
import json
import logging

import const


class IcqTestClient(object):
    CLIENT_LOGIN_URL = 'https://api.login.icq.net/auth/clientLogin'
    CONNECTION_TIMEOUT = 60 * 1000
    DEV_ID = 'ic1Ytjc4pxslFTEL'
    CLIENT_NAME = 'Test Icq Client'
    CLIENT_VERSION = '1.0'

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def _make_login_params(self):

        login_params = {
            const.CLIENT_NAME_FIELD: self.CLIENT_NAME,
            const.CLIENT_VERSION_FIELD: self.CLIENT_VERSION,
            const.DEV_ID_FIELD: self.DEV_ID,
            const.FORMAT_FIELD: 'json',
            const.ID_TYPE_FIELD: 'ICQ',
            const.PASSWORD_FIELD: self.password,
            const.LOGIN_FIELD: self.login
        }
        return login_params

    def do_login(self):
        try:
            logging.info('Login with credentials: %s, %s' % (self.login, self.password))
            response = requests.post(self.CLIENT_LOGIN_URL, data=self._make_login_params(),
                                     timeout=self.CONNECTION_TIMEOUT)
            if response.status_code == 200:
                res_content = json.loads(response.text).get('response', {})
                return res_content.get('statusCode', 0), res_content.get('data', {})
            else:
                logging.error('Server returns %s instead of 200' % response.status_code)
                return const.INTERNAL_ERROR_CODE, {}
        except requests.exceptions.Timeout:
            logging.error('Timeout reached while connecting to server')
            logging.info(traceback.format_exc())
            return const.INTERNAL_ERROR_CODE, {}


if __name__ == '__main__':
    c = IcqTestClient('291140261', 'password')
    print(c.do_login())
