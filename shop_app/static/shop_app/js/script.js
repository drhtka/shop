// var book = {
// 	topic: "JS",
// };
//
// {
// 	alert(book.topic);
// }

// картинка при нажатии перепрыгивает наглавную
var active_photo = document.getElementsByClassName('img_small')[0] // обращаемся к первой фотке списка маленьких фото
// при загрузке страницы
// изначально в этой глобальной переменной должна быть
function changeImg(mythis) {
	document.getElementsByClassName('main_img')[0].src = mythis.src // при нажатии записываем фотку в главное фото
	//alert(mythis.id) // id фоток
	active_photo = mythis // записываем в глобал перменную при клике картинку на которую мы кликнули
}
// var num = 0;
function newPrev(myThis){
	// alert('levo')
	// alert('newPrev')
	// console.log('active_photo.newPrev')
	// console.log(document.getElementsByClassName('img_small')[0])
	//active_photo =
	if(active_photo.parentNode.previousElementSibling != null){  // ищу следующую картинку, если ее нет то стоп
		// если есть то идем дальше
		active_photo = active_photo.parentNode.previousElementSibling.childNodes[0] // записываем в глобал перменную при клике картинку к которой подошел клик слева
		document.getElementsByClassName('main_img')[0].src = active_photo.src
	}

}

function newNext(myThis){
	// alert('newNext')
	// console.log(active_photo)
	// console.log('active_photo')
	// console.log(active_photo)
	// console.log(active_photo.parentNode.nextElementSibling)

	if(active_photo.parentNode.nextElementSibling != null ){
		active_photo = active_photo.parentNode.nextElementSibling.childNodes[0] // ложим ту картинку к которой подошёл клик
		document.getElementsByClassName('main_img')[0].src = active_photo.src // ложим ту картинку до которй дошел фокус
	}

}

