from setuptools import setup

setup(
    name="electrum-server-cesc",
    version="0.9",
    scripts=['run_electrum_server_cesc','electrum-server-cesc'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
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
        'electrumservercesc.stratum_tcp',
        'electrumservercesc.stratum_http'
    ],
    description="Cryptoescudo Electrum Server",
    author="Thomas Voegtlin (thomasv1@gmx.de) / Marcdnd (CESC)",
    author_email="marcdnd@gmail.com",
    license="GNU Affero GPLv3",
    url="https://github.com/Marcdnd/electrum-server-cesc/",
    long_description="""Server for the Electrum Lightweight Cryptoescudo Wallet"""
)


