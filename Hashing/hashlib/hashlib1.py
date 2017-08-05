import hashlib

#show hashlib documentation
#print(hashlib.__doc__)

#Show guaranteed hashing algorithms
#h = hashlib.algorithms_guaranteed
#print(h)

#Show available algorithms
#h = hashlib.algorithms_available
#print(h)

# MD5 hashing exemple
# First you have to encode the text to hash into byte literals
#using encode utf-8 function or b''

text = b' This is the text to be hashed'
h = hashlib.new("md5")
h.update(text)
hash_h = h.hexdigest()
print(hash_h)


#you may do this also

#h = hashlib.sha224(b"Nobody inspects the spammish repetition").hexdigest()
#print(h)
