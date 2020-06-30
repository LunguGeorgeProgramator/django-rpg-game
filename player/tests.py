from django.test import TestCase
from player.models import Player

class PlayerTestClass(TestCase):

    def setUp(self):
        self.player = Player.objects.create(
            email="test@email.com", 
            nume_utilizator="Test utilizator"
        )

    def tearDown(self):
        self.player.delete()

    def test_read_player(self):
        self.assertEqual(self.player.email, "test@email.com")
        self.assertEqual(self.player.nume_utilizator, "Test utilizator")

    def test_login_show_account_page(self):

        response = self.client.get('/profile/login')
        self.assertEqual(200, response.status_code)

        response = self.client.post('/profile/login', {
            'email': "test@email.com",
            'nume_utilizator': "Test utilizator"
        })
        self.assertEqual(302, response.status_code) # redirect to show account page
        self.assertRedirects(response, '/profile/' + str(self.player.id))

        response = self.client.get('/profile/' + str(self.player.id))
        self.assertEqual(200, response.status_code)