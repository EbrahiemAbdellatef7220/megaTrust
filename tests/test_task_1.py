from odoo.tests import HttpCase


class MyTest(HttpCase):
    def test_login_api(self):
        res = self.url_open('/trust/login?user_name=admin&password=admin').json()
        self.assertEqual(str(res['message']), 'Login Successful')

    def test_partner_api(self):
        res = self.url_open(f'/trust/company_partner?session_id=d89e178253fe1c7df8d307128450c997d9921942&company_id=1').json()
        self.assertEqual(str(res['message']), 'success')
