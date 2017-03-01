Layout: post
Title: GnuPG key transition statement
Date: 2014-05-15 22:33:39 -0600
Comments: true
Github_issue_id: 23
Tags: gpg, security

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA1,SHA512

I am transitioning GPG keys from an old 1024-bit DSA key to a new
4096-bit RSA key.  The old key will continue to be valid for some time,
but I prefer all new correspondence to be encrypted to the new key, and
will be making all signatures going forward with the new key.

This transition document is signed with both keys to validate the
transition.

If you have signed my old key, I would appreciate signatures on my new
key as well, provided that your signing policy permits that without
re-authenticating me.

The old key, which I am transitioning away from, is:

  pub   1024D/0x41E5C23F0F8E76D6 [created: 2004-10-14]
    Key fingerprint = FE97 560A 1C17 F268 1A20  5B80 41E5 C23F 0F8E 76D6

The new key, to which I am transitioning, is:

  pub   4096R/0xC139E10FD9F20FC1 [created: 2014-05-16]
    Key fingerprint = 7DFA 4AEF AC15 8BFC 151D  2DD8 C139 E10F D9F2 0FC1

To fetch the full new key from a public key server using GnuPG, run:

  gpg --keyserver keys.gnupg.net --recv-key 0xC139E10FD9F20FC1

If you have already validated my old key, you can then validate that the
new key is signed by my old key:

  gpg --check-sigs 0xC139E10FD9F20FC1

If you then want to sign my new key, a simple and safe way to do that is
by using caff as follows:

  caff 0xC139E10FD9F20FC1

Please contact me via e-mail at &lt;bd808@bd808.com&gt; if you have any
questions about this document or this transition.

Bryan Davis
&lt;bd808@bd808.com&gt;
2014-05-15

-----BEGIN PGP SIGNATURE-----

iEYEARECAAYFAlN1m3cACgkQQeXCPw+OdtYXEwCfXUThM0JsPacy1bCBQ6rZpWRY
dAcAoIMg91zhQlgo2DJCu3o9BUzCqEJuiQIcBAEBCgAGBQJTdZt3AAoJEEhMmO+k
BO60xv0QAJEV8VYVqpIdEoZWRYw6sGJVmkTCs2rC4OC68/W+1e41hgPqE+i+6ACU
2MhwusMQhsBu1QpyeWXTOEPMU4rvwwlMeQnIlg+DEFGn2k3qJfxeYooO1Ni9n0US
fb676RByWnaAZUYPebNrmTvk5bv/M5BSU8XDfPmDsFk5hzeOa1j1kw9Loffr74LL
LJozHb8Uj9fMZj1f8SzqlhyqPVUWqF3AEE3Dl14Wl2FH507ZzpMwuOetj65KxeiJ
Iee2Hhu6TvQcqs6erxMrsVFxuYz9s1eJzo7feEL22Z8Nm46KSF6x43lpt8ebiKDU
zxzdjLBRQOYf3KcCHE2HvbGxPqEfKkwmCJcd1a3Bd/7sgPXrKsJbeCg8LD2x8aTT
DHGXUEVbMv8r3qMAlKXxJ8iBJ9AvdG0nKneVJ8gB6YkCPlSuDlh2bL3CrMPQ5Db+
vtI0EwuGHSMocWX5cns3t31/iWdoOJ/8lvXJoauT+TVmenmhQ0mU71+whVlnahhr
fhKqsZHM4Nryve8LOntndzAIRUK9EZom1ZGfxzEgfgheg0boMfbk9+dS38zVxjmx
EZ4JuTVvAUv4ZgG553JaKed278wNPxdXSqaXggV+HAceFkaW80M6uQhvOCXX+T05
1HCfl3sQmGkYZ1f3DPrcur0jm+PkHPB4Jw29wogBFU0d7dDJQ0qv
=l8Kz
-----END PGP SIGNATURE-----
```