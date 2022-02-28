from .serializers import BudgetSerializer, DiarySerilaizer, EventSerializer, MeetingSerializer, PlanSerializer, ProjectSerializer, QuoteSerializer, TodoSerializer
from .forms import budgetForm, diaryForm, eventForm, meetingForm, planForm, projectForm, quoteForm, todoForm
from .models import Budget, Diary, Event, Meeting, Plan, Project, Quote, Todo

# Provides tuples, lists and dicts for use in other files

# 1. MODEL, FORM, SERIALIZER dict/object
models_forms_serializers= {
    'meeting':[Meeting,meetingForm, MeetingSerializer], 
    'todo':[Todo, todoForm, TodoSerializer],
    'diary':[Diary, diaryForm, DiarySerilaizer],
    'budget':[Budget, budgetForm,BudgetSerializer],
    'event':[Event, eventForm, EventSerializer],
    'project':[Project, projectForm, ProjectSerializer],
    'quote':[Quote, quoteForm, QuoteSerializer],
    'plan':[Plan, planForm, PlanSerializer]
    }

# 2. Types of actions/lists
types = ['todo','meeting','diary','event','plan','project','quote','budget']
