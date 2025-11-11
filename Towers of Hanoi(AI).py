def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n-1, auxiliary, source, target)

# Example with 3 disks
print("Towers of Hanoi Solution:")
hanoi(3, 'A', 'B', 'C')
