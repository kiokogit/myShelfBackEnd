from django.forms import ModelForm

from .models import Budget, Diary, Event, Meeting, Plan, Project, Quote, Todo

#todo
class todoForm(ModelForm):
    class Meta:
        fields='__all__';
        model=Todo;
        
#meeting
class meetingForm(ModelForm):
    class Meta:
        fields='__all__';
        model=Meeting;
        
#event
class eventForm(ModelForm):
    class Meta:
        fields='__all__';
        model=Event;
        
#diary
class diaryForm(ModelForm):
    class Meta:
        fields='__all__';
        model=Diary;
        
#plan
class planForm(ModelForm):
    class Meta:
        fields='__all__';
        model=Plan;
        
#project
class projectForm(ModelForm):
    class Meta:
        fields='__all__';
        model=Project;
        
#quote
class quoteForm(ModelForm):
    class Meta:
        fields='__all__';
        model=Quote;
        
# Budget
class budgetForm(ModelForm):
    class Meta:
        fields='__all__';
        model=Budget;