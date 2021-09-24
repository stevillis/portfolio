from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


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
