import numpy
import random
import pylab
import matplotlib.pyplot as plt
import collections

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """    

#
# PROBLEM 1
#

class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = float(maxBirthProb)
        self.clearProb = float(clearProb)
        
    def doesClear(self):
        """
        Stochastically determines whether this virus is cleared from the
        patient's body at a time step. 

        returns: Using a random number generator (random.random()), this method
        returns True with probability self.clearProb and otherwise returns
        False.
        """
        if random.random() <= self.clearProb:
            return True
        else:
            return False
    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        if random.random() <= self.maxBirthProb * (1 - popDensity):
            #print 'virus has reproduced'
            return SimpleVirus( self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException()

class SimplePatient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """
    
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop

    def getTotalPop(self):
        """
        Gets the current total virus population. 

        returns: The total virus population (an integer)
        """
        return len(self.viruses)     

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
          of virus particles accordingly.

        - The current population density is calculated. This population density
          value is used until the next call to update() 

        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: the total virus population at the end of the update (an
        integer)
        """
        #print 'the old poplulation is', len(self.viruses)
        newViruses = []
        for virus in self.viruses:
            if virus.doesClear() == True:
                self.viruses.remove(virus)
        self.popDensity = float(self.getTotalPop()) / float(self.maxPop)
        for virus in self.viruses:
            try:
                newViruses.append(virus.reproduce(self.popDensity))
            except NoChildException:
                    continue
        self.viruses.extend(newViruses)
        #print 'the new poplulation is', len(self.viruses)
        return len(self.viruses)
            

#
# PROBLEM 2
#

def problem2():
    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    

    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """
    virusesList = []
    maxBirthProb = 0.1
    clearProb = 0.05
    for x in range(0, 100):
        virusesList.append(SimpleVirus(maxBirthProb , clearProb))
    patient = SimplePatient(virusesList, 1000)
    populationList = []
    for trial in range(0,300):
        populationList.append(patient.update())

    plt.plot(list(range(0, 300)), populationList)
    plt.title('Virus population VS Time')
    plt.xlabel('Time steps')
    plt.ylabel('virus population')
    plt.grid()
    plt.show()
    
#problem2()
    
#
# PROBLEM 3
#

class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """    
    
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.
        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        
        clearProb: Maximum clearance probability (a float between 0-1).
        
        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.        
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb
        
    def getResistance(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.        

        drug: the drug (a string).

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        try:
            return self.resistances[drug]
        except KeyError:
            return False
        
    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).                       
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         
        """
        #first check if the virus is resistance to all drugs
        for drug in activeDrugs:
            if self.getResistance(drug) == False:
                raise NoChildException()
        #reproduce with the probability
        if random.random() <= (self.maxBirthProb * (1 - popDensity)):
            
            resistanceInheritance = {}
            for drug in self.resistances:
                #check inheritance probabilties
                #active drugs list
                if random.random() <= self.mutProb:
                    resistanceInheritance[drug] = not self.getResistance(drug)
                else:
                    resistanceInheritance[drug] = self.getResistance(drug)
            #generate a new instance of the class
            return ResistantVirus(self.maxBirthProb,
                                  self.clearProb,
                                  resistanceInheritance,
                                  self.mutProb)
        else:
            raise NoChildException()
        
        
            
class Patient(SimplePatient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """
    
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop
        self.drugs = []
        
    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.drugs
        
    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        totalResistant = 0
        
        for virus in self.viruses:
            drugs = 0
            for drug in drugResist:
                if virus.getResistance(drug) == True:
                    drugs = drugs + 1
            if drugs == len(drugResist):
                #print 'found resistant', totalResistant
                totalResistant = totalResistant + 1
        return totalResistant
                

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of 
          virus particles accordingly
          
        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient. 
          The listof drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces. 

        returns: the total virus population at the end of the update (an
        integer)
        """
        newViruses = []
        for virus in self.viruses:
            if virus.doesClear() == True:
                self.viruses.remove(virus)
        self.popDensity = self.getTotalPop() / float(self.maxPop)
        for virus in self.viruses:
            try:
                child = virus.reproduce(self.popDensity, self.getPrescriptions())
                newViruses.append(child)
            except NoChildException:
                    continue
        self.viruses.extend(newViruses)
        #print 'the new poplulation is', len(self.viruses)
        return self.getTotalPop()
        

#
# PROBLEM 4
#

def problem4():
    """
    Runs simulations and plots graphs for problem 4.

    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.

    total virus population vs. time  and guttagonol-resistant virus population
    vs. time are plotted
    """
    virusesList = []
    maxBirthProb = 0.1
    clearProb = 0.05
    resistance = {'guttagonol':False}
    mutProb = 0.005
    resistantPop = []
    for x in range(0, 100):
        virusesList.append(ResistantVirus(maxBirthProb , clearProb, resistance, mutProb))
    patient = Patient(virusesList, 1000)
    populationList = []
    for x in range(0,300):
        if x == 150:
            patient.addPrescription('guttagonol')
        populationList.append(patient.update())
        resistantPop.append(patient.getResistPop(['guttagonol']))
    
        
    print resistantPop
    virusLine = plt.plot(list(range(0, 300)),
                         populationList,
                         label='Virus population'
                         )
    drugResistantLine = plt.plot(list(range(0, 300)),
                                 resistantPop,
                                 label='Drug resistant virus'
                                 )
    plt.legend([virusLine, drugResistantLine])
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
    #plt.title('Virus and drug resistant population VS Time')
    plt.xlabel('Time steps')
    plt.ylabel('virus population')
    plt.grid()
    plt.show()

problem4()
#
# PROBLEM 5
#
        
def problem5(numberOfPatients, delay):
    """
    Runs simulations and make histograms for problem 5.

    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """
    curedPatients = []
    virusCount = []
    for patient in range(1, numberOfPatients):
        virusesList = []
        maxBirthProb = 0.1
        clearProb = 0.05
        resistance = {'guttagonol':False}
        mutProb = 0.005
        for x in range(0, 100):
            virusesList.append(ResistantVirus(maxBirthProb , clearProb, resistance, mutProb))
        patient = Patient(virusesList, 1000)
        for x in range(0,delay + 150):
            if x == delay:
                patient.addPrescription('guttagonol')
            patient.update()
            #print patient.getTotalPop()
        
        virusCount.append(patient.getTotalPop())
        if patient.getTotalPop() <= 50:
            curedPatients.append(patient)
    #bins = numpy.linspace(-10, 1000, 10)
    healedPercent = len(curedPatients)
    print 'total cured patients is ', healedPercent
    plt.figure()
    plt.hist(virusCount)
    plt.title('Treatment at %s and followed by 150 steps' %delay)
    plt.xlabel('Total virus population, Percentage cured patients is %s ' % healedPercent)
    plt.ylabel('Total patients')
    plt.show()

#problem5(100, 300)

#
# PROBLEM 6
#

def problem6(numberOfPatients, firstDelay, secondDelay):
    """
    Runs simulations and make histograms for problem 6.

    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
    
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """
    curedPatients = []
    virusCount = []
    for patient in range(1, numberOfPatients):
        virusesList = []
        maxBirthProb = 0.1
        clearProb = 0.05
        resistance = {'guttagonol': False, 'gimpex': False}
        mutProb = 0.005
        for x in range(0, 100):
            virusesList.append(ResistantVirus(maxBirthProb , clearProb, resistance, mutProb))
        patient = Patient(virusesList, 1000)
        for x in range(0,firstDelay + secondDelay + 150):
            if x == firstDelay:
                patient.addPrescription('guttagonol')
                print 'deoloyed guttagonol to patient blood'
            if x == firstDelay + secondDelay:
                patient.addPrescription('gimpex')
                print 'deoloyed gimpex to patient blood'
            patient.update()
            #print patient.getTotalPop()
        
        virusCount.append(patient.getTotalPop())
        if patient.getTotalPop() < 50:
            curedPatients.append(patient)
    healedPercent = len(curedPatients)
    print 'total cured patients is ', healedPercent
    plt.figure()
    plt.hist(virusCount)
    plt.title('At %s (guttagonol), At %s (gimpex) followed by 150 steps' %(firstDelay, firstDelay + secondDelay))
    plt.xlabel('Total virus population, Percentage cured patients is %s ' % healedPercent)
    plt.ylabel('Total patients')
    plt.show()

#problem6(100, 150, 0)


#
# PROBLEM 7
#
     
def problem7(firstDelay, secondDelay):
    """
    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.

    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.        
    """
    guttagonolResistance = []
    gimpexResistance = []
    virusCount = []

    virusesList = []
    maxBirthProb = 0.1
    clearProb = 0.05
    resistance = {'guttagonol': False, 'gimpex': False}
    mutProb = 0.005
    for x in range(0, 100):
        virusesList.append(ResistantVirus(maxBirthProb , clearProb, resistance, mutProb))
    patient = Patient(virusesList, 1000)
    for x in range(0,firstDelay + secondDelay + 150):
        if x == firstDelay:
            patient.addPrescription('guttagonol')
            print 'deoloyed guttagonol to patient blood'
        if x == firstDelay + secondDelay:
            patient.addPrescription('gimpex')
            print 'deoloyed gimpex to patient blood'
        patient.update()
        virusCount.append(patient.getTotalPop())
        guttagonolResistance.append(patient.getResistPop(['guttagonol']))
        gimpexResistance.append(patient.getResistPop(['gimpex']))
    plt.figure()
    virusLine, = plt.plot(list(range(0, firstDelay + secondDelay + 150)),
                          virusCount,
                          label='Total virus')
    guttagonolLine, = plt.plot(list(range(0, firstDelay + secondDelay + 150)),
             guttagonolResistance,
             label='Guttagonol resistant virus')
    gimpexLine, = plt.plot(list(range(0, firstDelay + secondDelay + 150)),
             gimpexResistance,
             label='Gimpex resistant virus'
             )
    plt.legend([virusLine, guttagonolLine, gimpexLine])
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
    #plt.title('Virus population VS time')
    plt.ylabel('Total virus population')
    plt.xlabel('Time steps')
    plt.show()
#problem7(150, 0)
