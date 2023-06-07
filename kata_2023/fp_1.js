origin_cart = [];


function main(){
    updated_cart = add_item_to_cart(origin_cart, name, price)
    update_dom(updated_cart)
    black_friday_promotion_safe(updated_cart)
}


function add_item_to_cart(cart, name, price){
    cart = push_to_shopping_cart(cart, name, price) // copy-on-write 후 리턴
    calc_cart_total(cart) // 계산
    return cart
}


function update_dom(cart){
    // dom update는 업데이트된 cart를 통해서 업데이트 된다고 가정
    set_cart_total_dom(cart);
    update_shipping_icons(get_buy_buttons_dom(cart));
    update_tax_dom(cart);
}


function push_to_shopping_cart(cart, name, price){
    var shallow_copied_shopping_cart = cart.slice()
    shallow_copied_shopping_cart.push({
        name: name,
        price: price
    })
    return shallow_copied_shopping_cart
}

function black_friday_promotion_safe(cart){
    var cart_copy = deepCopy(cart);
    black_friday_promotion(cart_copy);
    return deepCopy(cart_copy)
}