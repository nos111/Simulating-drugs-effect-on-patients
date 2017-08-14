<h1>Simulating drugs effect on viruses</h1>
In this write up, I will summarize the results of my simulation of viruses population growth in a patient. The simulation starts without drug treatment to observe the growth of the virus population and moves on to simulating drug treatment effect on the virus population along with the effect of delayed treatment.  


The simulation consist of a patient class and a virus class.
100 Viruses are injected into the patient body.


The growth of the virus population is simulated using:
1- The possibility of the immunity system of the patient clearing the virus unit
2- The possibility of a mutation in the virus form to appear, making it resistant to treatment
3- The max population of the virus due to limitation of resources.


In all experiments, the virus was initiated without any resistance to drugs. Yet, the resistance was present after an amount of simulation due to possibility of mutation.


<h2>Running and Analyzing a Simple Simulation (No Drug Treatments):</h2>
From my observation of the viruses population, in an environment without drug treatment, and after injecting 100 viruses into the patient body, I have noticed that the virus population will reach its max after (150-200) steps of simulation. In each step the immunity system effect and the reproduction for all viruses were calculated. After 250 steps the population tends to range between (500-600) viruses.


 <img src="https://github.com/nos111/MIT-OCW/blob/master/Introduction%20to%20Computer%20Science%20(fall%202008)/assignment12/Graphs/problem2.png?raw=true"> 


<h2>Running and Analyzing a Simulation with a Drug:</h2>
The simulation was started with injecting 100 Viruses into the body of a patient. None of the viruses were resistant to the drugs. With a mutation probability of 0.005, the virus started showing drug resistant forms after 25 steps of simulation. The resistant population was very small (less than 10 viruses) until the drug was injected. I have observed a huge increase in the drug resistant population since the injection of the drug. Within 50 steps, after the injection, the non resistant population was down to less than 100 viruses (was around 500) and the drug resistant population started growing repetitively. There was more than 100 drug resistant viruses within 75 steps. Within 150 steps, the drug resistant population has grown to reach a number around 500.


<img src="https://github.com/nos111/MIT-OCW/blob/master/Introduction%20to%20Computer%20Science%20(fall%202008)/assignment12/Graphs/problem4.png?raw=true">

<h2>The Effect of Delaying Treatment on Patient Outcome:</h2>
In this simulation, I have explored the effect of delaying treatment on the ability of the drug to eradicate the virus population. I have ranwill  multiple simulations to observe trends in the distributions of patient outcomes. The simulation was run for 300, 150, 75, and 0 time steps before administering guttagonol to the patient. Then it ran the simulation for an additional 150 time steps.
I have observed the following:


1- when the patient is given the treatment immediately after the infection with the virus, 99% of the patients were cured. 150 steps following the injection with the drugs to make sure there is not growth of the virus after healing.
 
<img src="https://github.com/nos111/MIT-OCW/blob/master/Introduction%20to%20Computer%20Science%20(fall%202008)/assignment12/Graphs/problem5With0Steps.png?raw=true">

2- When the treatment is delayed 75 time steps before injection, the percentage of cured patients has dropped down to 10%.


<img src="https://github.com/nos111/MIT-OCW/blob/master/Introduction%20to%20Computer%20Science%20(fall%202008)/assignment12/Graphs/problem5With75Steps.png?raw=true">



3- When the treatment is delayed 150 steps, the percentage of cured patients drops down to 5%

<img src="https://github.com/nos111/MIT-OCW/blob/master/Introduction%20to%20Computer%20Science%20(fall%202008)/assignment12/Graphs/problem5With150Steps.png?raw=true">



4-  When the treatment is delayed 300 steps, the percentage of cured patients drops down to 1%

<img src="https://github.com/nos111/MIT-OCW/blob/master/Introduction%20to%20Computer%20Science%20(fall%202008)/assignment12/Graphs/problem5With300Steps1.png?raw=true">

From those 4 observations we notice that the percentage of cured patients drops dramatically when the treatment is delayed. However, once the delay has reached 75 steps, further steps has little effects.
The first 75 steps are the most important in the virus life cycle to eliminate immediately. 


<h2>Designing a Treatment Plan with Two Drugs:</h2>
One approach to addressing the problem of acquired drug resistance is to use cocktails - administration of multiple drugs that act independently to attack the virus population. In the following simulations,I have used two independently-acting drugs to treat the virus. I have used this model to decide the best way of administering the two drugs. Specifically, I have examined the effect of a lag time between administering the first and second drugs on patient outcomes. 


In the case of administering the two drugs together after 150 steps of simulations of the virus life, 86% of the patients were cured:
<img src="https://github.com/nos111/MIT-OCW/blob/master/Introduction%20to%20Computer%20Science%20(fall%202008)/assignment12/Graphs/problem6With0Steps.png?raw=true">

With a delay of 75 steps between the two drugs, the percentage of healed patients has dropped down to 51%

<img src="https://github.com/nos111/MIT-OCW/blob/master/Introduction%20to%20Computer%20Science%20(fall%202008)/assignment12/Graphs/problem6With75Steps.png?raw=true">

If the delay between the two drugs become 150 steps, the percentage of cured patients drops down dramatically to 9%
<img src="https://github.com/nos111/MIT-OCW/blob/master/Introduction%20to%20Computer%20Science%20(fall%202008)/assignment12/Graphs/problem6With150Steps.png?raw=true">

I have also simulated a delay of 300 time steps between the administering of drugs. The percentage of cured patients dropped down to 4%

<img src="https://github.com/nos111/MIT-OCW/blob/master/Introduction%20to%20Computer%20Science%20(fall%202008)/assignment12/Graphs/problem6With300Steps1.png?raw=true">

From my observation, I can say that the delay between the drugs, once beyond 75 steps, will start having little or no effect on the patients results. 
A second drug is most effective with less than 75 steps in between.


<h2>Analysis of Virus Population Dynamics With Two Drugs:</h2>
To better understand the relationship between patient outcome and the time between administering the drugs, I have examined the virus population dynamics of two individual simulations in more detail. 
I have runa simulation for 150 time steps before administering guttagonol to the patient. Then ran the simulation for an additional 300 time steps before administering a second drug, grimpex, to the patient. Then ran the simulation for an additional 150 time steps.
I have used the same initialization parameters for Patient and Resistant Virus as I did for the previous experiment. 
Here you can see the results of it: 

<img src="https://github.com/nos111/MIT-OCW/blob/master/Introduction%20to%20Computer%20Science%20(fall%202008)/assignment12/Graphs/problem7With300Steps.png?raw=true">


I have also run a second simulation for 150 time steps before simultaneously administering guttagonol and grimpex to the patient. Then run the simulation for an additional 150 time steps. 
Here you can see the results:

<img src="https://github.com/nos111/MIT-OCW/blob/master/Introduction%20to%20Computer%20Science%20(fall%202008)/assignment12/Graphs/problem7With0Steps.png?raw=true">

The conclusion is that by administering the two drugs simultaneously we prevent drug resistance to arise among the virus population. When the virus is given the time between the two drugs, he will gain resistance which will make him harder to eliminate.