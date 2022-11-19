Topic: Post Quantum Digital Signatures

Overview
Rainbow was one of three finalists in the NIST project to standardize quantum-safe digital signatures. The Rainbow cryptosystem is based on the unbalanced oil and vinegar scheme (https://en.wikipedia.org/wiki/Unbalanced_oil_and_vinegar_scheme), which has a large public key, but smaller signatures.

Rainbow did not make the cut, as there is a server vulnerability in the Rainbow algorithm, opening it up to a classical attack able to break the system. It would be possible to fix Rainbow by changing the parameters, but this would significantly increase the key sizes and slow down the signing and verification algorithms, which would make Rainbow less efficient than the simpler oil and vinegar scheme that Rainbow was based on. (https://research.ibm.com/publications/breaking-rainbow-takes-a-weekend-on-a-laptop)

See: https://www.youtube.com/watch?v=67ATqQVWgLw and [Github GPG Overview](https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key)`````

Our goals:
Create example digital signatures using oil-and-vinegar and Rainbow
Demonstrate a successful attack on Rainbow
Compare the relative times and sizes for with other Signature Algorithms
