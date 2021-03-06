# REST - API basico en Pyhon
# Por William
# Con el jsonify nos ayuda a recivir y enviar datos en formato json
# Con el request nos ayuda a recibir y enviar datos 
from flask import Flask, jsonify, request
from productos import productos


# app o variable principal 
app = Flask(__name__)


# Ruta princital del home
@app.route('/')
def home():
    return jsonify({"message": "Hola"})

# Ruta para enlistar los productos
@app.route('/productos')
def getProductos():
    return jsonify({"productos": productos, "message": "Lista de productos"})

# Ruta para obtener un producto por el URl
@app.route('/productos/<string:producto_name>')
def getProducto(producto_name):
    #con un ciclo for buscamos el producto dentro de la lista "productos" y con la considion de si es igual al producto_name lo retorne
    productoFound = [productos for productos in productos if productos['name'] == producto_name ]
    if (len(productoFound) > 0 ):
        return jsonify({"Productos": productoFound[0]})

    return jsonify({"message": "Producto no encontrado"})

# Ruta y metodo para agragar un objeto a la lista 
@app.route('/productos', methods=['POST']) 
def addProductos():
    # Con el request recuperamos los datos mandado por el insomnia
    new_Producto = {
        "name": request.json['name'],
        "price": request.json['price'],
        "cantidad": request.json['cantidad']
    }

    # Aqui los agregamos a la lista con el append
    productos.append(new_Producto)
    # Retornamos y mandamos un mensaje y mostralos la lista de productos 
    return jsonify({"message": "Producto agregado sastifacoriamente", "Productos": productos})

# Esta es la ruta para editar la lista
@app.route('/productos/<string:producto_name>', methods=['PUT'])
def editProductos(producto_name):
    # Primero encontramos el obejto que querremos esta es mandado por el URL y se almacena en el product_name
    productoFound = [productos for productos in productos if productos['name'] == producto_name]

    # Veirificamos si el producto encontado es mayor que 0 entonces actualizamos los datos
    # Con ayuda del request actualizamos 
    if(len(productoFound) > 0):
        productoFound[0]['name'] = request.json['name']
        productoFound[0]['price'] = request.json['price']
        productoFound[0]['cantidad'] = request.json['cantidad']

        # Retornamos con un mensaje y con el nuevo produto actualizado
        return jsonify({"message": "Producto actualizado",
        "Producto": productoFound[0] })
    # Si el producto encontradno no es mayor que 0 entonces retornamos un mensaje en formato json con el produot no encontrado 
    return jsonify({"message": "Producto no encontrado"}) 

# Ruta para eliminar un producto
@app.route('/productos/<string:producto_name>', methods=['DELETE'])
def deleteProducto(producto_name):
    
    # Primero encontramos el producto con el ciclo for y lo almacenamos en el productoFound
    productoFound = [productos for productos in productos if productos['name'] == producto_name]
    # Validamos si el producto existe y lo eliminamos con la funcion de remove y el producto que selecionamos con el  productoFound[0]
    if (len(productoFound) > 0):
        productos.remove(productoFound[0])
        # Retornamos un mesaje y imprimimos la lista 
        return jsonify({"message": "Producto eliminado",
        "Producto": productos})
    # Si no se encontro se retorna un mensaje diciendo que no ha sido encontrado 
    return jsonify({"message": "Producto No encontrado"}) 



# Degugueadro principal
if __name__ == '__main__':
    app.run(debug=True, port=4000)