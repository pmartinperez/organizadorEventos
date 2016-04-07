from setuptools import setup


setup(name="Organizador de Eventos",
      version="0.1",
      description="Programa que ayuda a organizado eventos de distinto tipo",
      author="Patricia Martin Perez",
      author_email="pmartinperez@danielcastelao.org",
      url="http://www.patriciamape.com",
      license="GPL",
      scripts=["vPrincipal.py"],
      py_modules=["vCrearRegistro", "vEvento","conexionBD", "crearTablas", "Menu", "vCrearEvento", "vMensaje", "vTabla"],
      #packages = ["instalacion", "informes", "html"],
      #package_data = {"instalacion" : "setup.py"}
)