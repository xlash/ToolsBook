Customer Master Keys
	Top of key hierarchy
	Non-exportable

	1. Encryption/Data Keys (wrapped in CMK)

[++] Context is important. Original filename is preserved for decryption
	Contextualizing the encryption, will force to pass back the same context at decrypt.
		It acts as a second layer of protection, which acts as a field that shouldn't be controlled externally. You change the request parameter, and are able to request another resource, wrong context, you are out.
		Cloudwatch can monitor for incorrect context use.
		Also useful to protect against incorrect dev code (off by one by mistake)


Plaintext is limuted to 4096 bytes

"Envelope Encryption" with KMS
	Limited-scope data key for client-side encryption
	Key must be kept with the data

	==> Limits calls to KMS, regardless of data size (1GB vs 4096 bytes)

Data Format
	contains context on how to decrypt except the key

Key rings will be available in the future to replace Master Key Providers
	Can use KMS master key provider

Data Key Caching
	Lower latency
	sec/perf tradeoff
	[-] Missing audit logs
	[-] Only works on identical context and keys
	[-] Greater potential impact if a key is compromised
	AWS KMS TPS limits can be raised (if that is the reason to use Key Caching.)