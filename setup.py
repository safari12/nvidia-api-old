from setuptools import setup, find_packages

setup(
    name='nvidia-api',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'nvidia_api = app.__main__:main',
        ],
    },
    url='git@github.com:safari12/nvidia-api.git',
    license='MIT',
    author='Reza Safari',
    author_email='rsafari.s@gmail.com',
    description='API for getting Nvidia GPU info'
)
