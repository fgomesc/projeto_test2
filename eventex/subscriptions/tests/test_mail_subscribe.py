from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Henrique Bastos', cpf='12345678901', email='henrique@bastos.net', phone='21-99618-6180')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_post(self):
        """Valid POST should redirect to /inscricao/"""
        self.assertEqual(302, self.resp.status_code)

    def test_send_subscribe_selfemail(self):
        self.assertEqual(1, len(mail.outbox))

    def test_subscription_selfemail_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_selfemail_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_selfemail(self):
        expect = ['contato@eventex.com.br', 'henrique@bastos.net']
        self.assertEqual(expect, self.email.to)

    def test_subsription_selfemail_body(self):
        contents = ['Henrique Bastos',
                    '12345678901',
                    'henrique@bastos.net',
                    '21-99618-6180'
                    ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
            self.assertIn('Henrique Bastos', self.email.body)