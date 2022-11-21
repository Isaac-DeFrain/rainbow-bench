Topic: Post Quantum Digital Signatures

Overview
Rainbow was one of three finalists in the NIST project to standardize quantum-safe digital signatures. The Rainbow cryptosystem is based on the [unbalanced oil and vinegar scheme](https://en.wikipedia.org/wiki/Unbalanced_oil_and_vinegar_scheme), which has a large public key, but smaller signatures.

Rainbow did not make the cut, as there is a server [vulnerability](https://research.ibm.com/publications/breaking-rainbow-takes-a-weekend-on-a-laptop) in the Rainbow algorithm, opening it up to a classical attack able to break the system. It would be possible to fix Rainbow by changing the parameters, but this would significantly increase the key sizes and slow down the signing and verification algorithms, which would make Rainbow less efficient than the simpler oil and vinegar scheme that Rainbow was based on.

Our goals for this project are the following:
1. Evaluate a Rainbow implementation
2. Demonstrate a successful attack on Rainbow
3. Compare the relative times and sizes for with other Signature Algorithms

To do this we will do the following
1. Create example keys, digital signatures, and verification using [Rainbow](https://github.com/fast-crypto-lab/rainbow-submission-round2/tree/master/Optimized_Implementation/amd64)
2. Demonstrate a [successful attack on Rainbow](https://github.com/WardBeullens/BreakingRainbow)
3. Compare 100+ the rainbow-genkey, rainbow-sign, rainbow-verify, and pk and sk sizes with the corresponding parts for the signature algorithms available in [GPG](https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key): RSA, ElGamal, DSA, ECDH, ECDSA, EdDSA
    a. Write a [file](https://www.gnupg.org/documentation/manuals/gnupg/Unattended-GPG-key-generation.html) that generates all GPG parameters 
4. [Benchmark](www.realpythonproject.com/how-to-benchmark-functions-in-python/) these different signature schemes with 100+ examples

Learn more about [Breaking Rainbow](https://www.youtube.com/watch?v=67ATqQVWgLw) and a [Github GPG Overview](https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key)