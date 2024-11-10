class Nodo:
    def __init__(self, data,siguiente=None):
        self.data = data
        self.siguiente = siguiente

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
                    raise Exception("El email")
                break
            return self.error
    def error_2(self,v):
        errores=["@","."]
        con = 0
        punto=0
        if v[0]=="@" or v[0]==".":
            raise Exception("El email no debe tener parte local :Ejemplo ParteLocal@gmail.com ")
        if len(v)<5:
            raise Exception("El campo solo debe contener letras")
        elif len(v)>=5:
            for i in v:
                if i not in errores:
                    con+=1
                    punto=0
                if i==".":
                    punto+=1
                    if punto==2:
                        break
            if con>=2:
                return  self.error
            elif punto==2:
                raise Exception("Error de escritura")
            else:
                raise Exception("El campo debe ser un email :Debe incluir @ y .")

    def error_3(self,v):
        if v.upper() == "FEMENINO" or v.upper() == "MASCULINO":
            return self.error
        else:
            raise Exception("El campo debe contener :Masculino o Femenino")

    def error_4(self,v):
        try:
            int(v)
        except ValueError :
            raise ValueError()
        else:
            return self.error


class Organizar:
    def __init__(self):
        self.orden = []
    def organizar_lis(self,data):
        lista=[]
        usuario=data.cabeza
        if usuario:
            while usuario:
                lista.append(usuario.data)
                usuario = usuario.siguiente
            return lista
        else:
            return self.orden


    def quicksort(self, array, sel):
        if len(array) <= 1:
            return array
        pivot = getattr(array[len(array) // 2], sel)
        left = [x for x in array if getattr(x, sel) < pivot]
        middle = [x for x in array if getattr(x, sel) == pivot]
        right = [x for x in array if getattr(x, sel) > pivot]
        return self.quicksort(left, sel) + middle + self.quicksort(right, sel)
