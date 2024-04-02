

"""
port scanner

python portscanner.py -host=localhost -port=5000
Scanning host: localhost port: 5000
Port: 5000 is open

"""

import click
import socket
import time
import random

@click.command()
@click.option("-host")
@click.option("-port")
def port_scanner(host, port):

    host_list = host.split(',')

    def scanner(input_host, input_port):
        # rand_num = random.randrange(10000)
        # sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
        # sock.bind(("en1", 0))
        # sock.send(rand_num)
        # sock.settimeout(1)  # quickly checks if port is open
        # message = sock.recv(4096)
        # print('*******message: ', message)
        # sock.close()

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # quickly checks if port is open
        return_data = sock.connect_ex((input_host, int(input_port)))
        sock.close()
        return return_data

    def printer(status, current_port, has_input=False):
        status = "open" if status == 0 else "not open"
        msg = f"Port: {current_port} is {status}"
        if has_input is True:
            click.echo(msg)
        else:
            if status == "open":
                click.echo(msg)

    def helper(current_host, current_port):
        if current_port:
            result = scanner(current_host, current_port)
            printer(result, current_port, True)
        else:
            total_ports = 65535  # 16 bit unsigned range
            for p in range(2000, total_ports):
                result = scanner(current_host, p)
                printer(result, p)
        return

    print_port = port if port else "all"

    start = time.time()
    for each_host in host_list:
        click.echo(f"scanning host: {each_host} port: {print_port}")
        if each_host[-1] == '*':
            for i in range(255):
                helper(each_host[:-1] + str(i), port)
        else:
            helper(each_host, port)
    end = time.time()
    print('time elapsed : ', end - start)




























if __name__ == "__main__":
    port_scanner()