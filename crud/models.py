from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField(default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")


    def __str__(self):
        return self.title


class Contacts(models.Model):
    name = models.CharField(max_length=150)
    email =  models.EmailField()

    def __str__(self):
        return self.name