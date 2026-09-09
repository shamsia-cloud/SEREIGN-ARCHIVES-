const container =
document.getElementById(
"cart-container"
);


let cart =
JSON.parse(
localStorage.getItem("cart")
) || [];



let total=0;



cart.forEach(book=>{


total += book.price;



const item =
document.createElement("div");


item.className="book-card";


item.innerHTML=`

<img src="../${book.cover}">

<h2>
${book.title}
</h2>

<p>
$${book.price}
</p>

`;



container.appendChild(item);


});



document.getElementById("total")
.innerHTML=
"Total: $"+total.toFixed(2);
