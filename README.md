# PyPreCompiler

This script do only one thing. It's simple. You give him a file, 
it will look it up and if it find a line with `#include file.py`
it will copy all the `file.py` to that line.

## Regex

It uses the following regexes to detect things

### Recursion switch

It you switch to recursive mode, it will look into every included file too.

```regex
^-{1,2}[rR](ecursion|ecurson|ecursive)?$
```

### Save to switch

You can specify the saved file's name

```regex
^-{1,2}[sS](ave)?$
```

### Filename

Witch file want to preprocess before running it

```regex
[A-z\*0-9aáöőüűuú/\.]*.py$
```

### The include line

Includes the file if a line founded that matches with this

```regex
^\s*# ?include\s*([A-z\./aáoóöőuúüű0-9]+\.py)\s*$
```

## How to use

```bash
python3 pyCompiler.py compilethis.py -s saveasthis.py -r

```