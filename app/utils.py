import os
import uuid
from recipe_site import settings


def generate_unique_filename(filename):
    _, ext = os.path.splitext(filename)
    new_filename = str(uuid.uuid4()) + ext
    return new_filename


def save_image(image_file):

    image_dir = settings.MEDIA_ROOT
    new_filename = generate_unique_filename(image_file.name)
    image_path = os.path.join(image_dir, new_filename)
    with open(image_path, 'wb') as f:
        for chunk in image_file.chunks():
            f.write(chunk)

    return new_filename
