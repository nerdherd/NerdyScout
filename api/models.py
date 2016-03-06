from django.db import models

# Create your models here.
class team(models.Model):
    teamNumber = models.IntegerField(blank=False)
    numberOfMatches = models.IntegerField(default=0)
    maxScore = models.IntegerField(default=0)
    minScore = models.IntegerField(default=0)
    avgScore = models.IntegerField(default=0)

    class Meta:
        db_table = 'teams'

class match(models.Model):
    matchNumber = models.IntegerField(blank=False)
    team = models.ForeignKey("team", on_delete=models.CASCADE, blank=False)
    defenseA = (
        ("P", "Portcullis"),
        ("CF", "Cheval de Frise"),
    )
    defenseB = (
        ("M", "Moat"),
        ("R", "Ramparts"),
    )
    defenseC = (
        ("D", "Drawbridge"),
        ("SP", "Sally Port"),
    )
    defenseD = (
        ("RW", "Rock Wall"),
        ("RT", "Rough Terrain"),
    )

    class Meta:
        db_table = 'matches'
