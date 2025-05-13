import os
import yaml
from atlas import Atlas

class Atlas(Atlas):
    def get_project_clusters(self, group_id):
        return self.call('GET', f'/groups/{group_id}/clusters')
    
    def pause_cluster(self, group_id, cluster_name):
        payload = {"paused": True}
        return self.call('PATCH', f'/groups/{group_id}/clusters/{cluster_name}', json=payload)

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_file = os.path.join(dir_path, 'config.yaml')
    with open(config_file, 'r') as fh:
        config = yaml.safe_load(fh)
    
    atl = Atlas(config["public_key"], config["private_key"])
    response = atl.get_project_clusters(config["group_id"])
    
    for cluster in response.json()["results"]:
        print(f'Attempting to pause {cluster["name"]}')
        response = atl.pause_cluster(config["group_id"], cluster["name"])
        print(response.status_code)

if __name__ == '__main__':
    main()