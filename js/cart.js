// ============================
// CART SYSTEM
// ============================


let cart = JSON.parse(
    localStorage.getItem("sereignCart")
)
|| [];





function saveCart(){

    localStorage.setItem(
        "sereignCart",
        JSON.stringify(cart)
    );

}




document.addEventListener(
"click",
function(e){


    if(
        e.target.classList.contains("book-action")
    ){


        const id =
        e.target.dataset.id;



        fetch("../data/books.json")

        .then(res=>res.json())

        .then(books=>{


            const book =
            books.find(
            item=>item.id == id
            );


            if(book.price > 0){


                cart.push(book);


                saveCart();


                alert(
                `${book.title} added to cart`
                );


            }


            else {


                window.location.href =
                `reader.html?id=${id}`;


            }


        });


    }


});





function displayCart(){


const container =
document.querySelector(".cart-items");


if(!container)
return;



container.innerHTML="";



let total = 0;



cart.forEach(item=>{


total += item.price;



container.innerHTML += `


<div class="cart-item">


<h3>
${item.title}
</h3>


<p>
$${item.price}
</p>


</div>


`;


});



const totalBox =
document.querySelector(
".checkout-total"
);


if(totalBox){

totalBox.innerHTML =
`Total: $${total}`;

}



}



displayCart();