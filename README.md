# ip-tool script

(Interview.py)
IP tool script performs task according to user input. 
1. If user does not provide any input it will just return the networks in the cluster.
2. If user inputs --check-collision flag - it will check and print duplicate networks in the cluster. Also it will create duplicate.out file and will store the networks in that file.

How to Run:
"python3 interview.py" OR
"python3 interview.py --check-collision abc.txt"(or whatever name you want to give instead of abc.txt).

(Dockerfile)
Dockerfile dockerizes the application so application can be portable. There are 2 ways to run the dockerfile.

How to Run:
1. docker run <image_name> : This will print just the networks present in the cluster  OR
2. docker run <image_name> --check-collision <file_name> : This will check for colliding networks and print that.

(Deployment.yaml)
Deploys the application in pod. By default I have written it in such a way that it will execute "python3 interview.py --check-collision abc.txt".
Also for this example's sake, I have kept pod up for infinity time.

