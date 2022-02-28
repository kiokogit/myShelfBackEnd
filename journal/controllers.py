from .constants import models_forms_serializers;

# find model, form and serializer using the type
def find_model_form_ser(type):
    for key in models_forms_serializers:
        if key==type:
            return models_forms_serializers[key]
    return None


def budgetLogic():
    model=find_model_form_ser('budget')[0]
    budget = model.objects.all();
    # total budget
    total = 0;
    # loop through budget items
    for item in budget:
        total = total +item.amount;
        
    return total;

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
# accepts type as a list of many types
def fetch_data(types):
    # initialize data as an empty dict
    data={};
    
    for type in types:
        propList = find_model_form_ser(type);
        model, serializer = propList[0], propList[2];
        # for each type, get data and serilaize, then add to the dictionary
        data_raw = model.objects.all();
        final_data = serializer(data_raw, many=True).data;
        data.__setitem__(type,final_data);
        
    return data
    