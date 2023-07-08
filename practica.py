class ListaInteractiva:
    def __init__(self):
        self.lista = []

    def agregar_elemento(self, elemento):
        self.lista.append(elemento)
        print(f"Se agregó el elemento {elemento} a la lista.")

    def agregar_varios_elementos(self, elementos):
        self.lista.extend(elementos)
        print("Se agregaron los elementos:", elementos, "a la lista.")

    def insertar_elemento(self, posicion, elemento):
        self.lista.insert(posicion, elemento)
        print(f"Se insertó el elemento {elemento} en la posición {posicion}.")

    def eliminar_elemento(self, elemento):
        self.lista.remove(elemento)
        print(f"Se eliminó el elemento {elemento} de la lista.")

    def eliminar_por_indice(self, indice):
        elemento = self.lista.pop(indice)
        print(f"Se eliminó el elemento {elemento} en la posición {indice}.")

    def buscar_elemento(self, elemento):
        indice = self.lista.index(elemento)
        print(f"El elemento {elemento} se encuentra en la posición {indice}.")

    def contar_elemento(self, elemento):
        conteo = self.lista.count(elemento)
        print(f"El elemento {elemento} aparece {conteo} veces en la lista.")

    def ordenar_lista(self):
        self.lista.sort()
        print("La lista se ha ordenado de forma ascendente.")

    def invertir_lista(self):
        self.lista.reverse()
        print("La lista se ha invertido.")

    def copiar_lista(self):
        lista_copia = self.lista.copy()
        print("Se ha realizado una copia de la lista.")
        return lista_copia

    def limpiar_lista(self):
        self.lista.clear()
        print("Se han eliminado todos los elementos de la lista.")

    def mostrar_lista(self):
        print("Lista actual:", self.lista)


# Función principal
def interactuar_con_lista():
    lista_interactiva = ListaInteractiva()

    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar elemento")
        print("2. Agregar varios elementos")
        print("3. Insertar elemento")
        print("4. Eliminar elemento")
        print("5. Eliminar por índice")
        print("6. Buscar elemento")
        print("7. Contar elemento")
        print("8. Ordenar lista")
        print("9. Invertir lista")
        print("10. Copiar lista")
        print("11. Limpiar lista")
        print("12. Mostrar lista")
        print("13. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            elemento = input("Ingrese el elemento a agregar: ")
            lista_interactiva.agregar_elemento(elemento)
        elif opcion == 2:
            elementos = input("Ingrese los elementos separados por comas: ").split(",")
            lista_interactiva.agregar_varios_elementos(elementos)
        elif opcion == 3:
            posicion = int(input("Ingrese la posición: "))
            elemento = input("Ingrese el elemento a insertar: ")
            lista_interactiva.insertar_elemento(posicion, elemento)
        elif opcion == 4:
            elemento = input("Ingrese el elemento a eliminar: ")
            lista_interactiva.eliminar_elemento(elemento)
        elif opcion == 5:
            indice = int(input("Ingrese el índice a eliminar: "))
            lista_interactiva.eliminar_por_indice(indice)
        elif opcion == 6:
            elemento = input("Ingrese el elemento a buscar: ")
            lista_interactiva.buscar_elemento(elemento)
        elif opcion == 7:
            elemento = input("Ingrese el elemento a contar: ")
            lista_interactiva.contar_elemento(elemento)
        elif opcion == 8:
            lista_interactiva.ordenar_lista()
        elif opcion == 9:
            lista_interactiva.invertir_lista()
        elif opcion == 10:
            lista_copia = lista_interactiva.copiar_lista()
            print("Copia de la lista:", lista_copia)
        elif opcion == 11:
            lista_interactiva.limpiar_lista()
        elif opcion == 12:
            lista_interactiva.mostrar_lista()
        elif opcion == 13:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


interactuar_con_lista()