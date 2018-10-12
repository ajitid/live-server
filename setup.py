import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='live_server',
    version='0.9.9',
    author='Ajit Singh',
    author_email='ajit.singh2905@gmail.com',
    description='Serves your pages for development and automatically reloads when changed.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ajitid/live_server',
    packages=setuptools.find_packages(),
    package_data={'live_server': ['liveServer.js']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points='''
        [console_scripts]
        live-server=live_server.cli:cli
    ''',
    python_requires='>=3.4',
    install_requires=['Click == 7.0', 'tornado == 5.1.1',
                      'watchdog == 0.9.0', 'beautifulsoup4 == 4.6.3'],
)
