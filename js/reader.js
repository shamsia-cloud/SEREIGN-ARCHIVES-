const params =
new URLSearchParams(window.location.search);


const bookID =
Number(params.get("id"));



let currentPage = 0;

let pages = [];



fetch("../data/books.json")

.then(res=>res.json())

.then(books=>{


const book =
books.find(item=>item.id===bookID);



if(!book){

document.getElementById("book-title").innerHTML=
"Book Not Found";

return;

}



document.getElementById("book-title").innerHTML=
book.title;



// Temporary page loading

pages=[

"../assets/pages/page1.png",

"../assets/pages/page2.png",

"../assets/pages/page3.png"

];



document.getElementById("page-image").src=
pages[currentPage];


});





const page =
document.getElementById("page");



document.getElementById("next")
.onclick=()=>{


if(currentPage < pages.length-1){

page.classList.add("flip");


setTimeout(()=>{

currentPage++;

document.getElementById("page-image").src=
pages[currentPage];


page.classList.remove("flip");


},500);


}


};





document.getElementById("previous")
.onclick=()=>{


if(currentPage>0){

currentPage--;

document.getElementById("page-image").src=
pages[currentPage];

}


};
