from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team)

    def __unicode__(self):
        return u"{name} {team}".format(name=self.name, team=self.team.name)