from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from ..models import Group, Post
from posts.forms import PostForm


User = get_user_model()


class PostFormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='Ivan')
        Post.objects.create(
            text='Тестовый пост',
            author=cls.user,
            group=Group.objects.create(
                title='Тестовая группа',
                slug='test-slug',
                description='Тестовое описание'
            )
        )
        cls.form = PostForm()

    def setUp(self):
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_create_post(self):
        posts_count = Post.objects.count()
        form_data = {
            'author': 'Ivan',
            'text': 'Тестовый пост',
            'group': Group,
        }

        response = self.authorized_client.post(
            reverse('posts:post_create'),
            data=form_data,
            follow=True
        )

        self.assertEqual(Post.objects.count(), posts_count + 1)

        self.assertTrue(
            Post.objects.filter(
                author='Ivan',
                text='Тестовый пост',
                group=Group.title
            ).exists()
        )
        self.assertEqual(response.status_code, 200)

    def test_post_edit_form(self):
        """Валидная форма редактирует запись в Post."""
        posts_count = Post.objects.count()
        form_data = {
            'text': 'Пост изменен',
        }
        response = self.authorized_client.post(
            reverse('posts:post_edit', args={{self.post.id}}),
            data=form_data,
            follow=True
        )
        redirect = reverse('users:login') + '?next=/create/'
        self.assertRedirects(response, redirect)
        self.assertEqual(Post.objects.count(), posts_count)
        self.assertEqual(response.status_code, 200)
