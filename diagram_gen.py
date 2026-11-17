def export_mermaid_diagram():
    print('''
flowchart TD
    WAN((Internet Gateway)) --> FW[Palo Alto NGFW]
    FW --> CoreSW[Cisco Core 3850]
    CoreSW --> ASW1[Access SW - VLAN 10]
    CoreSW --> ASW2[Access SW - VLAN 20]
''')

if __name__ == '__main__':
    export_mermaid_diagram()
