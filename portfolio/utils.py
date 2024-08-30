import os
import uuid

def upload_project_image(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('projects/', new_filename)

