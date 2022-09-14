function fetchProducts(content) {
    fetch(`http://localhost:${PORT || 5000}/api/content/${content}`, {
        "method": "GET",
    })
    .then(response => response.json())
    .then(data => {
        productSelect = document.querySelector('#product')
        productSelect.innerHTML = '<option>Select product</option>'
        for (let product of data) {
            let opt = document.createElement('option');
            opt.value = product;
            opt.innerHTML = product;
            productSelect.appendChild(opt);
        }
    })
    .catch(err => {
        console.error(err);
    });
}


var select = document.querySelector('#contenttype');
select.addEventListener('change',function(){
    let contentType = select.value
    fetchProducts(contentType)
});