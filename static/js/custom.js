

function send_comment(product_id) {
    let hidden_input = $('#set-parent-comment').val()
    let text = $('#commentbody').val()
    $.get('/products/send-comment/', {
        'text' : text ,
        'product_id' : product_id ,
        'parent_id' : hidden_input
    }).then(
        response => {
            location.reload()
        }
    )
}


function parent_set(comment_id) {
    let name_user = $('#name-user').html()
    let text_comment = $('#text-comment')
    let hidden_input = $('#set-parent-comment')
    hidden_input.val(comment_id)
    text_comment.html(`پاسخ خود را برای ${name_user} بنویسید`)
}











function check_count() {
    let input = document.querySelector('#product-count').value
    let count = parseInt(input.value)
    if (parseInt(count) < 1) {
        input.value = 1
        input.style.border = '1px solid red'
        alert('تعداد محصول نمیتواند کمتر از یک باشد')
    }
}


function add_to_order(product_id) {
    let count = document.querySelector('#product-count').value
    $.get('/order/add-to-order/', {
        'product_id': product_id,
        'count': count
    }).then(response => {
        if (response.status === 'not-login') {
            Swal.fire({
                title: "ابتدا وارد حساب کاربری شوید",
                confirmButtonText: "باشه",
            }).then((result) => {
                if (result.isConfirmed) {
                    location.href = '/users/login'
                }
            });
        } else if (response.status === 'success') {
            Swal.fire({
                position: "center",
                icon: "success",
                title: "محصول با موفقیت به سبد خرید اضافه شد",
                showConfirmButton: false,
                timer: 1500
            })
        } else if (response.status === 'error-count') {
            Swal.fire({
                position: "center",
                icon: "error",
                title: "این مقدار تعداد برای این محصول موجود نمی باشد",
                showConfirmButton: false,
                timer: 1500
            })
        }
    })

}