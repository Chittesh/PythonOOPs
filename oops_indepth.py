class planet:
    pass

earth=planet()
mars=planet()

earth.name = "Earth"
earth.speed = "2000"

print(earth.name)       #Earth
print(earth.speed)      #2000

print(mars.name)        # Error : AttributeError: 'planet' object has no attribute 'name'