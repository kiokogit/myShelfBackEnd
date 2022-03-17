from .models import Budget;

# budget class
class BudgetChecks():
    model = Budget;
    
    def totals(entries, budget_total=0):
        for item in entries:
            budget_total =+ item.amount;
        return budget_total;

    def costs(model, cost_items=[], total_costs=0):
        for item in model:
            if item.cost > 0:
                cost_items.append(item);
                total_costs=+item.cost;
        return (total_costs, cost_items);
    
      