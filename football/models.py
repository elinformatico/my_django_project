from django.db import models

class Coach(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
        
class Team(models.Model):
    name = models.CharField(max_length=200)
    coach = models.ForeignKey(Coach)

    def __unicode__(self):
        return u"{name} {team}".format(name=self.name, team=self.coach.name)

class Player(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team)

    def __unicode__(self):
        return u"{name} {team}".format(name=self.name, team=self.team.name)


