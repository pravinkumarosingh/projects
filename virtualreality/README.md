## Galvanic Vestibular Stimulation using Virtual Reality

#### This project is based on two domains the first one is BCI(Brain Computer Interface) and second one is VR(Virtual Reality).

#### But the question is ,What is BCI?


### BCI - Brain Computer Interface
 Brain Computer Interface is the concept of connecting human brain to the computing device with a goal to control the human brain. This concept has actually arrived from the    studies of Neuroscience. Neuroscience is the field of science which focuses on studying the neurons of living organisms. Neurons are the core part of human bodies too. The signal which we receive from environment and process it the brain are actually done through the neurons present in our body. But coming to BCI there are two categories of BCI.
 
 ### Categories of BCI
 1. Invasive BCI
 2. Non-Invasive BCI

#### Invasive BCI
In Invasive BCI the electrodes which are used to control the human brain are implanted inside the human brain. Example for this is the [Neuralink](https://neuralink.com/) project funded by Elon Musk.

#### Non-Invasive BCI
In Non-Invasive BCI there is no need to implant the electrodes inside the brain instead it sticked to the essential part of the brain where the neurons are mostly active.

### VR - Virtual Reality
Virtual Reality is the simulation of the real environment. We all know the metaverse which is trending technology, it is also being called the new version of the internet. The word metaverse is derived from the meta which means __beyond__ and verse meaning __universe__. Now enough talking about the domains let's dive into project. 

### Basic Idea About the Project
Suppose you are  driving a car What are motion you feel due to inertia. If you apply a brake you bend forward if you turn left your body lean in the left direction same for the right side direction. This is what we replicating but in a virtual environment. 

### What is Galvanic?
Galvanic is aka galvanic current is the process of the passing the electric current to the __vestibular labyrinth__. Vestibular Labyrinth are the sensory organs below the ear.

![galvanic-stimulation](https://github.com/pravinkumarosingh/projects/blob/master/virtualreality/images/galvanic-stimulation.jpg)

### Basic Overview
![architecture](https://github.com/pravinkumarosingh/projects/blob/master/virtualreality/images/architecture.png)

### Tools Used

#### Hardware
* PNP Transistor
* NPN Transistor
* Resistors
* Raspberry PI
* 12 Volts Battery
* Bread Board
* Electrodes
* Digital Mulitmeter (for monitoring the current)

#### Software
* Blender
* Unity 3D
* Python 

### Circuit
Circuit in the project is the interface between human brain and virtual reality simualtion. The main part in the circuit is H-bridge which is responsible for the flow of current. Galvanic Stimulation totally depend on this part of the circuit. H-bridge maintains the current at 3mA which is the required current. The current should not exceed this level. The second part in the circuit is connecting with the raspberry pi so as to control the simulation. Power supply to the circuit is done through the 12 Volts battery.

![circuit](https://github.com/pravinkumarosingh/projects/blob/master/virtualreality/images/circuit.png)


### Simulation
Simulation is the virtual reality part of the project. Although the project is suitable for any simulation we decided to use the car simulation. Car simulation was rendered using __Blender__ a open source software for modelling and rendering the simulation. The animation is done through the __Unity 3D__ which another software widely used for game development.  

![car-simulation](https://github.com/pravinkumarosingh/projects/blob/master/virtualreality/images/car-simulation.png)

### References
1. [Galvanic Vestibular Stimulation](https://www.sciencedirect.com/topics/medicine-and-dentistry/galvanic-vestibular-stimulation)
2. [Full body haptic display for low-cost racing car driving simulators](https://ieeexplore.ieee.org/document/5759490)






