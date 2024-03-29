"""Creates a Container VM with the provided Container manifest."""

from container_helper import GenerateManifest


def GenerateConfig(context):
    """Generates configuration."""

    image = ''.join(['https://www.googleapis.com/compute/v1/',
                     'projects/cos-cloud/global/images/',
                     context.properties['containerImage']])
    default_network = ''.join(['https://www.googleapis.com/compute/v1/',
                               'projects/', context.env['project'],
                               '/global/networks/default'])

    instance_template = {
        'name': context.env['name'] + '-it',
        'type': 'compute.v1.instanceTemplate',
        'properties': {
            'properties': {
                'metadata': {
                    'items': [{
                        'key': 'gce-container-declaration',
                        'value': GenerateManifest(context)
                        }]
                    },
                'machineType': 'f1-micro',
                'disks': [{
                    'deviceName': 'boot',
                    'boot': True,
                    'autoDelete': True,
                    'mode': 'READ_WRITE',
                    'type': 'PERSISTENT',
                    'initializeParams': {'sourceImage': image}
                    }],
                'networkInterfaces': [{
                    'accessConfigs': [{
                        'name': 'external-nat',
                        'type': 'ONE_TO_ONE_NAT'
                        }],
                    'netowrk': default_network
                    }],
                'serviceAccounts': [{
                    'email': 'default',
                    'scopes': ['https://www.googleapis.com/auth/logging.write']
                    }]
                }
            }
        }

    outputs = [{'name': 'instanceTemplateSelfLink',
                'value': '$(ref.' + instance_template['name'] + '.selfLink)'}]

    return {'resources': [instance_template], 'outputs': outputs}