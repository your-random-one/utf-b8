# UTF-B8
I bring you UTF-B8. (why?)\
An encoding "standard" for Unicode.

UTF-B8 is my trap encoding that encodes Unicode characters outside of the BMP as surrogate pairs in UTF-16 then encodes the pair to UTF-8.

For example, U+10000 is encoded as F0 90 80 80 in normal UTF-8, but with my encoding, you take the UTF-16 surrogate pair, D800 DC00 in this case, and encode the pair in UTF-8, which is now ED A0 80 ED B0 80.

**Do not ask.**

So, I made a library for my encoding that can currently validate and encode to UTF-B8.

Please feel free to do anything you need to with this library.
