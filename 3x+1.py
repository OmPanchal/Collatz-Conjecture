from random import randint
from matplotlib.pyplot import plot

# Custom Range ------------------------------->

min = int(input("Min : \n" ))
max = int(input("Max : \n"))

# Basic Variables ---------------------------->

x = randint(min, max )
loops = 0

x_coordinates = []
y_coordinates = []

print(f"Random Number chosen: ===> {x}")


while True :
  
    # Even Detection ------------------------->

  if (x % 2) == 0:


    if loops == 0 :
      y_coordinates.append(x)
      x_coordinates.append(loops)

    print(f"Even: {int(x)}")

    x_coordinates.append(loops + 1)
    loops += 1

    x = x / 2
    y_coordinates.append(x)

    # To Prevent infinite Loop ---------------->

    if x == int(1) :
      print(f" <----- {len(y_coordinates)} Steps taken -----> ")
      plot(x_coordinates, y_coordinates)
      break
    
  # Odd Detection ----------------------------->

  if (x % 2) != 0:
     
    if loops == 0 :
      y_coordinates.append(x)
      x_coordinates.append(loops)

    print(f"Odd: {int(x)}")

    x_coordinates.append(loops + 1)
    loops += 1

    x = 3*x + 1 
    y_coordinates.append(x)

    # To Prevent infinite Loop------------------>

    if x == int(1) :
      print(f" <----- {len(y_coordinates)} Steps taken -----> ")
      plot(x_coordinates, y_coordinates)
      break