from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'joe blogs',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")
        
    def test_form_no_name(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="name was not provided but Form is valid")
        
    def test_form_no_email(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'joe bloggs',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="email was not provided but Form is valid")
        
    def test_form_no_message(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'joe bloggs',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="message was not provided but Form is valid")