from django.db import models

# Create your models here.
# ToDo
class Todo(models.Model):
    title=models.CharField(max_length=200);
    description=models.CharField(max_length=200, blank=True, null=True);
    date_created=models.DateTimeField(auto_now_add=True);
    deadline=models.DateTimeField(null=True, blank=True);
    done=models.BooleanField(default=False);
    date_done=models.DateTimeField(null=True, blank=True);
    
    class Meta:
        ordering=['-done','deadline', '-date_created']
    
    def __str__(self):
        return self.title;
    
# Diary
class Diary(models.Model):
    title=models.CharField(max_length=200);
    description=models.TextField(null=True, blank=True);
    date=models.DateField(auto_now_add=True);
    date_created=models.DateTimeField(auto_now=True);
    
    class Meta:
        ordering=['-date','-date_created']
    
    def __str__(self):
        return self.title;
    
# Meetings
class Meeting(models.Model):
    title=models.CharField(max_length=200);
    description=models.TextField(null=True, blank=True);
    venue=models.CharField(max_length=200);
    date=models.DateField(null=True, blank=True);
    start_time=models.TimeField(null=True, blank=True);
    end_time=models.TimeField(null=True, blank=True);
    agenda=models.TextField(null=True, blank=True);
    called_by=models.CharField(max_length=200);
    available=models.BooleanField(default=False);
    requirements=models.TextField(null=True, blank=True);
    my_contribution=models.TextField(null=True, blank=True);
    
    class Meta:
        ordering=['date','start_time']
    
    def __str__(self):
        return self.title;

# Events
class Event(models.Model):
    title=models.CharField(max_length=200);
    description=models.TextField(null=True, blank=True);
    venue=models.CharField(max_length=200);
    date=models.DateTimeField(null=True, blank=True);
    available=models.BooleanField(default=True);
    
    class Meta:
        ordering=['date']
    
    def __str__(self):
        return self.title;
    
# Plans
class Plan(models.Model):
    title=models.CharField(max_length=200);
    description=models.TextField(null=True, blank=True);
    deadline=models.DateTimeField(null=True, blank=True);
    
    class Meta:
        ordering=['deadline']
    
    def __str__(self):
        return self.title;

# Projects
class Project(models.Model):
    title=models.CharField(max_length=200);
    description=models.TextField(null=True, blank=True);
    progress=models.TextField(null=True, blank=True)
    deadline=models.DateField(null=True, blank=True);
    start_date=models.DateTimeField(null=True, blank=True);
    created=models.DateTimeField(auto_now_add=True);
    updated=models.DateTimeField(auto_now=True);
    end_date=models.DateField(null=True, blank=True);
    closed=models.BooleanField(default=False);
    open=models.BooleanField(default=False);
    
    class Meta:
        ordering=['open','deadline','updated']
    
    def __str__(self):
        return self.title; 
    
# Quotes
class Quote(models.Model):
    source=models.CharField(max_length=200, default='Anonymous');
    quote=models.TextField();
    date=models.DateTimeField(auto_now_add=True);
    
    class Meta:
        ordering=['-date', 'source']
    
    def __str__(self):
        return self.quote;

# Budget
class Budget(models.Model):
    category=models.CharField(max_length=200);
    item=models.CharField(max_length=200);
    amount=models.IntegerField(null=True, blank=True);
    
    class Meta:
        ordering=['amount']
    
    def __str__(self):
        return self.item