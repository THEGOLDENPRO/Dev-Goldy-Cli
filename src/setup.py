from setuptools import setup, find_packages

from DevGoldy import info

setup(
  name='DevGoldy',
  version=f"{info.VER}{info.STAGE[0]}{info.STAGE[1]}",
  description='My own custom cli software I install on every server/machine.', 
  url='https://github.com/THEGOLDENPRO/Dev-Goldy-Cli', 
  project_urls={"Bug Tracker": "https://github.com/THEGOLDENPRO/Dev-Goldy-Cli/issues"}, 
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