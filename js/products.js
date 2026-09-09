jfetch("../data/books.json")

.then(response => response.json())

.then(books => {


const container =
document.getElementById("book-container");


books.forEach(book=>{


let card=document.createElement("article");

card.className="book-card";



card.innerHTML=`

<img src="../${book.cover}">


<h2>
${book.title}
</h2>


<p>
${book.author}
</p>


<p class="price">

${book.free ? "FREE" : "$"+book.price}

</p>

${book.free ? 
`
<a 
class="book-button"
href="reader.html?id=${book.id}">
Read Now
</a>
`
:
`
<button 
class="book-button add-cart"
data-id="${book.id}">
Purchase
</button>
`
}


`;



container.appendChild(card);


});


});
