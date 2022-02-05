console.log("all good");
function tog(){
    document.body.classList.toggle("dark-theme")
    if (document.getElementById('dark').checked){
        document.getElementById('label').innerHTML = 'Day';
    }else{
        document.getElementById('label').innerHTML = 'Night';
    }
}