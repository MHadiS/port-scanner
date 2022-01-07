import socket
import sys


important_ports = [20, 21, 22, 23, 25, 50, 51, 53, 67, 68, 69, 80, 110,
                   119, 123, 135, 143, 161, 162, 194, 389, 443, 989, 990, 3389, 443]


def scan_ports():
    """scan the ports in important port list and return open and closed ports in dict format"""
    open_ports = []
    close_ports = []
    for port in important_ports:
        try:
            s.connect((HOST, port))
            open_ports.append(port)
            s.close()
        except:
            close_ports.append(port)
    return {"open": open_ports, "closed": close_ports}


def show_help():
    """print something to help user use the port scanner"""
    print("This program is a port scanner.")
    print("To use this program run this command.")
    print("command for windows: python scanner.py [HOST] [PORT]")
    print("command for linux and mac: python3 scanner.py [HOST] [PORT]")


def main():
    """scainnng the port(s)"""
    global s, HOST

    # making a socket to check the ports
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[ COMPELTED ] Socket successfully created")
    except socket.error as err:
        print(f"[ ERROR ] socket creation failed with error {err}")

    # get host and ip from user
    try:
        HOST = socket.gethostbyname(sys.argv[1])
        PORT = int(sys.argv[2])
    except IndexError:

        # if user didn't run the program true show_help function will run
        show_help()
        sys.exit()
    except socket.gaierror:

        # if the user entered url for host and program couldn't convert it to ip this massege will appears
        print(
            "[ ERROR ] there was an error resolving the host. your internet might be disconnected")
        sys.exit()

    # scanning the ports
    try:
        s.connect((HOST, PORT))  # try to connecting to port
        s.close()
        print(
            f"[ COMPELTED ] Successfully connected to {HOST} with port {PORT}")
    except:

        # if the port was closed check the ports in important ports list
        print(f"[ ERROR ] failed to connecte to {HOST} with port {PORT}")
        ports = scan_ports()  # scan the ports

        # show the results of scan
        for port_type in ports:
            for port in ports[port_type]:
                if port_type == "open":
                    print(f"\033[1;32m port {port} is open\033[00m")
                else:
                    print(f"\033[91m port {port} is closed \033[00m")


if __name__ == "__main__":
    main()
