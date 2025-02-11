# REFNOS PROSPECT
Hello, this README guides you through creating a Smart Solo prospect and setting up the nodes with their corresponding script.

#### Creating a New Prospect

1. Open the _**SoloLite**_ program.

2. Run it as _**Administrator**_.

3. Click on the _**New Prospect**_ icon.![Screenshot 2025-02-03 163240](https://github.com/user-attachments/assets/13da613c-8b8d-49e9-8fc9-6c7c23a6d644)

4. A window titled _**New Project Wizard**_ will appear.![Screenshot 2025-02-03 163425](https://github.com/user-attachments/assets/a5a4829b-10e2-4e5d-919b-5e356e2c8ac7)

5. Enter the Prospect Name, Project Name, and Project Description, then click _**Next**_.

6. Set the Sampling Rate (ms), Lowcut Frequency (Hz), and Filter Type. In our case, we kept the default values for the last two. Click _**Next**_.![Screenshot 2025-02-03 165044](https://github.com/user-attachments/assets/efed2cbd-9fd3-422d-b377-b24eb5696d9b)

7. The _**Project Summary**_ window will display directory paths, leave these unchanged. Click _**Finish**_.![Screenshot 2025-02-03 165254](https://github.com/user-attachments/assets/89773a0f-597d-4d6e-a200-5cb1ce2ca3aa)

8. Your project is now created!

#### Setting Up the Script

1. Click on the _**Setup Script**_ icon.
![Screenshot 2025-02-03 165422](https://github.com/user-attachments/assets/ca49789c-3390-45f8-994c-6c6556f7d8ec)

2. A new window will appear where you can configure the necessary parameters for your project.
    - Pay special attention to the _**FIFO (First In, First Out)**_ option, this feature allows old data to be automatically overwritten when redeploying the node.
![Screenshot 2025-02-03 170734](https://github.com/user-attachments/assets/1c57032b-285d-4330-9169-678add87da6f)

3. Once all settings are configured, click _**OK**_.

#### Configuring the Nodes

1. Click on the _**Setup IGU-16**_ icon.
![Screenshot 2025-02-03 162110](https://github.com/user-attachments/assets/ebfa9122-bd6d-4722-b51e-dfdc685880bf)

2. In the _**Device Setup**_ window, check the following boxes:
    - Select All
    - Format Device
    - Retain Configuration Files
    - Write Script (Ensure you select the correct script)
![Screenshot 2025-02-03 162210](https://github.com/user-attachments/assets/2df94d80-057e-4caf-9111-79ea82300ab4)

3. Click _**Apply**_ and wait for the nodes to be configured.

4. Once the process is complete, close the SoloLite program.
