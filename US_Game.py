import turtle
import pandas

screen = turtle.Screen()
correct_answ = turtle.Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
FONT = ("Title ", 10, "bold")


# Get the coordinates on the screen for place the name of the States
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
count = 0
game_is_on = True
data = pandas.read_csv("50_states.csv")
correct_guess = []

while game_is_on:
    answer_state = screen.textinput(title=f"{count}/50 State Correct", prompt="What's another state's name?").title()
    for i in data.state:
        if answer_state == i:
            correct_guess.append(answer_state)
            count += 1
            coordinate = data[data.state == answer_state]
            correct_answ.hideturtle()
            correct_answ.penup()
            correct_answ.goto(int(coordinate.x), int(coordinate.y))
            correct_answ.write(answer_state, font=FONT)
    if count == 50:
        print("Congratulation")
        game_is_on = False
