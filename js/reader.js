// ============================
// READER SYSTEM
// ============================


const readerContainer =
document.querySelector(".reader-content");



async function loadReader(){


if(!readerContainer)
return;



const params =
new URLSearchParams(
window.location.search
);



const id =
params.get("id");



const response =
await fetch("../data/books.json");



const books =
await response.json();



const book =
books.find(
item=>item.id == id
);



if(!book){

readerContainer.innerHTML=
"<h2>Book not found</h2>";

return;

}



readerContainer.innerHTML = `


<h1>
${book.title}
</h1>


<p>
${book.description}
</p>



${
book.pdf

?

`

<iframe

src="${book.pdf}"

width="100%"

height="700px"

>

</iframe>

`

:

`

<p>
Premium summary edition.
</p>

<a class="btn"
href="${book.reader}"
target="_blank">

Open Reader

</a>

`

}



`;



}



loadReader();