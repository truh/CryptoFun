__author__ = 'schueler'
import libnacl.public
import libnacl.secret
import libnacl.utils

# Define a message to send

# Generate the key pairs for Alice and bob, if secret keys already exist
# they can be passed in, otherwise new keys will be automatically generated
msg = b'But then of course African swallows are not migratory.'
# Create a SecretBox object, if not passed in the secret key is
# Generated purely from random data
bob = libnacl.public.SecretKey()
alice = libnacl.public.SecretKey()
bob_box = libnacl.public.Box(bob.sk, alice.pk)
alice_box = libnacl.public.Box(alice.sk, bob.pk)
box = libnacl.secret.SecretBox()
print(box.sk)
alice_ctxt = alice_box.encrypt(box.sk)
print(alice_ctxt)
aclear = bob_box.decrypt(alice_ctxt)
print(aclear)
encr = box.encrypt(msg)
print(encr)
box2 = libnacl.secret.SecretBox(aclear)
decr= box2.decrypt(encr)
print(decr)
