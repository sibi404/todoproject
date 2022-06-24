// function tog(){
//     document.body.classList.toggle("dark-theme")
//     if (document.getElementById('dark').checked){
//         document.getElementById('label').innerHTML = 'Day';
//     }else{
//         document.getElementById('label').innerHTML = 'Night';
//     }
// }

const body = document.querySelector("body");
const darkMode = document.getElementById('dark-button');
const button = document.getElementById('dark-button');
// const taskCard = document.getElementById("task-card");
function tog(){
    if (body.classList.contains('dark-theme')){
        body.classList.remove('dark-theme');
        localStorage.setItem("theme","light");
        button.innerHTML = 'Night';
        darkMode.style.backgroundColor = "#222831";
    }else{
        body.classList.add('dark-theme');
        button.innerHTML = 'Day';
        darkMode.style.backgroundColor = "whitesmoke";
        localStorage.setItem("theme","dark");
    }
}
if (localStorage.getItem("theme") === "dark"){
    body.classList.add("dark-theme");
    darkMode.style.backgroundColor = "whitesmoke";
    button.innerHTML = 'Day';
}