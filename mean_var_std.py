import numpy as np

def calculate(my_list):
    try:
        if not isinstance(my_list, list) or len(my_list) !=9:
            raise ValueError("List must contain nine numbers.")
    # except ValueError:
    #     print("List must contain nine numbers.")
    #     return None
    finally:
        pass

    my_list = np.array(my_list).reshape((3,3))
    
    calculations = {}
    key = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
    
    def stat_calculator(func, name):
        def calculator():
            results=[]
            results.append((func(my_list, axis=0)).tolist())
            results.append((func(my_list, axis=1)).tolist())
            results.append((func(my_list)).tolist())
            return results
        calculations[name] = calculator()

    stat_calculator(np.mean, key[0])
    stat_calculator(np.var, key[1])
    stat_calculator(np.std, key[2])
    stat_calculator(np.max, key[3])
    stat_calculator(np.min, key[4])
    stat_calculator(np.sum, key[5])

    
    
    return calculations


