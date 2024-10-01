from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    m = request.args['ques1']
    b = request.args['sellist1']
    c = request.args['sellist2']
    if b=='Action' and c=='New':
        reply3="The Movie For You Is Borderlands, " +m +"!"
    if b=='Action' and c=='Old':
        reply3="The Movie For You Is Point Break, " +m +"!"
    if b=='Adventure' and c=='Old':
        reply3="The Movie For You Is Treasure Island, "+ m+"!"
    if b=='Adventure' and c=='New':
        reply3="The Movie For You Is The New Indiana Jones, "+ m+"!"
    if b=='Horror' and c=='Old':
        reply3="The Movie For You Is Alien, "+ m+"!"
    if b=='Horror' and c=='New':
        reply3="The Movie For You Is Alien, "+ m+"!"
    if b=='Sci-fi' and c=='Old':
        reply3="The Movie For You Is Alien, "+ m+"!"
    if b=='Sci-fi' and c=='New':
        reply3="The Movie For You Is Alien, "+ m+"!"    
    return render_template('response.html', response3=reply3)
    
if __name__=="__main__":
    app.run(debug=True)
