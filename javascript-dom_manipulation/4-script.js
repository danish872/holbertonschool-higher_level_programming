document.querySelector('#add_item').addEventListener('click', () => {
    const ul = document.querySelector('.my_list');
    const list = document.createElement('li');
    list.textContent = 'Item';
    ul.appendChild(list);
});
