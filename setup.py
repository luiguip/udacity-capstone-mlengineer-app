from distutils.core import setup

setup(
    name='dog_breeds_app',
    version='0.1',
    packages=['dog_breeds_app'],
    install_requires=['numpy', 'pandas', 'torch', 'opencv-python', 'torchvision'],
    license='MIT',
    long_description=open('README.md').read(),
    scripts=['bin/dog-breeds-app'],
)
