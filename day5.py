data = open('day5.txt', 'r').read().split('\n')

seed_soil = []
soil_fertilizer = []
fertilizer_water = []
water_light = []
light_temperature = []
temperature_humidity = []
humidity_location = []

pointer = seed_soil
for line in data:
    line_input = line.split(" ")
    if len(line_input) == 2:
        input = line_input[0]
        if input == "seed-to-soil":
            pointer = seed_soil
        elif input == "soil-to-fertilizer":
            pointer = soil_fertilizer
        elif input == "fertilizer-to-water":
            pointer = fertilizer_water
        elif input == "water-to-light":
            pointer = water_light
        elif input == "light-to-temperature":
            pointer = light_temperature
        elif input == "temperature-to-humidity":
            pointer = temperature_humidity
        else:
            pointer = humidity_location

    if len(line_input) == 3: # input
        pointer.append(line_input)

unrefined_seed = data[0].split(" ")
refined_seed = []
for i in range(1, len(unrefined_seed)):
    refined_seed.append(int(unrefined_seed[i]))

print(light_temperature)

def solve(seed):
    execution_order = [seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location]
    current_value = seed
    print(f"Starting solving on {current_value}")
    
    for order in execution_order:
        for source, destination, r in order:
            if current_value >= int(destination) and current_value <= int(destination) + int(r) - 1:
                print(f"Found maching on {source}, {destination}, {r}")
                current_value = int(source) + (current_value - int(destination))
                break
        print("Current value {current_value}")

    print(f"Done with result {current_value}")
    return current_value

mn = float('inf')
for s in refined_seed:
    mn = min(mn, solve(s))

print(mn)

