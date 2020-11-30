from django.db import models

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=200, unique=True, null=False)
    email = models.EmailField(max_length=254, unique=True, null=False)
    password = models.CharField(max_length=128)

    # Define __repr__ that will be called when querying e.g. 'Users.query.all()'
    def __repr__(self):
        obj_repr = f'ID: {self.id},' \
                   f'Username: {self.username},' \
                   f'Email: {self.email},' \
                   f'Password: {self.password}' \

        return obj_repr
