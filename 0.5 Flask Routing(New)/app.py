from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return '''
    <html>
    <head>
        <title>Welcome</title>
    </head>
    <body>
        <h1>Welcome to the gallery</h1>
        <h2> here we have pics of food pets and space!! </h2>
        <br>
       <h3> <a href='/food1'> go to the first food photo </a></h3>
        <br>
       <h3> <a href='/pet2'> go pet a bear </a></h3>
        <br>
     <h3><a href='/space1'> spacee </a></h3>

    </body>
    </html>'''
@app.route("/space1")
def space1():
    return '''
       <html>
    <body>
        <img src='https://i0.wp.com/thelumberjack.org/wp-content/uploads/2019/04/black-hole.jpg?fit=1601%2C1175&ssl=1'>
               <br>
             <h3>  <a href='/space3'> flyyy!! </a> </h3>
               <br>
               <h3> <a href='/home'> go home </a></h3>
    </body>
    </html>
    '''

@app.route("/space2")
def space2():
    return '''
       <html>
    <body>
        <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGdJ8gx6sLyUQTfftGhzGz8nREDc43kQBAeg&s'>
              <h3> <a href='/space1'> go back </a></h3>
               <br>
              <h3> <a href='/space3'> flyyy!! </a> </h3>

    </body>
    </html>
    '''
@app.route("/space3")
def space3():
    return '''
       <html>
    <body>
        <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyL9aypgOluHxwS9Hv-ddu9iL2AI093tH9Cw&s'>
              <h3> <a href='/space1'> go back </a> </h3>
               <br>
              <h3> <a href='/space2'> yippiee </a> </h3>

    </body>
    </html>
    '''




@app.route("/pet2")
def pet2():
    return '''
       <html>
    <body>
        <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGKBIF91ijnCDgygFNPdWPmqU9ypVTFvEcUQ&s'>
              <h3> <a href='/pet1'> rawr </a> </h3>
               <br>
              <h3> <a href='/pet3'> rawrrr!! </a></h3>
               <br>
               <h3> <a href='/home'> go home </a> </h3>
    </body>
    </html>
    '''

@app.route("/pet1")
def pet1():
    return '''
       <html>
    <body>
        <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSx1HbpgopNZHrOaEGPHx4FKZIvlnD8RjgUIQ&s'>
        <br>
              <h3> <a href='/pet2'> moew </a> </h3>

    </body>
    </html>
    '''

@app.route("/pet3")
def pet3():
    return '''
       <html>
    <body>
        <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ30D3kcGzamody3DqXED0XMix44Tm_F1Uyug&s'>
             <h3>  <a href='/pet2'> moew </a> </h3>

    </body>
    </html>
    '''
    
@app.route("/food1")
def food1():
    return '''
       <html>
    <body>
        <img width="1000px"src="data:image/jpeg;base64,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">
               <a href='/food2'> go eat more </a>
    </body>
    </html>
    '''

@app.route("/food2")
def food2():
    return '''
     <html>
    <body>
       <h3>  <a href='/food3'> go eat more </a> </h3>
        <img width = "1000px" src="https://www.tripsavvy.com/thmb/2B5_4ks3SK2l_ehZj9ZY6pXJx9w=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/5033415296_4d025683af_o-5b953ba946e0fb00251ecdb5.jpg">      
    '''

@app.route("/food3")
def food3():
    return '''
     <html>
    <body>
      <h3>  <a href='/home'> go home </a> </h3>
        <img width = "1000px" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNbIX0KsvabL2V-X8S8z0W7ibZ3zQ6nahJKg&s">      
    '''


if __name__ == '__main__':
    app.run(debug=True)