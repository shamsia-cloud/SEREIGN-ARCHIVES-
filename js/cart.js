const cartContainer =
document.querySelector(".cart-container");


function loadCart(){


if(!cartContainer) return;



let cart =
JSON.parse(localStorage.getItem("cart")) || [];



if(cart.length===0){

cartContainer.innerHTML=
`
<p>
Your archive is empty.
</p>
`;

return;

}



cartContainer.innerHTML="";



cart.forEach((item,index)=>{


const card=document.createElement("article");


card.className="cart-item";


card.innerHTML=
`

<h3>${item.name}</h3>

<p>
${item.price}
</p>


<button onclick="removeItem(${index})">
Remove
</button>


`;


cartContainer.appendChild(card);



});


}



function removeItem(index){


let cart=
JSON.parse(localStorage.getItem("cart")) || [];


cart.splice(index,1);


localStorage.setItem(
"cart",
JSON.stringify(cart)
);


loadCart();


}



loadCart();