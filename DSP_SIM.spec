#This file is to be meant to compile this project into an executable file using pyinstaller.



import sys
import os
from PyInstaller.utils.hooks import collect_all

# Use a path relative to this spec file so it works on any machine
_here = os.path.dirname(os.path.abspath(SPEC))
runtime_hooks = [os.path.join(_here, 'temp', 'fix_sys_stderr.py')]

# Binaries differ per platform; let PyInstaller resolve them automatically on Linux/macOS
if sys.platform == 'win32':
    import glob as _glob
    import sysconfig as _sysconfig
    _sp = _sysconfig.get_path('purelib')  # e.g. .../site-packages
    _numpy_libs = os.path.join(_sp, 'numpy.libs')
    _win_dlls = _glob.glob(os.path.join(_numpy_libs, '*.dll'))
    binaries = [(dll, '.') for dll in _win_dlls]
else:
    binaries = []

a = Analysis(
    ['widget.py'],
    pathex=[],
    binaries=binaries,
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=runtime_hooks,
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='DSP_SIM',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='DSP_SIM',
)
