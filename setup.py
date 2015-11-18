import os
import setuptools

setuptools.setup(
    name='service-broker',
    version="0.1.0",
    description='The service broker for cloudfoundry service marketplace',
    author='EMC Labs China',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
    ],
    packages=setuptools.find_packages(exclude=['bin']),
    setup_requires=['setuptools_git>=0.4'],
    scripts=['bin/service-broker'],
    data_files=[(['/etc/service-broker'][os.sep == '\\'],
                 ['etc/service-broker/service_broker.conf.sample'])]

)