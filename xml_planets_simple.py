import lxml.etree as et

# ElementTree 
doc = et.parse('DATA/solar.xml')

for planet in doc.findall('.//planet'):
    planet_name = planet.get('planetname')
    print(planet_name)
    for moon in planet.findall('moon'):
        print(f"    {moon.text}")