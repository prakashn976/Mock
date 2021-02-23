from unittest import TestCase
from unittest.mock import patch, Mock
from BlogAPIService import Blog

class TestBlog(TestCase):
    @patch('BlogAPIService.Blog')
    def test_blog_posts(self, MockBlog):
        blog = MockBlog()

        blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
                'body': 'Test Body.'
            }
        ]

        response = blog.posts()
        self.assertIsNotNone(response) 
        self.assertIsInstance(response[0], dict)
