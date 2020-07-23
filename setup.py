from setuptools import setup, find_packages


setup(
    name='project20',
    version='0.0.1',
    packages=find_packages(include=['project20', 'project20.*']),
    python_requires='>=3.7',
    install_requires=[
        'flake8',
        'flake8-docstrings',
        'gitpython',
        'tqdm',
        'mlflow==1.10.0',
        'orion>=0.1.8',
        'pyyaml>=5.3',
        'pytest>=4.6',
        'sphinx',
        'sphinx-autoapi',
        'sphinx-rtd-theme',
        'sphinxcontrib-napoleon',
        'sphinxcontrib-katex',
        'recommonmark',
        'torch'],
    entry_points={
        'console_scripts': [
            'main=project20.main:main'
        ],
    }
)
