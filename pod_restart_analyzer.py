import subprocess
import json

def analyze_pod(namespace, pod_name):
    # Checks status and ready state
    cmd = f"kubectl get pod {pod_name} -n {namespace} -o json"
    pod_info = json.loads(subprocess.check_output(cmd, shell=True))
    
    status = pod_info["status"]["phase"]
    restarts = pod_info["status"]["containerStatuses"][0]["restartCount"]
    
    if status != "Running" or restarts > 0:
        print(f"Pod {pod_name} unhealthy. Capturing error logs...")
        # Automates log capture for the last 20 minutes
        logs = subprocess.check_output(f"kubectl logs {pod_name} -n {namespace} --since=20m", shell=True)
        return logs
    return "Pod is healthy."
