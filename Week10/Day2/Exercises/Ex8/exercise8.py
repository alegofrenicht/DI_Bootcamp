# Exercise 8 : How Old Are You On Jupiter?
# Instructions
# Given an age in seconds, calculate how old someone would be on:
# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you are told someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.

import datetime


def age_planet(orbital_period):
    planets = {
                1: 'Earth',
                0.2408467: 'Mercury',
                0.61519726: 'Venus',
                1.8808158: 'Mars',
                11.862615: 'Jupiter',
                29.447498: 'Saturn',
                84.016846: 'Uranus',
                164.79132: 'Neptune'}

    if orbital_period not in planets:
        return 'Unknown data'

    user = datetime.datetime.strptime(input('please enter you birth date (format: day/month/year): '), '%d/%m/%Y')
    age_seconds = (datetime.datetime.now() - user).days * 86400 + (datetime.datetime.now() - user).seconds
    return f"Your age on {planets[orbital_period]} is {round(age_seconds / 31557600 * orbital_period, 2)} years"

print(age_planet(84.016846))
