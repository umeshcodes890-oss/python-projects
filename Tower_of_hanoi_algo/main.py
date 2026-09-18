def hanoi_solver(n: int) -> str:
    # Initialize the three rods
    # Rod 0 is the source, Rod 1 is the auxiliary, Rod 2 is the target
    rods = [list(range(n, 0, -1)), [], []]
    
    # List to store the string representation of each state
    states = []
    
    # Helper function to capture the current state of the rods
    def record_state():
        states.append(f"{rods[0]} {rods[1]} {rods[2]}")
    
    # Record the starting arrangement
    record_state()
    
    # Recursive function to solve the puzzle
    def move_disks(disks, source, target, auxiliary):
        if disks == 1:
            # Move the top disk from source rod to target rod
            disk = rods[source].pop()
            rods[target].append(disk)
            record_state()
            return
        
        # Step 1: Move n-1 disks from source to auxiliary using target
        move_disks(disks - 1, source, auxiliary, target)
        
        # Step 2: Move the remaining largest disk from source to target
        disk = rods[source].pop()
        rods[target].append(disk)
        record_state()
        
        # Step 3: Move the n-1 disks from auxiliary to target using source
        move_disks(disks - 1, auxiliary, target, source)

    # Start the recursion: move n disks from rod 0 to rod 2 using rod 1
    move_disks(n, 0, 2, 1)
    
    # Join all states into a single string separated by newlines
    return "\n".join(states)
