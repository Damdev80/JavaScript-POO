class FormaGeometrica {
    // Método abstracto
    calcularArea() {
        throw new Error("Este método debe ser implementado por una subclase");
    }
}

class Cuadrado extends FormaGeometrica {
    constructor(lado) {
        super();
        this.lado = lado;
    }

    calcularArea() {
        return this.lado ** 2;
    }

    showinfo(){
        return `El area de tu Cuadrado es de: ${cuadrado.calcularArea()}`
    }
}

class Circulo extends FormaGeometrica {
    constructor(radio) {
        super();
        this.radio = radio;
    }

    calcularArea() {
        return Math.PI * (this.radio ** 2);
    }

    showinfo(){
        return document.getElementById('text').innerHTML = `<div class="contenido">El area de tu Circulo es de: ${circulo.calcularArea()}</div>`
    }
}

// Crear instancias y calcular áreas
const cuadrado = new Cuadrado(5);
const circulo = new Circulo(4);

function mostrar(){
    cuadrado.showinfo()
    "<br>"
    circulo.showinfo()
}