from django.db import models
from stdimage import StdImageField
import uuid
from PIL import Image

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

# Create your models here.
class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Cliente(Base):
    nome = models.CharField('Nome',max_length=100)
    telefone = models.CharField('Telefone', max_length=15)
    email = models.CharField('E-mail', max_length=100)
    uf = models.CharField('Estado', max_length=2)
    cidade = models.CharField('Cidade', max_length=50)
    endereco = models.CharField('Endereço', max_length=100, null=True)
    imagem = StdImageField('Imagem', null=True, upload_to=get_file_path, variations={
        'thumb': {'width': 75, 'height': 75, 'crop': True}
    })
    #, auto_rotate = True
    depoimento = models.TextField('Depoimento', max_length=300, null=True)
    avaliacao = models.IntegerField('Avaliação', null=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def rotate_image(image_path):
        with Image.open(image_path) as img:
            if hasattr(img, '_getexif'):
                # Obtem os metadados da imagem
                exif = img._getexif()
                if exif is not None:
                    # Obtem a orientação da imagem
                    orientation = exif.get(0x0112)
                    if orientation == 3:
                        # Gira a imagem em 180 graus
                        img = img.rotate(180, expand=True)
                    elif orientation == 6:
                        # Gira a imagem em 270 graus (90 graus no sentido horário)
                        img = img.rotate(270, expand=True)
                    elif orientation == 8:
                        # Gira a imagem em 90 graus (sentido anti-horário)
                        img = img.rotate(90, expand=True)
                    # Salva a imagem rotacionada
                    img.save(image_path)

    def __str__(self):
        return self.nome
