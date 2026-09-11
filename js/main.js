// Mobile navigation

const menuButton = document.querySelector(".menu-toggle");
const navLinks = document.querySelector(".nav-links");


if(menuButton){

menuButton.addEventListener("click",()=>{

navLinks.classList.toggle("active");

});

}



// Smooth scrolling

document.querySelectorAll("a[href^='#']").forEach(link=>{

link.addEventListener("click",function(e){

e.preventDefault();

document.querySelector(this.getAttribute("href"))
.scrollIntoView({
behavior:"smooth"
});

});

});



// Floating particles

const particleContainer = document.createElement("div");

particleContainer.className="particles";

document.body.appendChild(particleContainer);



for(let i=0;i<40;i++){

let particle=document.createElement("span");

particle.className="particle";


particle.style.left=Math.random()*100+"%";

particle.style.animationDelay=Math.random()*10+"s";

particle.style.animationDuration=
(5+Math.random()*10)+"s";


particleContainer.appendChild(particle);

}