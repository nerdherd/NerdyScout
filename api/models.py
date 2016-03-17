from django.db import models

# Create your models here.
class team(models.Model):
    teamName = models.CharField('Team Name', max_length=50, blank=False)
    teamNumber = models.IntegerField('Team Number', blank=False)
    numberOfMatches = models.IntegerField(default=0)
    maxScore = models.IntegerField(default=0)
    minScore = models.IntegerField(default=0)
    avgScore = models.IntegerField(default=0)

    def __str__(self):
        return self.teamName

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

    ALLIANCES = (
        ("R", "Red"),
        ("B", "Blue"),
    )

    matchNumber = models.IntegerField('Match Number', blank=False)
    team        = models.ForeignKey("team", on_delete=models.CASCADE, blank=False)
    alliance    = models.CharField('Alliance Color', max_length=1, choices=ALLIANCES, default="R")
    score       = models.IntegerField('Match Score', default=0)
    rp          = models.IntegerField('Ranking Points', default=0)

    defenseA    = models.CharField(max_length=2, choices=DEFENSE_A, default="P")
    defenseB    = models.CharField(max_length=2, choices=DEFENSE_B, default="M")
    defenseC    = models.CharField(max_length=2, choices=DEFENSE_C, default="D")
    defenseD    = models.CharField(max_length=2, choices=DEFENSE_D, default="RW")

    defenseACross   = models.IntegerField('Defense A Crosses', default=0)
    defenseBCross   = models.IntegerField('Defense B Crosses', default=0)
    defenseCCross   = models.IntegerField('Defense C Crosses', default=0)
    defenseDCross   = models.IntegerField('Defense D Crosses', default=0)
    lowBarCross     = models.IntegerField('Low Bar Crosses', default=0)

    batterShot      = models.IntegerField(default=0)
    courtyardShot   = models.IntegerField(default=0)
    defenseShot     = models.IntegerField(default=0)

    class Meta:
        db_table = 'matches'
