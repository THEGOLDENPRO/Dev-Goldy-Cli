from setuptools import setup, find_packages

setup(
  name='DevGoldy',
  version="1.2dev",
  description='My own custom server software I install on every server.', 
  url='https://github.com/THEGOLDENPRO/Dev-Goldy-Server-Software', 
  project_urls={"Bug Tracker": "https://github.com/THEGOLDENPRO/Dev-Goldy-Server-Software/issues"}, 
  author='Dev Goldy', 
  author_email='goldy@novauniverse.net', 
  license='MIT',
  packages=find_packages(), 
  include_package_data=True,
  install_requires=open('requirements.txt').read(),
  python_requires=">=3.8",

  entry_points = {
    "console_scripts": [
      "devgoldy = DevGoldy.dev_goldy:devgoldy"
    ]
  },
)