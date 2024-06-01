# Project

We conducted a rainbow benchmarking repository experiment to compare key sizes, key generation, signature, and verification in rainbow to RSA and DSA in the GPG/PGP standard.

We expected the following: 

- Large key sizes, slower key generation and quick signatures and verification for rainbow
- Faster key generation and comparable signatures and verification for RSA and DSA

## Conclusion

After conducting a rainbow benchmarking repository experiment to compare key sizes, key generation, signature, and verification in rainbow to RSA and DSA in the GPG/PGP standard, we can conlcude that a larger sample should be tested and additional understanding of the GPG/PGP key generation, signature, and verification is needed to accurately assess the data we gathered.

90 keys were analyzed in this data after we created 10 keys for each of the following key types:

1. RSA: 1024, 2048, 3072, 4096
2. DSA: 768, 896, 1024
3. Rainbow Optimized with secret key size: 103648 and public key size: 161600
4. Rainbow Reference with secret key size: 103648 and public key size: 161600

### We expected the following:

- Large key sizes, slower key generation and quick signatures and verification for rainbow
- Faster key generation and comparable signatures and verification for RSA and DSA
Please note that we are assuming an approximate 256 byte size for RSA and DSA keys as the key size data from the RSA and DSA keys was not extracted, and we only had key length to compare.

### Here are our findings:

Our findings show that the amount of time to generate a key for RSA and DSA are comparable using GPG/PGP implementation but unlike our expectations, the data shows that the amount of time to generate rainbow keys was faster than the time it took our program to generate RSA keys. This can be because of many reasons, one being that the GPG/PGP implementation runs other operational requirements during key generation that is not run in the rainbow implementation, and therefore increasing the timestamp for RSA and DSA key generation. We could not find a definitive answer on this topic in GPG/PGP documentation. Our findings show that the large rainbow keys were quicker to generate but like mentioned above, this could be for reasons outside of more efficient key generation time. Additionally, it is worth noting that the optimized version showed a slightly quicker key generation time. Finally, another thing to consider is that the amount of time that it takes to compute geometric and linear algebra, despite its complexity, may be faster than the amount of time that it takes to generate primes, generators, and compute modular exponentiation and inverses

- As a result, the data gathered from key generation is not conclusive
- As expected the rainbow keys showed quick signatures despite their size. Additionally, the optimized version also showed a more efficient signature time, but a wider time range.
- As expected the rainbow keys showed quick verification time despite their size. Additionally, the optimized version also showed a more efficient verification time.
