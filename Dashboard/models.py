from django.db import models
from django.contrib.auth.models import User


class Domain(models.Model):
    domain_name = models.CharField('Domain Name', max_length=30)

    def __str__(self):
        return self.domain_name

    def get_domain(self):
        return self.domain_name
    
class Questions(models.Model):
    que_id = models.CharField('Question Id', max_length=5)
    que_title = models.CharField('Title Name', max_length=150)
    que_link = models.URLField('Question Link')
    que_domain = models.ManyToManyField(Domain, blank = True)
    que_difficulty = models.CharField('Difficulty Level', max_length=10)
    dsa_sheet = models.CharField('DSA Sheet', max_length=2) #L - Love Babbar; F - Fraz; S - Striver; A - Apna College

    def __str__(self):
        return self.que_title
    
    def get_que_id(self):
        return self.que_id

    def get_que_link(self):
        return self.que_link

    def get_que_domain(self):
        return self.que_domain.all()

    def get_que_difficulty(self):
        return self.que_difficulty

class Student(models.Model):
    first_name = models.CharField('First Name', max_length=15, blank = True)
    last_name = models.CharField('Last Name', max_length=15, blank = True)
    username = models.CharField('Username', max_length=30, blank = True)
    email = models.EmailField('User Email', blank = True)
    que_ids = models.ManyToManyField(Questions, blank = True)
    
    def __str__(self):
        return self.first_name+' '+self.last_name

    def get_que_id(self):
        return self.que_ids.all()