from dataclasses import fields
from rest_framework.serializers import ModelSerializer

from .models import Budget, Diary, Event, Meeting, Plan, Project, Quote, Todo;

#Todo serializer
class TodoSerializer(ModelSerializer):
    class Meta:
        fields='__all__';
        model=Todo;
        
#Diary
class DiarySerilaizer(ModelSerializer):
    class Meta:
        fields='__all__';
        model=Diary;
        
#Meeting
class MeetingSerializer(ModelSerializer):
    class Meta:
        fields='__all__';
        model=Meeting;
        
#journal
class EventSerializer(ModelSerializer):
    class Meta:
        fields='__all__';
        model=Event;
        
#Plans
class PlanSerializer(ModelSerializer):
    class Meta:
        fields='__all__';
        model=Plan;
        
#Projects
class ProjectSerializer(ModelSerializer):
    class Meta:
        fields='__all__';
        model=Project;
        
#Quotes
class QuoteSerializer(ModelSerializer):
    class Meta:
        fields='__all__';
        model=Quote;
    
# Budget
class BudgetSerializer(ModelSerializer):
    class Meta:
        fields='__all__';
        model=Budget;