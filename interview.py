import subprocess
import json
import sys
import argparse

def get_cluster_networks():
    
    cluster_networks = [
        "10.0.0.0/16",      
        "172.16.0.0/16",     
        "192.168.0.0/24",
        "192.168.0.0/24",
        "172.16.0.0/16",  
    ]
    return cluster_networks

    
def main():
    
    cluser_networks = get_cluster_networks()
    
    #parse the input from user
    parser = argparse.ArgumentParser()
    parser.add_argument('--check-collision', 
                        metavar='<path_of_the_file>', 
                        type=str, 
                        help='Example: python3 ip-tool.py --check-collision ./omkar.txt')

    args = parser.parse_args()
  
    if args.check_collision:
        insert_into_file(cluser_networks, args.check_collision)
        check_collision(args.check_collision)
    else:
        # Print container's network ranges
        networks = get_cluster_networks()
        for network in networks:
            print(network)

#create a file according to user's input.    
def insert_into_file(pod_ips,path):
    try:
        with open(path, 'w') as file:
            for ip in pod_ips:
                if ip != None:
                    file.write(ip + "\n")
    except Exception as e:
        print(f"Error writing to file: {e}")
 
#check for duplicate networks by reading through same file that we written.    
def check_collision(file_path):
    
    list_of_networks=list()
    duplicate_networks=list()
    
    try:
        with open(file_path, 'r') as f:
            for ip in f:
                list_of_networks.append(ip)
        
    except (FileNotFoundError, json.JSONDecodeError) as e:
        sys.exit(1)
        
    for i in range(len(list_of_networks)-1):
        for j in range(i+1, len(list_of_networks)):
            if list_of_networks[i]==list_of_networks[j] and list_of_networks[j] not in duplicate_networks:
                duplicate_networks.append(list_of_networks[i])
                print(f"collision in IP addresses detected with duplicate IP: {list_of_networks[j]}")
    
    if len(duplicate_networks)==0:        
        print("No Colliding IPs")
        
    with open("duplicate.out",'w') as file :
        for network in duplicate_networks:
            file.write(network)
    
if __name__ == "__main__":
    main()
    
    
