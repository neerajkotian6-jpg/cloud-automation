import subprocess
import re
from kubernetes import client, config

def get_node_status(node_name):
    """Aggregates Node health and events"""
    config.load_kube_config()
    v1 = client.CoreV1Api()
    
    # Extracting Internal IP via Regex from 'kubectl describe'
    describe = subprocess.check_output(["kubectl", "describe", "node", node_name]).decode()
    node_ip = re.search(r"InternalIP:\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", describe).group(1)
    
    # Fetching node-specific events
    events = v1.list_event_for_all_namespaces(
        field_selector=f"involvedObject.kind=Node,involvedObject.name={node_name}"
    )
    return node_ip, events.items

print("Node Diagnostics Module Loaded.")
