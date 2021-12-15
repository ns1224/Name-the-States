from turtle import Screen, Turtle
import pandas as pd

screen = Screen()
screen.setup(width=700, height=500)
screen.title('US STATES GUESSING GAME')
screen.bgpic('us-states-game-start/united-states.gif')

df_states = pd.read_csv('us-states-game-start/50_states.csv')

# States list
states = df_states['state'].to_list()

# States pen
t = Turtle(shape='circle')
t.hideturtle()
t.penup()

guessed_states = []
while len(guessed_states) < 50:

    player_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed", prompt="Name a state: ").strip(' ').title()

    valid_answer = True
    if player_answer in guessed_states:
        valid_answer = False

    if valid_answer and player_answer in states:

        state_info = df_states[df_states['state'] == player_answer]
        x, y = int(state_info.x), int(state_info.y)

        t.goto((x, y))
        t.write(player_answer)

        guessed_states.append(player_answer)

    elif player_answer == "Exit":

        # Write Missed States to new file called Missed_states.csv
        missed_states = [state for state in states if state not in guessed_states]

        df_missed = pd.DataFrame(missed_states)
        df_missed.to_csv('States-to-learn.csv')

        break

    if len(guessed_states) == 50:
        t.goto(0, 0)
        t.write("You got all 50 States correctly!", align='CENTER', font=("Courier", 24, "normal"))

screen.mainloop()
