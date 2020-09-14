def calcular_almacenamiento(filesize):
    # Primer git, implementado en master
    block_size = 4096
    # Division exacta para obtener los bloques llenos
    full_blocks = filesize // block_size
    # Modulo para obtener el bloque parcial
    partial_block = filesize % block_size
    # Dependiendo si queda algo del bloque parcial, se le aumenta un bloque mas
    if partial_block > 0:
        return (full_blocks + 1) * block_size
    return full_blocks * block_size


if __name__ == '__main__':
    tamano = int(input('Ingrese el tamano del archivo: '))

    print('El tamano de los bloques es {tamano}'.format(tamano=calcular_almacenamiento(tamano)))

