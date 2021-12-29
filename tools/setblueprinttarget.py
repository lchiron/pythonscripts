import os, ntpath, glob, sys
import oyaml as yaml
import ruamel.yaml

blueprints = glob.glob('/Users/edward.li/Farfetch/blueprints/blueprints/*/*/*.yaml')

yamlfortmat = ruamel.yaml.YAML()
yamlfortmat.indent(sequence=4, offset=2)
yamlfortmat.width = 4096
yamlfortmat.preserve_quotes=True

def addtarget(blueprints):
    for blueprint in blueprints:
        try:
            with open(blueprint, 'r') as yamlfile:
                data = yamlfortmat.load(yamlfile)
                if 'environment_specific' in data  and 'target' in data['environment_specific'][0] and data['platform'] != 'dragon' and len(data['environment_specific'])>1:
                    for env in data['environment_specific']:
                        dc = env['datacenter']
                        context = data['security']['context']
                        cluster = dc+'-prd-asf-'+context+'-svc'
                        target = {'platform': 'infrastructure', 'boundary': 'kubernetes', 'name': cluster, 'traffic_weight': 0}
                        flag = True
                        if 'prd' in env['environment']:
                            for item in env['target']:
                                if cluster in item['name']:
                                    flag = False
                        if 'prd' in env['environment'] and flag:
                            env['target'].append(target)

                    if data:
                        print("Changing {}".format(blueprint))
                        with open(blueprint,'w') as yamlfile:
                            yamlfortmat.dump(data, yamlfile)
        except Exception as exc:
            print('Error: {} has error {} , continue'.format(blueprint, exc))
        
def gettargetinfo(blueprints):
    for i in blueprints:
        with open(i) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            if 'environment_specific' in data  and 'target' in data['environment_specific'][0] and data['platform'] != 'dragon':
                print(i)
                for env in data['environment_specific']:
                    if 'target' in env and env['environment'] != 'dev':
                        print(env['target'])


if __name__ == '__main__':
    addtarget(blueprints)
