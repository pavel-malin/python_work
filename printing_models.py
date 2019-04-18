# List of models that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# The loop sequentially prints each model to the end of the list.
# After printing, each model is moved to yr list complered_models.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Printing a model on a 3D-printer.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# The withdrawal of all finished models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

def print_models(unprinted_designs, completed_models):
    '''
    Simulates the printing of models until the list is empty.
    Each model of the post print s moved to completed_models.
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Printing a model on a 3D-printer.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    '''Display information on all printed models.'''
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models) 