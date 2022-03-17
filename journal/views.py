from rest_framework.response import Response;
from rest_framework.decorators import api_view;

from .controllers import delete_entry, fetch_data, new_or_edit_entry;
# from .constants import types;

# Create your views here.
#GET ALL lists
@api_view(['GET'])
def getEntries(request, type):
    data = fetch_data(type)
    return Response(data=data);

#create a journal entry, loop through the 'type' param in the url
@api_view(['POST'])
def addEntry(request, type):
    data=request.data;
    
    if new_or_edit_entry(type, data, None):
        return Response(status=201);
    else:
        return Response(status=500);
    
#Edit a journal Entry
@api_view(['PATCH'])
def editEntry(request, type, id):
    data=request.data;
    
    if new_or_edit_entry(type,data, id):
        return Response(status=201);
    else:
        return Response(status=500);
    
# delete from journal
@api_view(['DELETE'])
def delEntry(request, type, id):
    # forbid deleting diary entries
    if type=='diary':
        # not allowed
        return Response(status=403);
    # pass all to the logic    
    if delete_entry(type,id):
        return Response(status=200);
    else:
        return Response(status=404)
