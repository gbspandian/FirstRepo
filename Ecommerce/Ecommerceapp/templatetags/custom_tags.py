import os
from django import template
from pathlib import Path
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile

register = template.Library()

@register.filter
def basename(value):
  return os.path.abspath(value)

@register.filter
def get_last_path_value(path_str):
  return Path(path_str).name

@register.filter
def create_thumbnail(image_field, size=(100, 100), format='JPEG'):
    # Open the original image
    #image_field = basename(image_field)
    image = Image.open(image_field)
    
    # Convert to RGB if necessary (e.g., if PNG with transparency)
    if image.mode in ('RGBA', 'P'):
        image = image.convert('RGB')
        
    # Resize keeping aspect ratio or thumbnail method
    image.thumbnail(size)
    
    # Save to an in-memory buffer
    buffer = BytesIO()
    image.save(buffer, format=format, quality=85)
    buffer.seek(0)

    # Return as a Django ContentFile
    #filename = f"thumb_{image_field.name.split('/')[-1]}"
    filename = basename(image_field)
    return ContentFile(
      buffer.read(), name=f"thumb_{getattr(image_field, 'name', 'img.jpg')}"
  )