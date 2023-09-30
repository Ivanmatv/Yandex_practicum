from django.contrib.auth import get_user_model
from django.test import TestCase
from posts.models import Post

User = get_user_model()


class TaskModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.post = Post.objects.create(
            author=User.objects.create_user(username='test_name',
                                            email='test@mail.ru',
                                            password='test_pass',),
            text='Тестовая запись для создания нового поста'
        )

    def test_object_name_is_title_fild(self):
        post = TaskModelTest.post
        expected_object_name = post.text[:15]
        self.assertEqual(expected_object_name, str(post))
