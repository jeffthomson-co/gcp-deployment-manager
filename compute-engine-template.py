"""Creates the Compute Engine."""

NETWORK_NAME = 'once-upon-a-custom-network'

def GenerateConfig(unused_context):
    """Creates the Compute Engine with network and firewall."""

    resources = [{
        'name': 'the-first-vm',
        'type': 'vm-template.py',
        'properties': {
            'machineType': 'f1-micro',
            'zone': 'europe-west2-a',
            'network': NETWORK_NAME,
        }
    }, {
        'name': 'the-second-vm',
        'type': 'vm-template.py',
        'properties': {
            'machineType': 'f1-micro',
            'zone': 'europe-west2-a',
            'network': NETWORK_NAME,
        }
    }, {
        'name': NETWORK_NAME,
        'type': 'network-template.py',
    }, {
        'name': NETWORK_NAME + '-firewall',
        'type': 'firewall-template.py',
        'properties': {
            'network': NETWORK_NAME,
        }
    }]
    return {'resources': resources}