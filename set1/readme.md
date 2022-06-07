# TODO: Reflect on what you learned this week and what is still unclear.
## Lecture notes

## Class notes
* 20220602 15.15 I didn't realise at 22h that I had to click enter after every command
* 17.09 Managed to do print hello world!
Did a commit and the test is no good

## Sunday Arvo Trinket
* 20220605 16:25 Completed upload to personal computer
* Length of paths matter

### Trinket attempt 1
Turtle becomes a lowercase 'b'
Would help to understand how the turtle is orientated, an origin point and a grid? The pumpkin was kinda hit and miss with changing sizes and adding fangs
```
import turtle
import random

turtle.shape("turtle")
turtle.speed(2)
turtle.pendown()
turtle.right(90)
turtle.forward(100)
turtle.begin_fill()
turtle.circle(50)
turtle.circle('#%06x' % random.randint(0, 2**24 - 1))
turtle.end_fill()
```
https://hourofpython.trinket.io/from-blocks-to-code-with-trinket#/picture-time/jack-o-lantern 

## Readings
20220607 10:39 use git pull to sync computers with github information

### Maker's schedule, Manager's schedule - Paul Graham [^1].
```
Graham's mentality of 'Maker vs. Manager' doesn't address the importance of collaboration between the two parties. Whilst he states there is merit in both approaches, he is biased towards the maker's schedule. Dynamic workspaces with effective and empathetic leadership and both parties understanding the value of the other i.e. a change in mindset can be more effective (not necessarily a compromise).
``` 
### Simulating The World (In Emoji 😘) - Nicky Case [^2]

[^1]: Graham, P. (2009). Maker’s Schedule, Manager’s Schedule. http://paulgraham.com/makersschedule.html 

[^2]: Case, N. (2016). Simulating The World (In Emoji 😘). https://ncase.me/sim/ 