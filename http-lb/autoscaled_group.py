"""Creates autoscaled, network LB IGM running specified docker image."""


def GenerateConfig(context):
    """Generate YAML resource configuration."""

    # NOTE: Once we can specify the port/service during creation of IGM,
    # we will wire it up here.
    name = context.env['name']
    resources = [{
        'name': name + '-igm',
        'type': 'compute.v1.instanceGroupManager',
        'properties': {
            'zone': context.properties['zone'],
            'targetSize': context.properties['size'],
            'baseInstanceName': name + '-instance',
            'instanceTemplate': context.properties['instanceTemplate']
        }
    }, {
        'name': name + '-as',
        'type': 'compute.v1.autoscaler',
        'properties': {
            'zone': context.properties['zone'],
            'target': '$(ref.' + name + '-igm.selfLink)',
            'autoscalingPolicy': {
                'maxNumReplicas': context.properties['maxSize']
            }
        }
    }]
    return {'resources': resources}