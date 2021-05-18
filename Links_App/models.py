from django.db import models
from Slices_App.models import Slices_Model
from django.core.validators import MinValueValidator


# Links model
class Links_Model(models.Model):
    my_Slice = models.ForeignKey(Slices_Model, on_delete=models.CASCADE)
    icon_Image = models.URLField(max_length=400, blank=True, null=True)
    display_Name = models.CharField(max_length=40)
    sub_Name = models.CharField(max_length=20, blank=True, null=True)
    link_url = models.URLField(max_length=400)

    visibility = models.CharField(
        max_length=10,
        choices=[
            ('private', 'Private', ),
            ('public', 'Public', ),
        ],
        default='public'
    )
    clicks = models.IntegerField(
        default=0, blank=False, null=False,
        validators=[MinValueValidator(0), ]
    )

    def __str__(self, *args, **kwargs):
        return f'{self.my_Slice} -> `{self.id}`'
