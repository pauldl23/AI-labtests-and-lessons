import time

for i in range(3, -1, -1):
    print(f"\rCountdown timer: {i} ", end="")
    time.sleep(1)

print()

for x in range(0, 101, 20):
    progress = "█" * (x // 5)
    empty = " " * ((100 - x) // 5)
    print(f"\rLoading |{progress}{empty}| {x:3} of 100", end="")
    time.sleep(0.8)

print("\nDone!")
