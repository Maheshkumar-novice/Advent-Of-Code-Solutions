from collections import defaultdict, deque

with open('input.txt', 'r') as f:
    modules, dest_source_map = defaultdict(dict), {}

    for line in f:
        module, destinations = line.strip().split(' -> ')

        match module[0]:
            case '%':
                name = module[1:]
                type = 'flip-flop'
                destinations = destinations.split(', ')
                meta = {'state': 0}
            case '&':
                name = module[1:]
                type = 'conjunction'
                destinations = destinations.split(', ')
                meta = {'state': defaultdict(int)}
            case _:
                name = module
                type = module
                destinations = destinations.split(', ')
                meta = {'state': None}
            
        modules[name] = {'type': type, 'destinations': destinations, 'meta': meta}

    for module_name in modules:
        info = modules[module_name]
        if info['type'] in ('conjunction', 'flip-flop'):
            for dest in info['destinations']:
                # Mitigate dictionary change error. `rx` not in modules
                if dest in modules and modules[dest]:
                    if modules[dest]['type'] == 'conjunction':
                        modules[dest]['meta']['state'][module_name] = 0
    
    low_count, high_count, queue = 0, 0, deque()
    for _ in range(1000):
        queue.append((0, 'broadcaster', 'button'))
        
        while queue:
            signal, module_name, signal_from = queue.popleft()

            if signal == 1:
                high_count += 1
            else:
                low_count += 1

            module = modules[module_name]

            if not module:
                continue

            destinations = module['destinations']
            state = module['meta']['state']

            match module['type']:
                case 'broadcaster':
                    for dest in destinations:
                        queue.append((0, dest, module_name))
                case 'flip-flop':
                    if signal == 0:
                        state = 1 if state == 0 else 0

                        for dest in module['destinations']:
                            queue.append((state, dest, module_name))

                        module['meta']['state'] = state
                case 'conjunction':
                    state[signal_from] = signal

                    signal = 0 if all(i == 1 for i in state.values()) else 1

                    module['meta']['state'] = state
        
                    for dest in destinations:
                        queue.append((signal, dest, module_name))

    print(low_count * high_count)