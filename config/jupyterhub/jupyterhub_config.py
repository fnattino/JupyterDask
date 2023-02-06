# Configuration file for jupyterhub.

c = get_config()  #noqa

# docker spawner
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# The docker instances need access to the Hub, so the default loopback port doesn't work:
from jupyter_client.localinterfaces import public_ips
c.JupyterHub.hub_ip = public_ips()[0]

# Define image and start command (if not defined in image)
c.DockerSpawner.image = 'pangeo/pangeo-notebook'
c.DockerSpawner.cmd = ['jupyterhub-singleuser']

