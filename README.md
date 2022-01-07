# Port scanner

A port scanner made with python's socket.

# How to use

Run the scanner.py with this command.

#### windows

`python scanner.py [HOST] [PORT]`

#### linux and mac

`python3 scanner.py [HOST] [PORT]`

# How it work

This port scanner wrote with python and socket.
first it check the given port. if the port was opened, tells you it's opened.
else it check the ports in important_ports list and tells you which port is opened and closed
`important_ports = [20,21,22,23,25,50,51,53,67,68,69,80,110,119,123,135,143,161,162,194,389,443,989,990,3389,443]`
