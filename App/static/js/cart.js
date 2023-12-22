function addToCart(id, name, price) {
    fetch('/api/cart', {
        method: 'post',
        body: JSON.stringify ({
            "id": id,
            "name": name,
            "price": price
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function(res) {
        return res.json();
    }).then(function(data) {
        let items = document.getElementsByClassName("cart-counter");
        for (let item of items)
            item.innerText = data.total_quantity
    });
}

function updateCart(id, obj) {
    obj.disabled = true;
    fetch(`/api/cart/${id}`, {
        method: 'put',
        body: JSON.stringify ({
            "quantity": obj.value
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function(res) {
        return res.json();
    }).then(function(data) {
        obj.disabled = false;
        let items = document.getElementsByClassName("cart-counter");
        let amounts = document.getElementsByClassName("cart-amount");
        for (let item of items)
            item.innerText = data.total_quantity

        for (let item of amounts)
            item.innerText = data.total_amount
    });
}

function deleteCart(id, obj) {
    obj.disabled = true;
    if(confirm("Bạn chắc chắn xóa không?") === true) {
        fetch(`/api/cart/${id}`, {
            method: 'delete'
        }).then(function(res) {
            return res.json();
        }).then(function(data) {
            obj.disabled = false;
            let items = document.getElementsByClassName("cart-counter");
            let amounts = document.getElementsByClassName("cart-amount");

            for (let item of items)
                item.innerText = data.total_quantity

             for (let item of amounts)
                item.innerText = data.total_amount

            let d = document.getElementById(`product${id}`);
            d.style.display = "none";
        });
    }
}
