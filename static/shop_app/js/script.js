// var book = {
// 	topic: "JS",
// };
//
// {
// 	alert(book.topic);
// }


var active_photo = document.getElementsByClassName('img_small')[0] // обращаемся к первой фотке списка маленьких фото
// при загрузке страницы
// изначально в этой глобальной переменной должна быть
// картинка при нажатии перепрыгивает наглавную
function changeImg(mythis) {
	document.getElementsByClassName('main_img')[0].src = mythis.src // при нажатии записываем фотку в главное фото
	//alert(mythis.id) // id фоток
	//active_photo = mythis // записываем в глобал перменную при клике картинку на которую мы кликнули
}
// var num = 0;
function newPrev(myThis){
	if(active_photo.parentNode.previousElementSibling != null){  // ищу следующую картинку, если ее нет то стоп
		// если есть то идем дальше
		active_photo = active_photo.parentNode.previousElementSibling.childNodes[0] // записываем в глобал переменную при клике картинку к которой подошел клик слева
		document.getElementsByClassName('main_img')[0].src = active_photo.src
	}

}

function newNext(myThis){

	if(active_photo.parentNode.nextElementSibling != null ){
		active_photo = active_photo.parentNode.nextElementSibling.childNodes[0] // ложим ту картинку к которой подошёл клик
		document.getElementsByClassName('main_img')[0].src = active_photo.src // ложим ту картинку до которй дошел фокус
	}

}
// слайдер на индексной в футере
var first_push_image = document.getElementsByClassName('my-src')[0] // равна нажатой фотографии
function openModall(mythis) {

	document.getElementsByClassName('img_modal')[0].src = mythis.src
	$('#exampleModal').modal('show') // query запуск по id при нажати на фото
	document.getElementsByClassName('modal-open')[0].style.paddingRight = '0px'
	// console.log(modal('show'))
	document.getElementById('exampleModal').style.top = '20%'
	//document.getElementsByClassName('myModal')[0] = document.getElementsByClassName('my-src')[0].src
	first_push_image = mythis


}
// предыдущую фотграфию при клике заносим в модалку
function indexPrev(myThis){

	if(first_push_image.parentNode.previousElementSibling != null ) { // если сосед родитель нажатой фотографии и его вложенности не равна нулю

		first_push_image = first_push_image.parentNode.previousElementSibling.firstElementChild // тогда перзаписываем то фоо которое нажато
		document.getElementsByClassName('img_modal')[0].src = first_push_image.src // записываем и показываем в модалке
	}

}

function indexNext(myThis){

	if(first_push_image.parentNode.nextElementSibling != null ) {
		first_push_image = first_push_image.parentNode.nextElementSibling.firstElementChild
		document.getElementsByClassName('img_modal')[0].src = first_push_image.src

	}

}

//корзина

	function plus(mythis, productName){ // из функции plus идём от this по дому к единице .value) + 1

		if (Number(mythis.previousElementSibling.value < 10)) {

	// {#var plusOne = Number(thisplus.previousElementSibling.innerHTML)#}
	// console.log(mythis)
	// console.log('mythis')
	// console.log(mythis.previousElementSibling.value)
		var plusOne = Number(mythis.previousElementSibling.value) + 1 // для прорисовки в шаблоне увеличение на один каждое нажатие
			// console.log('+1')
			// console.log(plusOne)
	// 		console.log('84')
	// console.log(mythis.previousElementSibling.value)
	// console.log(mythis.parentNode.parentNode.previousElementSibling.childNodes[1].innerHTML)
	// 		console.log('summ')
	// console.log(mythis.parentNode.parentNode.nextElementSibling.childNodes[1].innerHTML)
	// console.log(mythis)
	// 		console.log('mythis.parentNode')
	// 		console.log(mythis.parentNode.parentNode.previousElementSibling)
			// console.log(mythis.parentNode.previousElementSibling.childNodes[1].innerHTML)
	// {#console.log(productName)#}
	// {#console.log(productId)#}
		var first_price_plus = mythis.parentNode.parentNode.previousElementSibling.childNodes[1].innerHTML // начальная цена одного товара
			// console.log('innerHTML')
			// console.log(first_price_plus)
			// console.log(mythis.parentNode.parentNode.nextElementSibling.childNodes[1])
		// console.log('first_price_plus')
		// console.log(first_price_plus)
			console.log('number')
			console.log(Number(document.getElementsByClassName('main_summ')[0].innerHTML))
		document.getElementsByClassName('main_summ')[0].innerHTML = Number(document.getElementsByClassName('main_summ')[0].innerHTML) + Number(first_price_plus) // к общей сумме пр нажатиии на плюсик
		// приплюсовывается начальная цена одного товара
			$.ajax({
				url: '/final_order',
				type: 'get',
				data: {name: productName},
				success: function (response) { // в респонсе прилетает общая сумма количство нажатий  умноженное на цену товара
				// console.log('response')
				// console.log(response)
				mythis.parentNode.parentNode.nextElementSibling.childNodes[1].innerHTML = response // записываем общую сумма
				$('#bloc_content').html(response)
			}
		})
		mythis.previousElementSibling.value = plusOne // для прорисовки в шаблоне увеличение на один каждое нажатие
		// console.log('value')
		// console.log(mythis.previousElementSibling.value)
	}
}

	function minus(mythis, productName, productId){
		console.log('minu')
		if (Number(mythis.nextElementSibling.value > 1)) {

		var minusOne = Number(mythis.nextElementSibling.value) - 1
			console.log('minusOne')
			console.log(minusOne)
		var first_price = mythis.parentNode.parentNode.previousElementSibling.childNodes[1].innerHTML // здесь цена за штуку товара

		$.ajax({
			url: '/final_order',
			type: 'get',
			data: {prodid: productId},
			success: function (response) {
			console.log('resp_minus')
			console.log(response)
				console.log(mythis.parentNode.parentNode.nextElementSibling.childNodes[1].innerHTML)
			mythis.parentNode.parentNode.nextElementSibling.childNodes[1].innerHTML = response
			$('#bloc_content').html(response)
		}
})
	mythis.nextElementSibling.value = minusOne
			// console.log('mythis.nextElementSibling.value')
			// console.log(mythis.nextElementSibling.value)
			// console.log('first_price')
			// console.log(first_price)
			console.log('111')
			console.log(document.getElementsByClassName('main_summ'))
			console.log(document.getElementsByClassName('main_summ')[0].innerHTML)
	//alert(first_price)
		document.getElementsByClassName('main_summ')[0].innerHTML = document.getElementsByClassName('main_summ')[0].innerHTML - first_price// гланая сумма внизу
		//console.log(mythis.nextElementSibling.value)
	}
}

