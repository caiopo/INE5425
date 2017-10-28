from cx_Freeze import setup, Executable

setup(
    name="Simulador",
    version="1",
    executables=[Executable("main.py", base="Win32GUI")],
)
