from setuptools import setup

setup(
    name="electrum-server-cesc", 
    version="1.0.20160803",
    scripts=['run_electrum_server_cesc','electrum-server-cesc'],
    install_requires=['plyvel','jsonrpclib', 'irc >= 11, <=14.0'],
    package_dir={
        'electrumservercesc':'src'
        },
    py_modules=[
        'electrumservercesc.__init__',
        'electrumservercesc.utils',
        'electrumservercesc.storage',
        'electrumservercesc.deserialize',
        'electrumservercesc.networks',
        'electrumservercesc.blockchain_processor',
        'electrumservercesc.server_processor',
        'electrumservercesc.processor',
        'electrumservercesc.version',
        'electrumservercesc.ircthread',
        'electrumservercesc.stratum_tcp'
    ],
    description="Cryptoescudo Electrum Server",
    author="Marcdnd",
    author_email="marcdnd@gmail.com",
    license="MIT Licence",
    url="https://github.com/Marcdnd/electrum-server-cesc/",
    long_description="""Server for the Electrum Lightweight Cryptoescudo Wallet"""
)
