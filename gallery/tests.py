from django.test import TestCase
from .models import Category, Image
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime

class GalleryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Nature')
        image_file = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
        self.image = Image.objects.create(
            title='Test Image',
            image=image_file,
            created_date=datetime.date.today(),
            age_limit=12
        )
        self.image.categories.add(self.category)

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Nature')

    def test_image_creation(self):
        self.assertEqual(self.image.title, 'Test Image')
        self.assertEqual(self.image.age_limit, 12)
        self.assertIn(self.category, self.image.categories.all())

    def test_image_str(self):
        self.assertEqual(str(self.image), 'Test Image')
