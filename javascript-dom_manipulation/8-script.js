document.addEventListener('DOMContentLoaded', () => {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
      .then(reponse => reponse.json())
      .then(data => {
        document.querySelector('#hello').textContent = data.hello;
      })
      .catch(error => console.error('Error:', error));
});
