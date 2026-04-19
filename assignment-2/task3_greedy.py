class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(capacity, items):
    # Sort items based on value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_value = 0.0
    knapsack = []
    
    for item in items:
        if capacity == 0:
            break
            
        if item.weight <= capacity:
            # Take fully
            capacity -= item.weight
            total_value += item.value
            knapsack.append({'item': item, 'fraction': 1.0})
        else:
            # Take fraction
            fraction = capacity / item.weight
            total_value += item.value * fraction
            knapsack.append({'item': item, 'fraction': fraction})
            capacity = 0
            
    return total_value, knapsack

if __name__ == "__main__":
    print("Running Task 3: Greedy Algorithms (Fractional Knapsack)...")
    
    # Define items (value, weight)
    items = [Item(60, 10), Item(100, 20), Item(120, 30)]
    capacity = 50
    
    print(f"Knapsack Capacity: {capacity}")
    print("Available Items:")
    for i, item in enumerate(items):
        print(f"Item {i+1}: Value = {item.value}, Weight = {item.weight}, Ratio = {item.ratio:.2f}")
        
    optimal_value, selected_items = fractional_knapsack(capacity, items)
    
    print("\nSelected Items:")
    for i, sel in enumerate(selected_items):
        item = sel['item']
        fraction = sel['fraction']
        print(f"Used {fraction*100:.1f}% of Item with Value = {item.value}, Weight = {item.weight}")
        
    print(f"\nFinal Optimal Maximum Value: {optimal_value:.2f}")
    print("Task 3 complete!")
