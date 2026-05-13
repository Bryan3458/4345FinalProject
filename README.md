# 4345FinalProject
Transmitting Data Over Sound

Overview
This project is about transmitting data over sound. Instead of using Wi-Fi or a network cable, we’re using the laptop's speakers and mic to move info. One terminal window "talks" in beeps, and the other window "listens" and turns those beeps back into text.

1. What You Need
Visual Studio Code: We used this as our editor to write and manage the code.

Install the Tools: Open powershell and run this command to get the audio libraries:
pip install sounddevice numpy scipy

Keeping them Together: Create a folder and open it in VS Code. Inside that folder, create two files named sender.py and receiver.py. Then, copy the code from the repository into each file accordingly, making sure both files are saved in the same directory.

2. How to Run It
Open the Folder: Find the folder where you saved your files.

Open PowerShell: Right-click on that folder and select "Open in Terminal". Duplicate the window you opened so you have two separate windows open side-by-side allowing you to run both files.

Start Receiver: In the first PowerShell window, type:
python receiver.py

Start Sender: In the second PowerShell window, type:
python sender.py

Send it: Type a message in the sender window and hit Enter. You’ll hear the beeps and see the 0s and 1s pop up in the receiver window as it decodes the message!

3. How the Beeps Work
The computer uses these specific "pitches" (Hz) to know what’s going on:

500 Hz: The "Start" signal. It tells the mic to wake up and start recording.

1000 Hz: This represents a 0.

2000 Hz: This represents a 1.

3000 Hz: The "End" signal. This tells the receiver the message is done.
