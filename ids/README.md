## Intrusion Detection Using Raspberry Pi

.bashrc is used to automate the raspberry pi as plug and play, ssh is used to islote the system in case infected. YARA rules is used for malware detection in network, tshark is used to capture packets and bro is used to analyze them and extract the files.

## Working 

![alt text](https://github.com/pravinkumarosingh/projects/blob/master/ids/upes.jpeg)

![alt text](https://github.com/pravinkumarosingh/projects/blob/master/ids/upes1.jpeg)

#### Kitnet algorithm is used which provides higher approximation rate of differentiation between normal and abnormal traffic. Under the hood this algorithm uses Artificial Neural Network to achieve it's goal.

## Future Work
The current idea is to convert the logs into images and train the model using deep learning to detect any zero days in the network, the idea is to convert the conn.log into matrix consisting of each network request as 1 or a 0. Every malware after certain succession reaches out to its CnC server, however these connections made form a pattern. N number of patterns can be made and converted into image (since we convert logs into matrix, there after converting them into image) and irregularities can be reported.



Presented at UPES Hackathon 2020 Dehradun.
