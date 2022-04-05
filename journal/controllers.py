from .constants import models_forms_serializers, types as all_types;

# find model, form and serializer using the type
def find_model_form_ser(type):
    for key in models_forms_serializers:
        if key==type:
            return models_forms_serializers[key]
    return None

#delete data from the database
# Takes two args - a string type, and int id; 
def delete_entry(type, id):
    # find model using type; returns arr['model','form','serializer']
    model = find_model_form_ser(type)[0];
    if model != None:
        try:
            model.objects.get(id=id).delete()
            return True
        except:
            # model item not found
            return False
    else:
        return False
    
#editing
def new_or_edit_entry(type, data, id):
    props = find_model_form_ser(type);
    model, form = props[0], props[1];
    # if id is given, then it is to edit
    if id is not None:
        instance=model.objects.get(id=id);
        form = form(data, instance=instance);
    else:
        form = form(data);
    if form.is_valid():
        form.save(commit=True);
        return True;
    else:
        print(form.errors.as_json());
        return False;
    
# fetch data from database model
# accepts type as a string
def fetch_data(type, serialized=False, id=None, many=True):
    
    model = find_model_form_ser(type)[0];
    # for each type, get data and serilaize, then add to the dictionary
    raw_data = model.objects.all();
    if id is not None:
        raw_data=model.objects.get(id=id);
    if serialized:
        return serialize_data(type, raw_data=raw_data, many=many)
    else:
        return raw_data; 

# Get serialized data
def serialize_data(type, raw_data, many):
    serializer = find_model_form_ser(type)[2]
    final_data = serializer(raw_data, many=many).data;
    return final_data

# urgent meetings, data, etc
def urgents():
    data = {};
    
    types = ['meeting','event','project','todo']
    for type in types:
        entries=fetch_data(type, serialized=False);
        final_list= []
        for entry in entries: 
            # if entry has not passed:
            if not entry.has_passed:
                    # append serialized version of the entry
                ser_entry = fetch_data(type,serialized=True,id=entry.id, many=False);
                final_list.append(ser_entry)
        data.__setitem__(type,final_list)
   
    return data