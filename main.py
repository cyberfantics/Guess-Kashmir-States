import turtle
import pandas
import zipfile
screen = turtle.Screen()
screen.title("State guessing game ")

image = "./Kashmir_states.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("2_states.csv")
all_state = data.state.to_list()
all_states = []

while len(all_states) < 10:
    answer = screen.textinput(
        title=f"{len(all_states)}/10: Guess the district ", prompt="Guess another ").title()
    if answer == 'Exit':
        missing_state = []
        for state in all_state:
            if answer not in all_states:
                missing_state.append(state)
            new_data = pandas.DataFrame(missing_state)
            new_data.to_csv("Missing_district.csv")
        break

    elif answer in all_state:
        all_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        district_data = data[answer == data.state]
        t.goto(int(district_data.x), int(district_data.y))
        t.write(answer)


# def mouse(x, y):
#      print(x, y)
# turtle.onscreenclick(mouse)
# turtle.mainloop()
# screen.exitonclick()
