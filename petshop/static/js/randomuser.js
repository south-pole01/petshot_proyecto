var contenido = document.querySelector('#contenido')
function traer() {
    fetch('https://randomuser.me/api/')
    .then(res => res.json())
    .then(data => {
        console.log(data.results['0'])
        contenido.innerHTML = `
        <img src="${data.results['0'].picture.large}" width="100px" class="img-fluid rounded-circle"> 
        <p>Nombre: ${data.results['0'].name.title} ${data.results['0'].name.first}  ${data.results['0'].name.last}</p>
        <p>Direccion: ${data.results['0'].location.street.number} - ${data.results['0'].location.street.name}</p>
        <p>${data.results['0'].location.city}, ${data.results['0'].location.state}, ${data.results['0'].location.country}</p>
        <p>Codigo postal: ${data.results['0'].location.postcode}</p>
        <p>Edad: ${data.results['0'].dob.age} </p>
        `
    })
} 