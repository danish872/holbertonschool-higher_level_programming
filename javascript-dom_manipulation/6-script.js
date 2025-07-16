fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(reponse => reponse.json())
  .then(data => {
    document.querySelector('#character').textContent = data.name;
  })
  .catch(error => console.error('Error:', error));
