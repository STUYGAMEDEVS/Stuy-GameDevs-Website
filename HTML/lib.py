#!/usr/bin/env python3
import http.server
import socketserver
import cgi
import os

PORT = 8000
DATA_FILE = 'data.csv'

print("Content-type: text/html\n")

form = cgi.FieldStorage()


test_file = open('data.csv', 'a')
text = test_file.read()
lisp = []


lisp = (text.split('\n'))
print(lisp)

lisp = lisp[1:]
test_file.close()

#print(lisp)



#for question, correct_answer in answers.items():
#    if form.getvalue(question) == correct_answer:
 #       score += 1

response = f"""
<!DOCTYPE html>
<html lang="en">
<head>

    <title>GameDevs - Survey Complete</title>
    <video autoplay muted loop id="myVideo">
      <source src="stars.mp4" type="video/mp4">
    </video>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dropdown Quiz</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
        }}
        #myVideo {{
            position: absolute;
            right: 0;
            bottom: 0;
            left: 0;
            bottom: 0;
            min-width: 100%; 
            min-height: 100%;
            object-fit: fill;
            z-index: -10;
        }}
        
        .square {{
            opacity: 0.9;
            width: 50%;
            border: 10px solid black;
            position: absolute;
            background-color: silver;
            border: 8px solid #ccc;
            border-radius: 20px;
            position: absolute; 
            left: 40%; 
            transform: translateX(-50%);
        }}
        .result {{
            margin-top: 20px;
        }}
        .quiz-container {{
            font-size: 30px;
        }}
        .buuton {{

            background-color: #C0C0C0;
            color: black;
            text-align: center;
            text-decoration: none;
            font-size: 26px;
            border: 2px solid #71797E;
            cursor: pointer;  
            padding: 8px 24px;
            position: absolute; 
            top: 53%;
            font-family: 'Courier New', monospace;
            font-weight: bold;
        }}
        .buuton:hover {{
            box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
            background-color: #808080;
        }}
    </style>
</head>
<body>
    <div class="square" style="left: 50%; transform: translateX(-50%); top: 21.7%; height: 40%;"></div>
    <div class="quiz-container">
        <h1 style="position: absolute; transform: translateX(-50%); left: 50%; top: 26%; font-size: 60px;">Thank You!</h1>
        <div class="result" style="position: absolute; transform: translateX(-50%); left: 50%; top: 40%; font-size: 45px; font-family: 'Courier New', monospace; font-weight: bold;">
        </div>
        <a href="http://homer.stuy.edu/~trahman60/HTML/test.html" type="submit" class="buuton" style="left: 35%;">View Data</a>
        <a href="http://homer.stuy.edu/~trahman60/HTML/homepage.html" type="submit" class="buuton" style="left: 56%;">Back to Site</a>
    </div>
</body>
</html>
"""

#text.write("\n")
#text.write(3)
text.write('\n,"')
for i in range(len(languages)):
    if i == 0:
        text.write(languages[i])
    else:
        text.write(', ')
        text.write(languages[i])
text.write('"')
text.close()
htmlTail()

