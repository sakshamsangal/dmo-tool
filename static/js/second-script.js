function fetchProducts(content) {
    fetch(`http://localhost:${PORT || 5000}/api/content/${content}`, {
        "method": "GET",
    })
    .then(response => response.json())
    .then(data => {
        productSelect = document.querySelector('#product');
        productSelect.innerHTML = '<option>Select product</option>';
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

function uploadUrl(type, url) {
    let sendObj = {}
    product_name = document.querySelector('#product').value
    sendObj[type] = url
    sendObj = {...sendObj, product_name}
    fetch(`http://localhost:${PORT || 5000}/api/upload-url`, {
        body: JSON.stringify(sendObj),
        headers: {
            "Content-Type": "application/json",
        },
        method: "post",
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success: ', data);
    })
    .catch(err => {
        console.error(err);
    });
//    console.log({type: url});
}

var select = document.querySelector('#content-type');
select.addEventListener('change',function(){
    let contentType = select.value;
    fetchProducts(contentType);
});


var xmlBtn = document.querySelector('#xml-submit');
var pdfBtn = document.querySelector('#pdf-submit');
var chkptBtn = document.querySelector('#chkpt-submit');

xmlBtn.addEventListener('click', function(){
    let url = document.querySelector('#xml-url').value;
    uploadUrl('xml_url', url);
})

pdfBtn.addEventListener('click', function(){
    let url = document.querySelector('#pdf-url').value;
    uploadUrl('pdf_url', url);
})

chkptBtn.addEventListener('click', function(){
    let url = document.querySelector('#chkpt-url').value;
    uploadUrl('online_url', url);
})

