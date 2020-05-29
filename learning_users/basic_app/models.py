from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)


    #addition by SIVA

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic',blank=True)


    def __str__(self):
        return self.user.username


class Organization(models.Model):
    orgname = models.CharField(max_length = 100, blank=True)

    def __str__(self):
        return str(self.orgname)

class Team(models.Model):
    teamID = models.AutoField(primary_key=True)
    teamName = models.CharField(max_length = 100, blank=True)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.teamName)

class AgileTeam(models.Model):
    agileTeamID = models.AutoField(primary_key=True)
    agileTeamName = models.CharField(max_length = 100, blank=True)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    team = models.ForeignKey(Team,  on_delete=models.CASCADE)

    def __str__(self):
        return str(self.agileTeamName)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    assoc_id = models.CharField(max_length=10)
    username = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    agile_team = models.ForeignKey(AgileTeam, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
