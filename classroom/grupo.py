from classroom.asignatura import Asignatura

class Grupo:

    grado = 'Grado 12'

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        self.grado = Grupo.grado

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=[]):
        if (lista is None):
            self.listadoAlumnos = [alumno]
        else:
            self.listadoAlumnos = lista + [alumno]

    def __str__(self):
        return ('Grupo de estudiantes: {}'.format(self._grupo))


    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    # @ classmethod
    # def asignarNombre(cls, nombre="Grado 4"):
        # cls.grado = nombre

