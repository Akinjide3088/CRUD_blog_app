from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='secret',
        )


        self.post = Post.objects.create(
            title='A good title',
            body='Nice body',
            author=self.user
        )

    def test_string_representaion(self):
        post = Post('A simple title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 301)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')








   
#  <div class="nav-left">
#         <h1><a href="{% url 'home' %}">Ajay blog</a></h1>
#      </div>
#      <div class="nav-right">
#         <h1><a href="{% url 'post_new' %}">New Blog Post</a></h1>
#      </div>


    