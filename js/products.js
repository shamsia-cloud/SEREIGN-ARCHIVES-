// ============================
// SEREIGN ARCHIVES
// PRODUCT SYSTEM
// ============================


const productContainer = document.querySelector(".book-grid");


async function loadBooks(){

    if(!productContainer) return;


    try {

        const response = await fetch("../data/books.json");

        const books = await response.json();


        productContainer.innerHTML = "";


        books.forEach(book => {


            const card = document.createElement("article");

            card.className = "book-card";


            card.innerHTML = `

                <img 
                src="${book.cover}" 
                alt="${book.title}"
                >


                <h3>
                ${book.title}
                </h3>


                <p>
                ${book.description}
                </p>


                <div class="price">

                ${
                    book.price === 0
                    ? "Free"
                    : "$" + book.price
                }

                </div>


                <button 
                class="btn book-action"
                data-id="${book.id}"
                >

                ${
                    book.price === 0
                    ? "Read Now"
                    : "Add To Cart"
                }

                </button>


            `;


            productContainer.appendChild(card);


        });



    }

    catch(error){

        console.error(
            "Books loading failed:",
            error
        );

    }


}



loadBooks();