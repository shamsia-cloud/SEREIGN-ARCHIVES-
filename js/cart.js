function getCart(){

return JSON.parse(
localStorage.getItem("cart")
) || [];

}



function saveCart(cart){

localStorage.setItem(
"cart",
JSON.stringify(cart)
);

}



document.addEventListener(
"click",
function(e){


if(e.target.classList.contains("add-cart")){


const id =
Number(e.target.dataset.id);



fetch("../data/books.json")

.then(res=>res.json())

.then(books=>{


const book =
books.find(
item=>item.id===id
);



let cart=getCart();



cart.push(book);



saveCart(cart);



alert(
book.title+" added to cart"
);



});


}


});
