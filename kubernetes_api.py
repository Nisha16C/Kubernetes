import streamlit as st
from kubernetes import client, config

# Load the Kubernetes configuration
config.load_kube_config()

# Create a Kubernetes API client
v1 = client.CoreV1Api()

# Get all the namespaces in the Kubernetes cluster
namespace_list = v1.list_namespace().items
namespace_names = [ns.metadata.name for ns in namespace_list]

# Create a streamlit web app
st.title("Kubernetes Pod Viewer")

# Add a selectbox to choose a namespace
namespace = st.sidebar.selectbox("Select Namespace", namespace_names)

# List all the pods in the selected namespace
st.write(f"**Pods in Namespace {namespace}**")
pod_list = v1.list_namespaced_pod(namespace=namespace).items
for pod in pod_list:
    st.write(pod.metadata.name)


import streamlit as st
# from kubernetes import client, config
#
# # Load the Kubernetes configuration
# config.load_kube_config()
#
# # Create a Kubernetes API client
# v1 = client.CoreV1Api()
#
# pod_list = v1.list_namespaced_pod(namespace='kube-system')
# for pod in pod_list.items:
#     print(pod.metadata.name)

