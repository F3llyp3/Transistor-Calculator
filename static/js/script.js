function mostrarCampos() {
    const calculo = document.getElementById("calculo").value;
    const campos = document.querySelectorAll(".campo");

    campos.forEach(campo => {
        campo.style.display = "none";
        campo.style.opacity = "0";
    });

    if (calculo === "ib") {
        document.getElementById("vcc").parentElement.style.display = "block";
        document.getElementById("rb").parentElement.style.display = "block";
    } else if (calculo === "ic") {
        document.getElementById("vcc").parentElement.style.display = "block";
        document.getElementById("rb").parentElement.style.display = "block";
        document.getElementById("beta").parentElement.style.display = "block";
    } else if (calculo === "vce") {
        document.getElementById("vcc").parentElement.style.display = "block";
        document.getElementById("rb").parentElement.style.display = "block";
        document.getElementById("beta").parentElement.style.display = "block";
        document.getElementById("rc").parentElement.style.display = "block";
    }

    setTimeout(() => {
        campos.forEach(campo => campo.style.opacity = "1");
    }, 100);
}
