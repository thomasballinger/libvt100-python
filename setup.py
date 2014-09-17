from distutils.core import setup, Extension
import subprocess

# http://code.activestate.com/recipes/502261-python-distutils-pkg-config/
def pkgconfig(*packages, **kw):
    flag_map = {'-I': 'include_dirs', '-L': 'library_dirs', '-l': 'libraries'}
    args = ["pkg-config", "--libs", "--cflags"]
    args.extend(packages)
    for token in subprocess.check_output(args).split():
        token = token.decode('utf-8')
        kw.setdefault(flag_map.get(token[:2]), []).append(token[2:])
    return kw

setup(
    name="vt100",
    version="0.0.1",
    description="an in-memory terminal parsing library",
    author="Jesse Luehrs",
    author_email="doy@tozt.net",
    url="https://github.com/doy/vt100/",
    ext_modules=[
        Extension(
            name="vt100",
            sources=[
                "vt100module.c",
                "libvt100/src/screen.c",
                "libvt100/src/parser.c"
            ],
            **pkgconfig('glib-2.0')
        )
    ],
)