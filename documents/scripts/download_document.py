
import requests
import os

url = 'https://www.dane.gov.co/files/operaciones/PM/pres-PM-2022.pdf'

media_directory = os.path.join('documents', 'Media')
os.makedirs(media_directory, exist_ok=True)  
file_path = os.path.join(media_directory, 'pres-PM-2022.pdf')

response = requests.get(url)

with open(file_path, 'wb') as file:
    file.write(response.content)

print(f'Documento guardado en {file_path}')
