from django.test import TestCase
from django.core.files import File
from .models import Image


class GalleryModelTest(TestCase):

    def test_gallery_model_save_and_retrieve(self):
        image1 = Image(
            title='image 1',
            image=File(open('test_images/test_image_1.png', 'rb'))
        )
        image1.save()

        image2 = Image(
            title='image 2',
            image=File(open('test_images/test_image_2.png', 'rb'))
        )
        image2.save()

        all_images = Image.objects.all()

        self.assertEqual(len(all_images), 2)

        self.assertEqual(
            all_images[0].title, image1.title
        )

        self.assertEqual(
            all_images[0].image, image1.image
        )

        self.assertEqual(
            all_images[1].title, image2.title
        )

        self.assertEqual(
            all_images[1].image, image2.image
        )
