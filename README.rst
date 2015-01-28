#########
CryptoFun
#########

Task
====

Kommunikation [12Pkt]
~~~~~~~~~~~~~~~~~~~~~

Programmieren Sie eine Kommunikationsschnittstelle zwischen zwei Programmen
(Sockets; Übertragung von Strings). Implementieren Sie dabei eine unsichere
(plainText) und eine sichere (secure-connection) Übertragung.

Bei der secure-connection sollen Sie eine hybride Übertragung nachbilden. D.h.
generieren Sie auf einer Seite einen privaten sowie einen öffentlichen
Schlüssel, die zur Sessionkey Generierung verwendet werden. Übertragen Sie den
öffentlichen Schlüssel auf die andere Seite, wo ein gemeinsamer Schlüssel für
eine synchrone Verschlüsselung erzeugt wird. Der gemeinsame Schlüssel wird mit
dem öffentlichen Schlüssel verschlüsselt und übertragen. Die andere Seite kann
mit Hilfe des privaten Schlüssels die Nachricht entschlüsseln und erhält den
gemeinsamen Schlüssel.

Sniffer [4Pkt]
~~~~~~~~~~~~~~

Schreiben Sie ein Sniffer-Programm (Bsp. mithilfe der jpcap-Library
http://jpcap.sourceforge.net oder jNetPcap-Library http://jnetpcap.com/),
welches die plainText-Übertragung abfangen und in einer Datei speichern kann.
Versuchen Sie mit diesem Sniffer ebenfalls die secure-connection anzuzeigen.

Info
~~~~

Gruppengröße: 2 Mitglieder
Punkte: 16

* Erzeugen von Schlüsseln: 4 Punkte
* Verschlüsselte Übertragung: 4 Punkte
* Entschlüsseln der Nachricht: 4 Punkte
* Sniffer: 4 Punkte

Cryptographic libraries
=======================

Design
======

Protocol
~~~~~~~~

UML
~~~

Effort estimate
===============

================================ ========
Task                             Estimate
                                 [hh:mm]
================================ ========
Evaluation of crypto libraries    02:00
Protocol design                   02:00
Application design                02:00
Documentation                     02:00
Implementation                    04:00
Testing                           02:00
================================ ========

Time recording
==============

Jakob Klepp
~~~~~~~~~~~

================================ ========== ===== ===== =========
Task                             Date       From  To    Duration
================================ ========== ===== ===== =========
Starting documentation           2014-01-28 10:10 10:50   00:40  
**Total**                                               **00:40**
================================ ========== ===== ===== =========

Andreas Vogt
~~~~~~~~~~~~

================================ ========== ===== ===== =========
Task                             Date       From  To    Duration
================================ ========== ===== ===== =========
**Total**                                               **00:00**
================================ ========== ===== ===== =========

Bibliography
============

.. _1:

[1]  "libnacl: Python bindings to NaCl",
     https://libnacl.readthedocs.org/en/latest/
     last visited: 2015-01-28

.. _2:

[2]  "NaCl: Networking and Cryptography library",
     http://nacl.cr.yp.to/
     last visited: 2015-01-28

.. _3:

[3]  "Python 3.4.2 Documentation: socket — Low-level networking interface",
     https://docs.python.org/3/library/socket.html
     last visited: 2015-01-28

.. header::

    +-------------+---------------+------------+
    | Title       | Author        | Date       |
    +=============+===============+============+
    | ###Title### | Andreas Vogt  | 2015-01-30 |
    |             | — Jakob Klepp |            |
    +-------------+---------------+------------+

.. footer::

    ###Page### / ###Total###
