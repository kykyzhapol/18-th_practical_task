from solution import TrafficLight

seven_roads = TrafficLight()
print(seven_roads.current_signal)
for _ in range(5):
    seven_roads.next_signal()
print(seven_roads.current_signal)
