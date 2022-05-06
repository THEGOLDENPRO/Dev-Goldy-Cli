from setuptools import setup, find_packages

setup(
  name='DevGoldy',
  version="1.0dev",
  description='My own custom server software I install on every server.', 
  url='https://github.com', 
  project_urls={"Bug Tracker": "https://github.com/Goldy-Bot/Goldy-Bot-V4/issues"}, 
  author='Dev Goldy', 
  author_email='goldy@novauniverse.net', 
  license='MIT',
  keywords=["goldy bot", "Goldy Bot", "Goldy Bot V4", "Goldy Bot V3", "goldy"], 
  packages=find_packages(), 
  include_package_data=True,
  install_requires=open('requirements.txt').read(),
  python_requires=">=3.8"
)