# README

## Introduction

This code is a Streamlit web app that allows users to view Kubernetes pods in a selected namespace. The app uses the Kubernetes Python client library to communicate with the Kubernetes API and fetch the pods.

## Installation

To run this code, you need to have Python 3 and Streamlit installed. You can install Streamlit using pip:

```
pip install streamlit
```

You also need to have a Kubernetes cluster set up and configured on your system. The app uses the Kubernetes configuration file (`~/.kube/config` by default) to authenticate with the Kubernetes API.

You can install the required dependencies by running the following command:

```
pip install kubernetes
```

## Usage

To run the app, open a terminal and navigate to the directory where the code is saved. Then, run the following command:

```
streamlit run app.py
```

This will launch the app in your default web browser. The app will display a list of namespaces in your Kubernetes cluster. You can select a namespace from the dropdown menu on the sidebar to view the pods in that namespace.

The app will display the name of each pod in the selected namespace.

## Code Explanation

The code starts by importing the required libraries: Streamlit and the Kubernetes Python client.

```
import streamlit as st
from kubernetes import client, config
```

The next step is to load the Kubernetes configuration from the default location (`~/.kube/config`).

```
config.load_kube_config()
```

Then, a Kubernetes API client is created using the `CoreV1Api` class.

```
v1 = client.CoreV1Api()
```

The app uses the `list_namespace()` method to fetch a list of all the namespaces in the Kubernetes cluster. The `metadata.name` attribute of each namespace is added to a list.

```
namespace_list = v1.list_namespace().items
namespace_names = [ns.metadata.name for ns in namespace_list]
```

The app then creates a Streamlit web app and displays a dropdown menu on the sidebar, allowing users to select a namespace.

```
st.title("Kubernetes Pod Viewer")
namespace = st.sidebar.selectbox("Select Namespace", namespace_names)
```

When the user selects a namespace, the app uses the `list_namespaced_pod()` method to fetch a list of all the pods in that namespace. The `metadata.name` attribute of each pod is displayed using the `st.write()` method.

```
pod_list = v1.list_namespaced_pod(namespace=namespace).items
for pod in pod_list:
    st.write(pod.metadata.name)
```

## Conclusion

This code demonstrates how to use the Kubernetes Python client library to fetch information from a Kubernetes cluster and display it in a Streamlit web app. With this app, users can easily view the pods running in a selected namespace without having to use the Kubernetes command-line interface.