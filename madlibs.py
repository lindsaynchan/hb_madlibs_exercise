from random import choice

from flask import Flask, render_template, request, redirect


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return redirect("/hello")


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Get the user's response to the yes or no question on the 'would you like to play a game?'"""

    wants_game = request.args.get("gamechoice")

    if wants_game == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")

@app.route('/madlib')
def show_madlib():
    """Fills in the template with the picked values."""

    person_choice = request.args.get("person")
    color_choice = request.args.get("color")
    noun_choice = request.args.get("noun")
    adjective_choices = request.args.getlist("adjective")

    return render_template("madlib.html",
                            person=person_choice,
                            color=color_choice,
                            noun=noun_choice,
                            adjectives=adjective_choices)
@app.route('/goodbye')
def say_goodbye():
    return render_template("goodbye.html")

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
