from __future__ import absolute_import, unicode_literals
import urllib.request
import os
from celery import shared_task

@shared_task
def download_and_save_document():
    url = 'https://www.dane.gov.co/files/operaciones/PM/pres-PM-2022.pdf'
    media_directory = os.path.join('documents', 'Media')
    file_path = os.path.join(media_directory, 'pres-PM-2022.pdf')

    os.makedirs(media_directory, exist_ok=True)

    try:
        with urllib.request.urlopen(url) as response:
            with open(file_path, 'wb') as file:
                file.write(response.read())

        return f'Documento guardado en {file_path}'

    except Exception as e:
        return f'Error al descargar el documento: {str(e)}'
