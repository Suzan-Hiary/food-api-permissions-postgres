from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Food

class BlogTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='testuser', password='password')
        test_user.save()

        food = Food.objects.create(
            author = test_user,
            name = 'Apple',
            body = "An apple is an edible fruit produced by an apple tree."
        )

        food.save()

    def test_blog_content(self):
        food = Food.objects.get(id=1)
        actual_author = str(food.author)
        actual_name = str(food.name)
        actual_body = str(food.body)
        self.assertEqual(actual_author, 'testuser')
        self.assertEqual(actual_name, 'Apple')
        self.assertEqual(actual_body, "An apple is an edible fruit produced by an apple tree.")