import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from stdimage import StdImageField


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Alterado em'), auto_now=True)
    created_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_related_created_by", null=True,
                                   blank=True, default=None, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_related_updated_by", null=True,
                                   blank=True, default=None, on_delete=models.CASCADE)
    active = models.BooleanField(_('Ativo'), default=True)
    deactivated_at = models.DateTimeField(_('Inativado em'), null=True, blank=True)

    class Meta:
        abstract = True


class Academy(BaseModel):
    name = models.CharField(_('Nome'), max_length=100, null=False, blank=False)
    description = models.TextField(_('Descrição'), max_length=200, null=True, blank=True)
    logo = StdImageField(_('Logo'), upload_to=get_file_path,
                         variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    class Meta:
        verbose_name = _('Academia')
        verbose_name_plural = _('Academias')

    def __str__(self):
        return self.name


class Course:
    pass


class Training:
    pass
