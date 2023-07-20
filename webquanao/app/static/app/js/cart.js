var addBtns = document.getElementsByClassName('add-cart')

for (i=0; i<addBtns.length;i++){
    addBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId', productId,'action',action)
        console.log('user: ', user)
        if (user === "AnonymousUser"){
            console.log("Người dùng chưa đăng nhập")
        }else{
            addUserOrder(productId,action)
        }
    })
}

function addUserOrder(productId,action){
    console.log('người dùng đã đăng nhập, thêm thành công')
    var url = '/add_cart/'
    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken ,
            

        },
        body: JSON.stringify({'productId':productId,'action':action})
    })
    .then((response)=>{
       return response.json()

    })
    .then((data)=>{
        console.log('data',data)

        location.reload()
        
    })
}