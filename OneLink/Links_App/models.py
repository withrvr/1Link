from django.db import models
from Slices_App.models import Slices_Model


# Links model
class Links_Model(models.Model):
    my_Slice = models.ForeignKey(Slices_Model, on_delete=models.CASCADE)
    icon_Image = models.URLField(max_length=400)
    display_Name = models.CharField(max_length=40)
    sub_Name = models.CharField(max_length=20)
    link_url = models.URLField(max_length=400)

    visibility = models.CharField(
        max_length=10,
        choices=[
            ('private', 'Private', ),
            ('public', 'Public', ),
        ],
        default='public'
    )

    '''
    number of time clicked
    '''

    def __str__(self, *args, **kwargs):
        return f'{self.my_Slice} -> `{self.id}`'
