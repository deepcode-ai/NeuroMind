from setuptools import setup
from setuptools import find_packages

setup(name='NeuroMind',
      version='0.0.1',
      description='Deep Learning implying human understanding',
      author='DeepCode AI',
      author_email='dev.sulaiman@icloud.com',
      url='https://github.com/deepcode-ai/neuromind',
      license='MIT',
      install_requires=['theano', 'h5py'],
      packages=find_packages(),
)