import { Fluidos } from './models/Fluidos.js';


const escolhaContainer = document.querySelector("#escolha");
const btnBomba = document.querySelector(".btn-bomba");
const btnPrensa = document.querySelector(".btn-prensa");
const btnVoltarAoMenu = document.querySelector(".voltar");

//Bomba
const inputDiametro = document.querySelector("#diametro");
const inputSegmentoA = document.querySelector(".segmento-a");
const inputSegmentoB = document.querySelector(".segmento-b");
const inputSegmentoC = document.querySelector(".segmento-c");

//Valores Bomba
const diametroTubo = inputDiametro.value;
const valorSegA = inputSegmentoA.value;
const valorSegB = inputSegmentoB.value;
const valorSegC = inputSegmentoC.value;

//Prensa
const prensaControls = document.querySelector("#prensa-controls");
const prensaImage = document.querySelector(".prensa");
const slideValue = document.querySelector("span");
const inputSlider = document.querySelector("input");

// Valores Prensa
const sliderValue = document.getElementById("range-value").valueAsNumber;
const btnCalcula = document.getElementById('btn-calcula');

function toggleItens(listOfObjects) {
	[...listOfObjects].forEach(objectDOM => objectDOM.classList.toggle("hidden"));
}

btnVoltarAoMenu.addEventListener("click", () => toggleItens([prensaControls, prensaImage, escolhaContainer, btnVoltarAoMenu]))
btnPrensa.addEventListener("click", () => toggleItens([prensaControls, prensaImage, escolhaContainer, btnVoltarAoMenu]));

function sayHello(){
	alert('Hello');
}
btnCalcula.addEventListener('click', () => sayHello());

inputSlider.oninput = (() => {
	let value = inputSlider.value;
	slideValue.textContent = value;
	slideValue.style.left = (value / 2) + "%";
	slideValue.classList.add("show");
});
inputSlider.onblur = (() => {
	slideValue.classList.remove("show");
});


//-----------------------------------------------
const RUGOSIDADE = 0.0015;
const TEMPAGUA = 25.00;












