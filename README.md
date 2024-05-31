## Basic morse Encoder/Decoder package you can use with your Python projects

Just add the py file to your project's folder and add an import statement to your project

```
import basic_morse
# rest of your code
# blah blah blah.....
```

There are two main classes: Encoder and Decoder

- Encode
  - def_Encode(string): Encodes and returns the encoded morse of the given string
  - fileEncode(file): Returns a tuple of the encoded and original lines of the file

- Decode
  - def_Decode(string): Decodes morse code and returns the original message (capitalised)
  - fileDecode(file): Decodes entire file line by line and returns tuple of the decoded lines, and original lines
 
Other useful stuff include a character dictionary consisting of characters and their morse translation
which can be accessed using:
```
from basic_morse import charDict
print(charDict)
# blah blah.....
```
