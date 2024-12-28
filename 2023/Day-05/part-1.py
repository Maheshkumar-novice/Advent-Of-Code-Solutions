import re

class Parser():
    def __init__(self, data):
        self.state = 'seeds'
        self.next_states = {
            'seeds': 'seed-to-soil map',
            'seed-to-soil map': 'soil-to-fertilizer map',
            'soil-to-fertilizer map': 'fertilizer-to-water map',
            'fertilizer-to-water map': 'water-to-light map',
            'water-to-light map': 'light-to-temperature map',
            'light-to-temperature map': 'temperature-to-humidity map',
            'temperature-to-humidity map': 'humidity-to-location map'
        }

        self.data = data

        self.seeds = []
        self.soil = []
        self.fertilizer = []
        self.water = []
        self.light = []
        self.temperature = []
        self.humidity = []
        self.location = []

        self.seed_to_soil_map = {}
        self.soil_to_fertilizer_map = {}
        self.fertilizer_to_water_map = {}
        self.water_to_light_map = {}
        self.light_to_temperature_map = {}
        self.temperature_to_humidity_map = {}
        self.humidity_to_location_map = {}

    def move_state(self):
        self.state = self.next_states[self.state]

    def parse_location(self):
        for line in self.data:
            if line == '':
                self.move_state()

            self.current_data = list(map(int, re.findall(r'\d+', line)))
            if self.state == 'seeds':
                self.seeds = self.current_data
            elif self.state == 'seed-to-soil map':
                self._parse_to_map(self.seed_to_soil_map)
            elif self.state == 'soil-to-fertilizer map':
                self._parse_to_map(self.soil_to_fertilizer_map)
            elif self.state == 'fertilizer-to-water map':
                self._parse_to_map(self.fertilizer_to_water_map)
            elif self.state == 'water-to-light map':
                self._parse_to_map(self.water_to_light_map)
            elif self.state == 'light-to-temperature map':
                self._parse_to_map(self.light_to_temperature_map)
            elif self.state == 'temperature-to-humidity map':
                self._parse_to_map(self.temperature_to_humidity_map)
            elif self.state == 'humidity-to-location map':
                self._parse_to_map(self.humidity_to_location_map)

        self._process_map_data(self.seed_to_soil_map, self.seeds, self.soil) 
        self._process_map_data(self.soil_to_fertilizer_map, self.soil, self.fertilizer) 
        self._process_map_data(self.fertilizer_to_water_map, self.fertilizer, self.water) 
        self._process_map_data(self.water_to_light_map, self.water, self.light) 
        self._process_map_data(self.light_to_temperature_map, self.light, self.temperature) 
        self._process_map_data(self.temperature_to_humidity_map, self.temperature, self.humidity) 
        self._process_map_data(self.humidity_to_location_map, self.humidity, self.location) 

        print(min(self.location))

    def _parse_to_map(self, map):
        if not self.current_data: 
            return

        dest = self.current_data[0]
        source = self.current_data[1]
        incr = self.current_data[-1]

        map[(source, source + incr)] = dest

    def _process_map_data(self, map, source, destination):
        for i in source:
            flag = False
            for key in map.keys():
                if i >= key[0] and i <= key[1]:
                    flag = True
                    destination.append(abs(i - key[0]) + map[key])
            if not flag:
                destination.append(i) 


with open('input.txt', 'r') as f:
    Parser(f.read().splitlines()).parse_location()
