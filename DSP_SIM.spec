# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_all

runtime_hooks = [r"C:\Users\alexi\OneDrive - Universidad Tecnológica de Panamá\UTP\College Docs\S9\Comunicaciones 1\Lab\GUI_QtCreator\GUI_PCM\temp\fix_sys_stderr.py"]

binaries = [
    ("C:\\Users\\alexi\\miniconda3\\envs\\compile_Qt_files\\Lib\\site-packages\\numpy.libs\\msvcp140-8021418012832a07a8ca5105a33b1086.dll", '.'),  
    ("C:\\Users\\alexi\\miniconda3\\envs\\compile_Qt_files\\Lib\\site-packages\\numpy.libs\libscipy_openblas64_-fb1711452d4d8cee9f276fd1449ee5c7.dll", '.'),
    (r"C:\Users\alexi\miniconda3\envs\compile_Qt_files\Lib\site-packages\pandas.libs", "."),  
    (r'C:\Users\alexi\miniconda3\envs\compile_Qt_files\lib\site-packages\numpy\f2py\*', 'numpy/f2py'),
]

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
