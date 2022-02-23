from .models import Budget

def budgetLogic():
    budget = Budget.objects.all();
    
    # total budget
    total = 0;
    # loop through budget items
    for item in budget:
        total = total +item.amount;
        
    return total;