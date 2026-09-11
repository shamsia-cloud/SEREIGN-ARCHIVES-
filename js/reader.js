const params =
new URLSearchParams(
window.location.search
);



const bookID =
params.get("id");



const readerFrame =
document.querySelector("#reader-frame");



const books={


1:
"../assets/pdf/48-laws-of-power.pdf",


3:
"../assets/pdf/the-prince.pdf",


5:
"../assets/pdf/meditations.pdf",


7:
"../assets/pdf/art-of-war.pdf"



};



if(readerFrame && books[bookID]){


readerFrame.src =
books[bookID];


}