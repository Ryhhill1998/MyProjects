import turtle
import pandas as pd

ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")
END_FONT = ("Arial", 40, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

states_df = pd.read_csv("50_states.csv")
states = states_df.state
states_list = states.to_list()

states_guessed = []
states_not_guessed = states_list
lives = 5

while len(states_guessed) < 50 and lives > 0:

    answer_state = screen.textinput(title=f"{len(states_guessed)}/50 States Correct, Lives: {lives}",
                                    prompt="Enter the name of a state: ").title()

    guess_correct = answer_state in states_list

    missing_states = [state for state in all_states if state not in guessed_states]

    if guess_correct:
        state_info = states_df[states_df.state == answer_state]
        x_position = int(state_info.x)
        y_position = int(state_info.y)
        pen.goto(x_position, y_position)
        pen.write(answer_state, align=ALIGNMENT, font=FONT)
        states_guessed.append(answer_state)
        states_not_guessed.remove(answer_state)
        if len(states_guessed) == 50:
            pen.goto(0, 0)
            pen.write("AMAZING!\nYOU GUESSED ALL 50 STATES!", align=ALIGNMENT, font=END_FONT)
            end_game = screen.textinput(title="End of Game", prompt="Enter Y to end game: ").upper()
            if end_game == "Y":
                break
            else:
                end_game = screen.textinput(title="End of Game", prompt="Enter Y to end game: ").upper()

    else:
        lives -= 1
        if lives == 0:
            pen.goto(0, 270)
            pen.write("GAME OVER", align=ALIGNMENT, font=END_FONT)

            for state in states_not_guessed:
                state_info = states_df[states_df.state == state]
                x_position = int(state_info.x)
                y_position = int(state_info.y)
                pen.goto(x_position, y_position)
                pen.color("red")
                pen.write(state, align=ALIGNMENT, font=FONT)

            end_game = screen.textinput(title="End of Game", prompt="Enter Y to end game: ").upper()
            if end_game == "Y":
                break
            else:
                end_game = screen.textinput(title="End of Game", prompt="Enter Y to end game: ").upper()
