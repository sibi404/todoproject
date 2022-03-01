// function tog(){
//     document.body.classList.toggle("dark-theme")
//     if (document.getElementById('dark').checked){
//         document.getElementById('label').innerHTML = 'Day';
//     }else{
//         document.getElementById('label').innerHTML = 'Night';
//     }
// }

const body = document.body;
function tog(){
    if (body.classList.contains('dark-theme')){
        body.classList.remove('dark-theme');
        localStorage.setItem("theme","light");
        document.getElementById('label').innerHTML = 'Night';
    }else{
        body.classList.add('dark-theme');
        localStorage.setItem("theme","dark-theme");
        document.getElementById('label').innerHTML = 'Day';
    }
}
if (localStorage.getItem("theme") === "dark-theme"){
        body.classList.add("dark-theme");
        document.getElementById('label').innerHTML = 'Day';
    }