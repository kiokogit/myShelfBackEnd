from django.shortcuts import render

from rest_framework.response import Response;
from rest_framework.decorators import api_view

from .models import Budget, Diary, Event, Meeting, Plan, Project, Quote, Todo
from .serializers import BudgetSerializer, DiarySerilaizer, EventSerializer, MeetingSerializer, PlanSerializer, ProjectSerializer, QuoteSerializer, TodoSerializer;
from .forms import budgetForm, diaryForm, eventForm, meetingForm, planForm, projectForm, quoteForm, todoForm

# Create your views here.
#GET AL TODOS
@api_view(['GET'])
def getEntries(request):
    todos = Todo.objects.all().order_by('-date_created');
    todoSer = TodoSerializer(todos, many=True);
    
    meetings = Meeting.objects.all().order_by('start_time');
    meetingsSer = MeetingSerializer(meetings, many=True);
    
    diary = Diary.objects.all().order_by('-date');
    diarySer = DiarySerilaizer(diary, many=True);
    
    events = Event.objects.all();
    eventsSer = EventSerializer(events, many=True);
    
    plans=Plan.objects.all();
    plansSer = PlanSerializer(plans, many=True);
    
    projects=Project.objects.all().order_by('deadline');
    projectsSer = ProjectSerializer(projects, many=True);
    
    quotes=Quote.objects.all().order_by('-date');
    quotesSer = QuoteSerializer(quotes, many=True);
    
    budget=Budget.objects.all().order_by('category');
    budgetSer = BudgetSerializer(budget, many=True);
    
    data = {
        'todos':todoSer.data, 
        'meetings':meetingsSer.data, 
        'diary':diarySer.data, 
        'events':eventsSer.data, 
        'plans':plansSer.data,
        'projects':projectsSer.data,
        'quotes':quotesSer.data,
        'budget':budgetSer.data,
        }
    
    return Response(data=data);

#create a journal entry, loop through the pk in the url
@api_view(['POST'])
def addEntry(request, type):
    data=request.data;
    if type=='todo':
        form=todoForm(data);
    elif type=='meeting':
        form=meetingForm(data);
    elif type=='event':
        form=eventForm(data);
    elif type=='diary':
        form=diaryForm(data);
    elif type=='plan':
        form=planForm(data);
    elif type=='project':
        form=projectForm(data);
    elif type=='quote':
        form=quoteForm(data);
    elif type=='budget':
        form=budgetForm(data);
    else:
        return Response(status=404);
    
    if form.is_valid():
        form.save(commit=True);
        
        return Response(status=201);
    else:
        print(form.errors.as_json());
        return Response(status=500);
    
#Edit a journal Entry
@api_view(['PATCH'])
def editEntry(request, type, id):
    data=request.data;
    if type=='todo':
        instance=Todo.objects.get(id=id)
        form=todoForm(data, instance=instance);
    elif type=='meeting':
        instance=Meeting.objects.get(id=id)
        form=meetingForm(data, instance=instance);
    elif type=='event':
        instance=Event.objects.get(id=id)
        form=eventForm(data, instance=instance);
    elif type=='diary':
        instance=Diary.objects.get(id=id)
        form=diaryForm(data, instance=instance);
    elif type=='plan':
        instance=Plan.objects.get(id=id)
        form=planForm(data, instance=instance);
    elif type=='project':
        instance=Project.objects.get(id=id)
        form=projectForm(data, instance=instance);
    elif type=='budget':
        instance=Budget.objects.get(id=id)
        form=budgetForm(data, instance=instance);
    else:
        return Response(status=404);
    
    if form.is_valid():
        form.save(commit=True);
        
        return Response(status=201);
    else:
        print(form.errors.as_json());
        return Response(status=500);
    
# delete from journal
@api_view(['DELETE'])
def delEntry(request, type, id):        #item id sent as pk, type of entry sent as body
    
    if type=='todo':
        task = Todo.objects.get(id=id);
    elif type=='meeting':
        task=Meeting.objects.get(id=id);
    elif type=='event':
        task=Event.objects.get(id=id);
    elif type=='plan':
        task=Plan.objects.get(id=id);
    elif type=='diary':
        task=Diary.objects.get(id=id);
    elif type=='project':
        task=Project.objects.get(id=id);
    elif type=='quote':
        task=Quote.objects.get(id=id);
    elif type=='budget':
        task=Budget.objects.get(id=id);
    else:
        return Response(status=500);
    
    task.delete();
    return Response(status=200);
