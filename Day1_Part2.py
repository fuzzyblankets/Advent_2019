"""
During the second Go / No Go poll, the Elf in charge of the Rocket Equation Double-Checker
stops the launch sequence. Apparently, you forgot to include additional fuel for the fuel
you just added.

Fuel itself requires fuel just like a module - take its mass, divide by three, round down,
and subtract 2. However, that fuel also requires fuel, and that fuel requires fuel, and so
on. Any mass that would require negative fuel should instead be treated as if it requires
zero fuel; the remaining mass, if any, is instead handled by wishing really hard, which has
no mass and is outside the scope of this calculation.
"""

import math

# Numbers provided by website
mass_mods = [78390,73325,52095,126992,106546,81891,69484,131138,95103,53296,115594,79485,130202,95238,99332,136331,124321,127271,108047,69186,90597,96001,138773,55284,127936,110780,89949,85360,55470,110124,101201,139745,148170,149108,79579,139733,52014,125910,77323,145751,52161,105606,132240,69907,144129,116958,60818,144964,111789,85657,115509,84509,50702,69012,110376,134213,127319,92966,58422,144491,128198,84367,94269,147895,105494,88369,117882,146239,50704,62591,149258,63118,145393,122997,136534,96402,121057,59561,86916,75873,68670,147465,62902,145858,137810,108108,97314,118001,54699,56603,66821,80744,124514,143113,132581,79376,105728,115337,111028,52209]
total_fuel = 0

for i in mass_mods:
    fuel = math.floor(i/3)-2
    mod_fuel = fuel
    while (math.floor(fuel/3)-2) > 0:
        fuel = math.floor(fuel / 3) - 2
        mod_fuel += fuel
    total_fuel+=mod_fuel

print(total_fuel)
