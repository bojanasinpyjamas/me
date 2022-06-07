# TODO: Reflect on what you learned this week and what is still unclear.
## Lecture notes
![alt-text](..\set1\Pavlovic-B_LectureNotes.jpg)

### Notes from lecture
* Concepts - what makes programming work?
* Competency - Understanding where it is most appropriate 
* Culture - Done by/for people
* Foundational block
* Consumed by computers + people, needs to be comprehensive by both

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

### Maker's schedule, Manager's schedule - Paul Graham[^1]

Graham's mentality of 'Maker vs. Manager' doesn't address the importance of collaboration between the two parties. Whilst he states there is merit in both approaches, he is biased towards the maker's schedule. Dynamic workspaces with effective and empathetic leadership and both parties understanding the value of the other i.e. a change in mindset can be more effective (not necessarily a compromise).

### Simulating The World (In Emoji 😘) - Nicky Case[^2]

* Complex systems understanding and synthesising through simulations
* **Emergence** complex systems have simple rules
* Once these are established then you can prompt the system with 'what-if' statements.

A system needs a feedback loop
* reinforcing loop: more leads to more (more fire gets you more fire) making infinite growth
* balancing loop: more leads to less (more trees make more fires which makes less trees) 
```
Self-organisation allows a system to automatically adapt to new scenarios.
```
Which leads to predictions and assumptions can be made.
These loops can generate rules but not necessarily the correct one. In computational design, the data you put in is the information you will get churned out.

### Why Architects Can't Be Automated - Daniel Davis[^3]
In the 1960s, there was a big push for computation in the field of architecture, not so much in the visual design but efficiency. Failure as the study didn't factor in qualitative data. Quantitative data can inform architects and assist them. Once again, there is a interest in using computer to tackle design problems e.g. big data + cloud-based computing to analyse the walkability of cities

Davis's notion of 'don't worry, computers won't take our jobs' is a revered view on architecture and design. Art and engineering have embraced computers but design still seems strangely stunted to using it as a tool to inform and excel design.

### Architects getting automated - Ben Doherty[^4]
The main factors contributing to 'if a job can be automated' are:

* Social intelligence
* Creativity
* Perception and manipulation of real-world impacts

The romanticised part of being an architect/designer may not be automated right now but tedious tasks have (rendering, technical drawings, printing copies)

Automating tasks and technology opens up people to more opportunities and different, unexpected problems to solve.

### The digital computer as a creative medium[^5]


[^1]: Graham, P. (2009). Maker’s Schedule, Manager’s Schedule. http://paulgraham.com/makersschedule.html 

[^2]: Case, N. (2016). Simulating The World (In Emoji 😘). https://ncase.me/sim/ 

[^3]: Davis, D. (2015). Why Architects Can’t Be Automated. https://www.architectmagazine.com/technology/why-architects-cant-be-automated_o 

[^4]: Doherty, B. (2015). Architects getting automated? https://notionparallax.co.uk/2015/architects-getting-automated

[^5]: Noll, A. M. (1967). The digital computer as a creative medium. IEEE Spectrum, 4(10), 89–95.