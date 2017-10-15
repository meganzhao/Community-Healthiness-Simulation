# Community Healthiness Simulation
Our program is a simulation of disease spread within a community that consists of 5000 members with 50 members in each age group from 0 to 99.
We define children as 0 to 18, adults as 19 to 60, and elderly as 61 to 99. 
The user is asked to input how many days they would like to simulate. 
Before the first day of the simulation, one random community member is chosen as the first sick person. 
Each day, a random number of children go to school, a random number of adults go to the office, and a random number of community members go to the shop. 
Thus, a child could go both to school and the shop, an adult could go both to the office and to the shop, and any sick person could go to the hospital as well as other places. 
At these places, if there is at least one sick person present, every healthy person has a chance of getting sick. 
At the beginning of the simulation, the user decides whether each place will have a high or low probability of making the community members sick - for example, high probability gives the elderly a 75% chance of becoming sick, while low probability gives them only a 50% chance of becoming sick. 
Probability is different for each age group - older community members have a greater chance of getting sick than younger community members. Then, a random number of sick community members are sent to the hospital, where each sick person has a chance of becoming healthy. 
Again, at the beginning of the simulation, the user decides whether the hospital has a high or low probability of having its patients recover. Probability is again based on age - older community members have less chance of recovering as compared to younger community members. 
After all of these functions are run, the user clicks and a new day is simulated. 
After the number of days that the user chose is simulated, the window closes and a final screen displays the numbers of sick and healthy children, adults, and elderly people.

## How To Run
```
# Clone this repository
$ git clone https://github.com/meganzhao/Community-Healthiness-Simulation.git

# Go into the repository
$ cd Community-Healthiness-Simulation

# Run the simulation
$ python3 community.py
```

## Game Demo

![Alt text](img-demo/img1.png?raw=true "Title")
![Alt text](img-demo/img2.png?raw=true "Title")
![Alt text](img-demo/img3.png?raw=true "Title")

## Authors
* Anne Hackman
* Megan Zhao

