Electrum-server for the Electrum client
=========================================

  * Authors: Thomas Voegtlin (ThomasV on the bitcointalk forum)
  * Cryptoescudo features: Marcdnd (marcdnd on [cryptoescudotalk.com](http://cryptoescudotalk.com) forum)
  * Language: Python

Features
--------

  * The server indexes UTXOs by address, in a Patricia tree structure
    described by Alan Reiner (see the 'ultimate blockchain
    compression' thread in the Bitcointalk forum)

  * The server requires cryptoescudod, leveldb and plyvel

  * The server code is open source. Anyone can run a server, removing
    single points of failure concerns.

  * The server knows which set of Cryptoescudo addresses belong to the same
    wallet, which might raise concerns about anonymity. However, it
    should be possible to write clients capable of using several
    servers.

Installation
------------

  1. To install and run a server, see [INSTALL](https://github.com/Marcdnd/electrum-server-cesc/blob/master/INSTALL). For greater
     detail on the installation process, see [HOWTO.md](https://github.com/Marcdnd/electrum-server-cesc/blob/master/HOWTO.md).

  2. To start and stop the server, use the 'electrum-server-cesc' script



License
-------

Electrum-server is made available under the terms of the [GNU Affero General
Public License](http://www.gnu.org/licenses/agpl.html), version 3. See the 
included `LICENSE` for more details.
