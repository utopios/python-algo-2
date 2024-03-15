from functools import reduce
# def calculer(*args, **kwargs):
#     operation = kwargs.get('operation', 'somme')
#     if operation == 'somme':
#         return sum(args)
#     elif operation == 'moyenne':
#         return sum(args) / len(args) if args else 0
#     elif operation == 'produit':
#         return reduce(lambda x, y: x * y, args, 1)
    

def calculer(*args, **kwargs):
    operation = kwargs.get('operation')
    # if operation == 'somme':
    #     return sum(args)
    # elif operation == 'moyenne':
    #     return sum(args) / len(args) if args else 0
    # elif operation == 'produit':
    #     return reduce(lambda x, y: x * y, args, 1)

    return operation(args)

# Test
print(calculer(1, 2, 3, 4, operation= lambda args: sum(args) / len(args) if args else 0))

print(calculer(1, 2, 3, 4, operation= lambda args: sum(args)))
