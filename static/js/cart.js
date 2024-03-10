 
// setup bucket scoket
const bucketSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/product/'+ user_id +'/bucket/'
);

// on socket open
bucketSocket.onopen = function (e) {
    console.log('bucket socket successfully connected.');
};

// on socket close
bucketSocket.onclose = function (e) { 
    console.log('bucket socket closed unexpectedly');
};

// on receiving message on group
bucketSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const id = data.id;
    const name = data.name;
    const url = data.url;
    const amount = data.amount;
    const img_url = data.img_url;
    const price = data.price;
    
    addProductHtml(id,name,url,amount,img_url,price);
};

function addProductInBucket(id,name,url,amount,img_url,price){

    bucketSocket.send(JSON.stringify({
        'id':id,
        'name': name,
        'url':url,
        'amount':amount,
        'img_url':img_url,
        'price':price
    }));

}

function addProductHtml(id,name,url,amount,img_url,price){

    let card_item_html = `
                        <li id="${id}" class="header-cart-item">
                            <div class="header-cart-item-img">
                            <img src="${img_url}" alt="IMG" />
                            </div>
                            <div class="header-cart-item-txt">
                            <a href="${url}" class="header-cart-item-name">${name}</a>
                            <span class="header-cart-item-info">1 x ${price}</span>
                            </div>
                        </li>
                        `
    $('#cart-bucket').append(card_item_html)

}


