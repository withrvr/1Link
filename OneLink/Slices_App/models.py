from django.db import models
from UsersProfile_App.models import UsersProfile_Model
from django.core.validators import RegexValidator


class Slices_Model(models.Model):
    author = models.ForeignKey(UsersProfile_Model, on_delete=models.CASCADE)
    slice_Name = models.CharField(
        max_length=30,
        help_text='Only Numbers, Lowecase-Letter and UserScore ( _ ) is allowed',
        validators=[RegexValidator(
            r'^[0-9a-z_]+$',
            message="Enter a valid Slice Name. Only Numbers, Lowecase-Letter and UserScore ( _ ) is allowed"
        )],
        error_messages={
            'unique': "This slice name all ready exist",
        },
    )
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

    class Meta:
        unique_together = (
            ('author', 'slice_Name', ),
        )

    def __str__(self, *args, **kwargs):
        return f'{self.author} -> `{self.slice_Name}`'
