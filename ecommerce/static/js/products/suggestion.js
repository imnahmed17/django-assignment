const searchInput = document.getElementById('searchInput');
const suggestionsDiv = document.getElementById('suggestions');

searchInput.addEventListener('input', () => {
    const query = searchInput.value;
    if (query.length >= 3) {
        fetch(`/products/get_product_name_suggestions/?query=${query}`)
            .then(response => response.json())
            .then(data => {
                suggestionsDiv.innerHTML = '';
                data.suggestions.forEach(suggestion => {
                    const li = document.createElement('li');
                    const hr = document.createElement('hr');

                    li.classList.add('px-4', 'py-2.5', 'cursor-pointer', 'hover:bg-blue-100', 'flex', 'items-center');
                    li.textContent = suggestion;

                    suggestionsDiv.appendChild(li);
                    suggestionsDiv.appendChild(hr);

                    li.addEventListener('click', () => {
                        searchInput.value = suggestion;
                        suggestionsDiv.innerHTML = '';
                    });
                });
            });

        suggestionsDiv.classList.remove('hidden');
    } else {
        suggestionsDiv.innerHTML = '';
        suggestionsDiv.classList.add('hidden');
    }
});

document.addEventListener('click', event => {
    if (!searchInput.contains(event.target) && !suggestionsDiv.contains(event.target)) {
        suggestionsDiv.innerHTML = '';
        suggestionsDiv.classList.add('hidden');
    }
});