from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    # setup function that is ran before every test that is ran. 
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password='password123'
        )
        self.client.force_login(self.admin_user) # login admin into client
        # spare user for testing
        self.user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='password123',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        # generate url for list user page
        url = reverse('admin:core_user_changelist')
        # use test client to perform http get on url
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""

        # args: /admin/core/user/<user_id>/
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
