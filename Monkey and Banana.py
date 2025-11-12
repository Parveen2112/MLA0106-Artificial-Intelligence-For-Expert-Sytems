def monkey_banana():
    state = {'monkey': 'floor', 'banana': 'hanging', 'box': 'corner'}
    print("Initial State:", state)
    
    print("Monkey moves to box.")
    state['monkey'] = 'box'
    
    print("Monkey pushes box under banana.")
    state['box'] = 'under banana'
    
    print("Monkey climbs the box.")
    state['monkey'] = 'on box'
    
    print("Monkey grabs the banana.")
    state['banana'] = 'with monkey'
    
    print("Goal achieved:", state)

monkey_banana()
