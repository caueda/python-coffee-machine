from turtle import Screen, Turtle
from hello import Hello

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Charmander"])
table.add_column("Pokemon Type", ["Electric", "Fire"])
table.align = "l"

print(table)