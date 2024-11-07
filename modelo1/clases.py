class Nodo:
    def __init__(self, data,siguiente=None):
        self.data = data
        self.siguiente = siguiente  # Apunta al siguiente nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_usuario(self,data):
        nuevo_nodo = Nodo(data)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def listar_usuarios(self):
        actual = self.cabeza
        while actual:
            yield actual.data
            actual = actual.siguiente

class Error:
    def __init__(self):
        self.error = None

    def error_1(self,v):
            errores = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')',
                       '*',
                       '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '{', '|',
                       '}',
                       '~']
            for i in v:
                if i in errores:
                    raise ValueError("El campo solo debe contener letras")
                break
    def error_2(self,v):
        errores=["@","."]
        for i in v:
            if i not in errores:
                raise ValueError("El campo debe ser un email :Debe incluir @ y .")
    def error_3(self,v):
        if v.upper() == "FEMENINO" or v.upper() == "MASCULINO":
            return self.error
        else:
            raise ValueError("El campo debe contener :Masculino o Femenino")
    def error_4(self,v):
        int(v)


class Organizar:
    def __init__(self):
        self.orden = None
    def organizar_lis(self,data):
        lista=[]
        usuario=data.cabeza
        print(data.cabeza)
        print(usuario)
        while usuario:
            lista.append(usuario.data)
            usuario=usuario.siguiente
        return lista


    def quicksort(self, array, sel):
        if len(array) <= 1:
            return array
        pivot = getattr(array[len(array) // 2], sel)

        left = [x for x in array if getattr(x, sel) < pivot]
        middle = [x for x in array if getattr(x, sel) == pivot]
        right = [x for x in array if getattr(x, sel) > pivot]
        return self.quicksort(left, sel) + middle + self.quicksort(right, sel)
