# ASL-gloves

1. Roadmap:
    - Brainstorm Ideas (Done) June 16th, 2022
    - Build the circuit connecting the Arduino ESP32-WROOM-32D to the flex sensors. (Done) June 17th, 2022
    - Build the gloves with the circuitry on it. (Done) June 17th 2022
    - Write a HTTP server that saves all POST requests into a CSV file. (Done) June 17th 2022
        - The Arduino is able to send POST requests, but is pretty slow at doing so. What I hope to do is optimize it a bit further or maybe even switch to a different device (Teensy 4.1 is looking very enticing for only 30 dollars.)
        - The HTTP server should be able to differentiate between the two gloves. (I only have 1 glove at the moment but I plan on building 2)
    - Learn the very basics of machine learning, and try to get it to differentite between the letters in the alphabet. (Done) July 17th, 2022
    - Hook up my accelerometer/gyroscope module [MPU-6050] to the Arduino and pass all that data back to the HTTP server. (Done) June 18th, 2022
    - Replace flex sensors with [Val's Indexers](https://www.youtube.com/watch?v=R4z_pNbKnNo)
        - Reason for replacing the flex sensors with Val's Indexers is because the flex sensors are
            1. Inaccurate
            2. Can't detect splay
            3. Expensive
            4. Hard to keep superglued
        - Val's indexers are just much better for the job. They're far more accurate due to the use of potentiometers instead of flex sensors, which could lead to higher quality data. 
    - Write a neural network that can translate the hand movements into images. This shouldn't be that hard.
    - USe the same neural network and match it with an ASL dict\
