import json

from django.test import TestCase
from django.core.urlresolvers import reverse

from backend.models import *

# Create your tests here.

####################
# HELPER FUNCTIONS #
####################


class TaskMethodsTests(TestCase):
    def test_json_detail(self):
        """
        The @ref Task.json_detail method should return a dictionnary in the
        adequate format.
        """
        pass

class TaskDetailsTests(TestCase):
    def sign_in(self):
        """
        Log in as a test user to authenticate for further testing.
        """
        u = User.objects.create(first_name = "Testing",
                last_name = 'Tester',
                password='******',
                email='testing.tester@mom.com',
                phone_number='000-000-0000')
        self.client.session['user_pk'] = u.pk
