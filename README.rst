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

Cryptographic library
=====================

We used the python library libnacl.
With it you can create a public and private key(keypar) with following method:

.. code:: python

    bob = libnacl.public.SecretKey()

In the variable bob is now a public and private key. To get only
the public key you can use following method:

.. code:: python

    bob.pk() 

This will return only the public key which can now be used to send it
to Person B. Person B now does the same and Person A has now the public 
key from Person B.

Now Person B can create a new Key which can encrypt and decrypt.
This can be done with the method :

.. code:: python

    Newbox = libnacl.secret.SecretBox()

Now we have to encrypt this key and send it to Person A.
Since Person A has the publickey from Person B and and vice versa we
can simply decrypt the key and encrypt it with following methods.

Person B :

.. code:: python

    B_box = libnacl.public.Box(B.sk, A.pk)
    encr_key = B_box.encrypt(NewBox.sk)

Now we send this to Person A and he can decrypt it since he has the
public key from B.

Person A :

.. code:: python

    A_box = libnacl.public.Box(A.sk, B.pk)
    decr_key = A_box.encrypt(encr_key)
    Newbox = libnacl.secret.SecretBox(decr_key)

Person A can now decrypt messages from Person B with this key 
or encrypt messages and send them to Person B where he can also decrypt them.

Small example with 2 Clients (Bob,Alice)

.. code:: python

    __author__ = 'schueler'
    import libnacl.public
    import libnacl.secret
    import libnacl.utils

    msg = b'But then of course African swallows are not migratory.'
    # This methods creates a keypar(public,private) for the Clients
    bob = libnacl.public.SecretKey()
    alice = libnacl.public.SecretKey()
    # Alice and Bob create a box which is a combination of sender's secret key
    # and the receiver's public key.With this they can encrypt and decrypt messages.
    bob_box = libnacl.public.Box(bob.sk, alice.pk)
    alice_box = libnacl.public.Box(alice.sk, bob.pk)
    # Alice creates a new Key which will we be their shared key
    box = libnacl.secret.SecretBox()
    print(box.sk)
    # Alice encrypts the shared key.
    alice_ctxt = alice_box.encrypt(box.sk)
    print(alice_ctxt)
    # Bob can decrypt the key since he has Alice public key in the 'box'
    aclear = bob_box.decrypt(alice_ctxt)
    print(aclear)
    # Alice encrypts a message with the shared key and send it to Bob
    encr = box.encrypt(msg)
    print(encr)
    #Since Bob decrypted the sharedkey he can now use it  to decrypt
    #the encrypted message from Alice
    box2 = libnacl.secret.SecretBox(aclear)
    decr= box2.decrypt(encr)
    print(decr)

Sniffer
~~~~~~~

In Python you can create a simple Sniffer only with the socket libary.
Example for a simple sniffer:

.. code:: python

    #Packet sniffer in python
    #For Linux
     
    import socket
     
    #create an INET, raw socket
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
     
    # receive a packet
    while True:
      print s.recvfrom(65565)

This will print out no useful information but works.
We used the Code from [4] , since it was written for python 2 we had to update it.
Some braclets were missing and the output had to be decoded. We also added a function
that saved the sniffed data in a file.

Test
====

.. code:: txt
    
    Data : #####
    Data : VáÄ
    Data : ######
    Data : 
    Data : ##
    Data : 
    Data : #####
    Data : C²P´
    Data : ######
    Data : This is a test.

    Data : ######
    Data : #####
    Data : óª

    Data : ######
    Data : 
    Data : ######
    Data : ######
    Data : 



Effort estimate
===============

================================ ========
Task                             Estimate
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
Starting documentation           2015-01-28 10:10 10:50   00:40
Application design (UML)         2015-01-28 19:00 19:50   00:50
Protocol design                  2015-01-29 12:30 13:00   00:30
socket prototyping               2015-01-29 13:00 14:15   01:15
socket chat                      2015-01-29 16:00 17:30   01:30
encryption                       2015-01-29 18:00 20:40   02:40
**Total**                                               **07:25**
================================ ========== ===== ===== =========

Andreas Vogt
~~~~~~~~~~~~

================================ ========== ===== ===== =========
Task                             Date       From  To    Duration
================================ ========== ===== ===== =========
Testing Ptyhon Libary libnacl    2015-01-28 19:00 20:00   01:00
encrypt and decrypt example      2015-01-29 12:00 14:30   02:30
Documentetaion ecrypt decrypt    2015-01-29 15:30 16:45   01:15
Sniffer example                  2015-01-29 16:45 17:15   00:30
Sniffer-Programm                 2015-01-29 17:15 20:15   03:00
**Total**                                               **08:15**
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

.. _4:

[4]  "Code a network packet sniffer in python for Linux"
     http://www.binarytides.com/python-packet-sniffer-code-linux/
     last visited: 2015-01-30

.. header::

    +-------------+---------------+------------+
    | Title       | Author        | Date       |
    +=============+===============+============+
    | ###Title### | Andreas Vogt  | 2015-01-30 |
    |             | — Jakob Klepp |            |
    +-------------+---------------+------------+

.. footer::

    ###Page### / ###Total###
