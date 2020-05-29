from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo,Organization, Team, AgileTeam, Employee

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

class OrganizationForm(forms.ModelForm):
    class Meta():
        model = Organization
        fields = ('orgname',)

class TeamForm(forms.ModelForm):
    class Meta():
        model = Team
        fields = ('teamName','org')


class AgileTeamForm(forms.ModelForm):
    class Meta():
        model = AgileTeam
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(render_value = True))
    class Meta:
        model = Employee
        fields = ('name', 'assoc_id', 'username', 'password', 'organization', 'team', 'agile_team',)
        labels = {
            'name':'Name',
            'assoc_id':'Associate ID',
            'username': 'Username',
            'password': 'Password',
            'organization':'Organization Name',
            'team': 'Team Name',
            'agile_team': 'Agile Team'
        }

        def __init__(self, *args, **kwargs):
            super(EmployeeForm,self).__init__(*args, **kwargs)
        # Code to make fields optional and to set the first option of dropdown as "Choose.."
            self.fields['organization'].required = False
            self.fields['organization'].empty_label = "Choose.."
            self.fields['team'].required = False
            self.fields['team'].empty_label = "Choose.."
            self.fields['agile_team'].required = False
            self.fields['agile_team'].empty_label = "Choose.."
