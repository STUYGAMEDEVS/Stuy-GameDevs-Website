#!/usr/bin/env python3
import cgi

print("Content-type: text/html\n")

form = cgi.FieldStorage()

answers = {
    'q1': 'Print',
    'q2': 'Instant',
    'q3': 'Bertie',
    'q4': 'User',
    'q5': 'List'
}
score = 0
for question, correct_answer in answers.items():
    if form.getvalue(question) == correct_answer:
        score += 1

response = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    
    <title>GameDevs - Quiz Results</title>
    
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
            left: 0;
            bottom: -33%;
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
        
        .footer {{
            width: 99.64%;
            border: 5px solid black;
            background-color: black;
            opacity: 0.5;
	        position: absolute;
        }}
    </style>
</head>
<body>
    <div class="square" style="left: 50%; transform: translateX(-50%); top: 21.7%; height: 40%;"></div>
    <div class="quiz-container">
        <h1 style="position: absolute; transform: translateX(-50%); left: 50%; top: 26%; font-size: 60px;">Results</h1>
        <div class="result" style="position: absolute; transform: translateX(-50%); left: 50%; top: 40%; font-size: 45px; font-family: 'Courier New', monospace; font-weight: bold;">
            You scored {score} out of {len(answers)}
        </div>
        <a href="http://homer.stuy.edu/~trahman60/HTML/test.html" type="submit" class="buuton" style="left: 35%;">Try Again</a>
        <a href="http://homer.stuy.edu/~trahman60/HTML/homepage.html" type="submit" class="buuton" style="left: 56%;">Back to Site</a>
    </div>
    
    <div class="footer" style="left: 50%; transform: translateX(-50%); top: 100%; height: 32%;"></div>
<p style="text-decoration: underline; font-family: Courier New; font-size: 25px; position: absolute; left: 31%; top: 100.5%; color: white; opacity: 0.7;">Contact Information</p>
<p style="font-size: 25px; font-family: Courier New; position: absolute; left: 26%; top: 105%; color: white; opacity: 0.7;">Email: stuyvesantgamedev@gmail.com</p>
<p style="font-size: 25px; font-family: Courier New; position: absolute; left: 29%; top: 109%; color: white; opacity: 0.7;">Number: +1 929 919 0588</p>
<p style="text-decoration: underline; font-family: Courier New; font-size: 25px; position: absolute; left: 35.5%; top: 113%; color: white; opacity: 0.7;">Address</p>
<p style="font-size: 25px; font-family: Courier New; position: absolute; left: 26%; top: 117.5%; color: white; opacity: 0.7;">345 Chambers St, New York, NY 10282</p>

<a href="http://homer.stuy.edu/~trahman60/HTML/homepage.html" style="text-decoration: underline; font-family: Courier New; font-size: 25px; position: absolute; left: 63%; top: 104%; color: white; opacity: 0.7;">Home</a>
<a href="http://homer.stuy.edu/~trahman60/HTML/resources.html" style="text-decoration: underline; font-family: Courier New; font-size: 25px; position: absolute; left: 61.2%; top: 108.5%; color: white; opacity: 0.7;">Resources</a>
<a href="http://homer.stuy.edu/~trahman60/HTML/games.html" style="text-decoration: underline; font-family: Courier New; font-size: 25px; position: absolute; left: 62.7%; top: 113%; color: white; opacity: 0.7;">Games</a>
<a href="http://homer.stuy.edu/~trahman60/HTML/team.html" style="text-decoration: underline; font-family: Courier New; font-size: 25px; position: absolute; left: 63%; top: 117.5%; color: white; opacity: 0.7;">Team</a>

<p style="font-family: Courier New; font-size: 20px; position: absolute; left: 50%; transform: translateX(-50%); top: 124%; color: white; opacity: 0.7;">Stuyright © 2024 Game Developers</p>
<p style="font-family: Courier New; font-size: 20px; position: absolute; left: 50%; transform: translateX(-50%); top: 127%; color: white; opacity: 0.7;">Created February 26th, 2024</p>

    
</body>
</html>
"""
print(response)
