
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='jamf_helper_window_tool',  
     version='0.1',
     scripts=['makewindow.py'] ,
     author="Zackn9ne",
     author_email="zackn9ne@gmail.com",
     description="A jamf helper window creator tool",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/zackn9ne/module_jamf_helper_window.git",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
