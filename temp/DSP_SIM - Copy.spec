# widget.spec

# Import necessary modules
from PyInstaller.utils.hooks import collect_all

# Collect all necessary data and hidden imports for matplotlib
#datas, binaries, hiddenimports = collect_all('matplotlib')

# Add the missing DLLs manually

datas, binaries, hiddenimports = collect_all('matplotlib')
pandas_datas, pandas_binaries, pandas_hiddenimports = collect_all('pandas')
numpy_datas, numpy_binaries, numpy_hiddenimports = collect_all('numpy')

datas += pandas_datas + numpy_datas
binaries += pandas_binaries + numpy_binaries
hiddenimports += pandas_hiddenimports + numpy_hiddenimports

hiddenimports += [
    'numpy.f2py',
    'numpy.f2py.crackfortran',
    'numpy.f2py.diagnose',
    'numpy.f2py.f2py2e',
    'numpy.f2py.rules',
    'numpy.f2py.auxfuncs',
]



binaries += [
    ("C:\\Users\\alexi\\miniconda3\\envs\\compile_Qt_files\\Lib\\site-packages\\numpy.libs\\msvcp140-8021418012832a07a8ca5105a33b1086.dll", '.'),  # Adjust the path as necessary
    ("C:\\Users\\alexi\\miniconda3\\envs\\compile_Qt_files\\Lib\\site-packages\\numpy.libs\libscipy_openblas64_-fb1711452d4d8cee9f276fd1449ee5c7.dll", '.'),
    (r"C:\Users\alexi\miniconda3\envs\compile_Qt_files\Lib\site-packages\pandas.libs", "."),  

]

a = Analysis(
    ['..\widget.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True, name='widget', debug=False, bootloader_ignore_signals=False, strip=False, upx=True, upx_exclude=[], runtime_tmpdir=None, console=False)
coll = COLLECT(exe, a.binaries, a.zipfiles, a.datas, strip=False, upx=True, upx_exclude=[], name='widget')
