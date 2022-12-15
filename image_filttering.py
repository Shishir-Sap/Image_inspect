import json
f = open('image_inspect.json',"r")
input_file=(f.read())
#print(input_file)
docker_dict2 = json.loads(input_file)
print(docker_dict2[0].keys())
print("-----------Antword--------------")
print(docker_dict2[0]["Created"])

print(docker_dict2[0]["RepoTags"])
print(docker_dict2[0]["ContainerConfig"]["Hostname"])
print(docker_dict2[0]["DockerVersion"])




