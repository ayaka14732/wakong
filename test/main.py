from wakong import Wakong

wakong = Wakong(seed=42)

for _ in range(100):
    print(wakong(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']))
