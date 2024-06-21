function replaceImages() {
  console.log("hello");
  let images = document.getElementById("Catyawning");
  let text = document.createTextNode(images.alt);
  images.parentNode.replaceChild(text, images);
}

function replaceImages1() {
  console.log("hello");
  let images = document.getElementById("Catwithhat");
  let text = document.createTextNode(images.alt);
  images.parentNode.replaceChild(text, images);
}

const insertNewElement = () => {
  let newDiv = document.createElement("div"); // this creates a new div element
  newDiv.innerHTML = "This is a newly created div!";
  newDiv.className = "alpha added";

  let parentDiv = document.getElementById("parent-div");
  if (parentDiv) {
    parentDiv.appendChild(newDiv); // this attaches our new div element into the DOM, by nesting it under an existing element
  }
};

function featureImage1() {
  var img = document.getElementById("Catyawning");
  img.classList.remove("show");
  img.classList.add("fade");
  setTimeout(function () {
    img.src =
      "https://cdn.britannica.com/70/234870-050-D4D024BB/Orange-colored-cat-yawns-displaying-teeth.jpg";
    img.classList.remove("fade");
    img.classList.add("show");
  }, 500);
}

function featureImage2() {
  var img = document.getElementById("Catwithhat");
  img.classList.remove("show");
  img.classList.add("fade");
  setTimeout(function () {
    img.src =
      "https://i.etsystatic.com/10692466/r/il/619b56/1783519511/il_570xN.1783519511_l5sk.jpg";
    img.classList.remove("fade");
    img.classList.add("show");
  }, 500);
}

function featureImage3() {
  var img = document.getElementById("sleepycat");
  img.classList.remove("fade");
  setTimeout(function () {
    img.src =
      "https://i.etsystatic.com/10692466/r/il/619b56/1783519511/il_570xN.1783519511_l5sk.jpg";
    img.classList.remove("fade");
  }, 500);
}
