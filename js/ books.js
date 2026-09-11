const cartButtons = document.querySelectorAll(".add-cart");


let cart = JSON.parse(localStorage.getItem("cart")) || [];



cartButtons.forEach(button=>{


button.addEventListener("click",()=>{


const book = {

id: button.dataset.id,

name:
button.closest(".archive-book")
.querySelector("h3")
.textContent,


price:
button.closest(".archive-book")
.querySelector("span")
.textContent


};



cart.push(book);


localStorage.setItem(
"cart",
JSON.stringify(cart)
);



button.innerHTML="Added ✓";


});


});