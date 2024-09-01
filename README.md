# py_smb_worm
![XW](https://res.cloudinary.com/dxubkzzbx/image/upload/v1725223966/worm_dnnrt0.png)

In this Python program, I’ve developed a tool for network scanning and automated exploitation of live hosts within specified IP subnets. The primary objectives are to identify active devices on the network and execute targeted exploit scripts on these devices.

    Network Scanning: The core functionality involves scanning predefined IP subnets to detect live hosts. I use threading to perform this scan in parallel, which helps to speed up the process. Each thread attempts to establish a TCP connection to port 445, commonly associated with SMB (Server Message Block). If a connection is successful, the host is deemed live and is added to a list of live hosts.

    Exploitation: Upon detecting a live host, the program proceeds to execute specific exploitation scripts. These scripts are designed to exploit vulnerabilities associated with EternalBlue and DoublePulsar—two well-known exploits. I’ve set up the program to change the console title to “Hidden” for stealth, and then it runs the corresponding executables with parameters that target the identified host. This part of the program is crafted to demonstrate potential security weaknesses, assuming ethical use such as penetration testing.

    Concurrency Management: To handle the scanning and exploitation efficiently, I use threading to manage concurrent tasks. I’ve implemented a system that monitors the number of active threads to ensure the program does not overload the system. If the number of active threads exceeds a predefined limit, new threads are paused until some of the current threads complete.

    Directory and Exception Handling: I included logic to change the working directory to “depens,” where the exploit executables are expected to be located. If this directory change fails, the program catches the exception and continues execution without it.

    Logging and Output: Throughout the execution, the program provides real-time feedback about the status of the scan and exploitation processes. It logs messages to indicate when hosts are found and when exploits are being executed. After the scan completes, it summarizes the number of live hosts discovered and lists them.

In essence, this program is designed to efficiently identify and test networked devices for specific vulnerabilities, leveraging multithreading to handle multiple tasks simultaneously and providing detailed feedback on its operations.
