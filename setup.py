from setuptools import setup
from agent2 import __version__

setup(name="openproximity-agent2",
      version = __version__,
      packages = ['agent2',
                  'agent2.management', 
                  'agent2.management.commands', ],
      include_package_data = True,
      package_data = {
        'agent2': [
            'templates/agent2/*', 
            ]},
    summary = "OpenProximity Agent2",
    description = 
      """A data collector that pushes records into a centralized server.""",
    author = "Naranjo Manuel Francisco",
    author_email = "manuel@aircable.net",
    license = "GPL2",
    url = "https://github.com/OpenProximity/plugins-agent2", 
)
