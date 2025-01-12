from django.db import models

from learningDjango.db_connection import db
# Create your models here.

usersCollection = db['users']
sequencesCollection = db['sequences']
