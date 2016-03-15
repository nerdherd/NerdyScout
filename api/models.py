from django.db import models

# Create your models here.
class team(models.Model):
    teamName = models.CharField(max_length=50, blank=False)
    teamNumber = models.IntegerField(blank=False)
    numberOfMatches = models.IntegerField(default=0)
    maxScore = models.IntegerField(default=0)
    minScore = models.IntegerField(default=0)
    avgScore = models.IntegerField(default=0)

    class Meta:
        db_table = 'teams'

class match(models.Model):
    DEFENSE_A = (
        ("P", "Portcullis"),
        ("CF", "Cheval de Frise"),
    )
    DEFENSE_B = (
        ("M", "Moat"),
        ("R", "Ramparts"),
    )
    DEFENSE_C = (
        ("D", "Drawbridge"),
        ("SP", "Sally Port"),
    )
    DEFENSE_D = (
        ("RW", "Rock Wall"),
        ("RT", "Rough Terrain"),
    )

    matchNumber = models.IntegerField(blank=False)
    team        = models.ForeignKey("team", on_delete=models.CASCADE, blank=False)

    defenseA    = models.CharField(max_length=2, choices=DEFENSE_A, default="P")
    defenseB    = models.CharField(max_length=2, choices=DEFENSE_B, default="M")
    defenseC    = models.CharField(max_length=2, choices=DEFENSE_C, default="D")
    defenseD    = models.CharField(max_length=2, choices=DEFENSE_D, default="RW")

    defenseACross   = models.IntegerField(default=0)
    defenseBCross   = models.IntegerField(default=0)
    defenseCCross   = models.IntegerField(default=0)
    defenseDCross   = models.IntegerField(default=0)
    lowBarCross     = models.IntegerField(default=0)

    batterShot      = models.IntegerField(default=0)
    courtyardShot   = models.IntegerField(default=0)
    defenseShot     = models.IntegerField(default=0)

    class Meta:
        db_table = 'matches'
