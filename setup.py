from __future__ import print_function
from setuptools import setup, find_packages
import os
from distutils import log

from jupyter_packaging import (
    create_cmdclass,
    install_npm,
    ensure_targets,
    combine_commands,
    get_version,
)

name = 'ipytree'

here = os.path.dirname(os.path.abspath(__file__))
long_description = 'A Tree Widget using jsTree'

log.set_verbosity(log.DEBUG)
log.info('setup.py entered')
log.info('$PATH=%s' % os.environ['PATH'])

# Get ipytree version
version = get_version(os.path.join(name, '_version.py'))

js_dir = os.path.join(here, 'js')

# Representative files that should exist after a successful build
jstargets = [
    os.path.join(js_dir, 'dist', 'index.js'),
]

data_files_spec = [
    ('share/jupyter/nbextensions/ipytree', 'ipytree/static', '*.*'),
    ('etc/jupyter/nbconfig/notebook.d', '.', 'ipytree.json'),
]

cmdclass = create_cmdclass('jsdeps', data_files_spec=data_files_spec)
cmdclass['jsdeps'] = combine_commands(
    install_npm(js_dir, build_cmd='build'), ensure_targets(jstargets),
)

setup_args = {
    'name': name,
    'version': version,
    'description': 'A Tree Widget using jsTree',
    'long_description': long_description,
    'include_package_data': True,
    'install_requires': [
        'ipywidgets>=7.5.0,<8',
    ],
    'packages': find_packages(),
    'zip_safe': False,
    'cmdclass': cmdclass,
    'author': 'Martin Renou',
    'author_email': 'martin.renou@gmail.com',
    'url': 'https://github.com/martinRenou/ipytree',
    'keywords': [
        'ipython',
        'jupyter',
        'widgets',
    ],
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Multimedia :: Graphics',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
}

setup(**setup_args)
