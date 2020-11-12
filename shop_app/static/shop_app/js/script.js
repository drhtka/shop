// var book = {
// 	topic: "JS",
// };
//
// {
// 	alert(book.topic);
// }

// картинка при нажатии перепрыгивает наглавную
var active_photo = ''
function changeImg(mythis) {
	document.getElementsByClassName('main_img')[0].src = mythis.src // при нажатии записываем фотку в главное фото
	//alert(mythis.id) // id фоток
	active_photo = mythis // записываем в глобал перменную при клике картинку на которую мы кликнули
}
// var num = 0;
function newPrev(myThis){
	// alert('levo')
	if(active_photo.parentNode.previousElementSibling != null){  // ищу следующую картинку, если ее нет то стоп
		// если есть то идем дальше
		active_photo = active_photo.parentNode.previousElementSibling.childNodes[0] // записываем в глобал перменную при клике картинку к которой подошел клик слева
		document.getElementsByClassName('main_img')[0].src = active_photo.src
	}

}

function newNext(myThis){
	alert('123')
	console.log(active_photo)
	// console.log('active_photo')
	// console.log(active_photo)
	// console.log(active_photo.parentNode.nextElementSibling)

	if(active_photo.parentNode.nextElementSibling != null ){
		active_photo = active_photo.parentNode.nextElementSibling.childNodes[0] // ложим ту картинку к которой подошёл клик
		document.getElementsByClassName('main_img')[0].src = active_photo.src // ложим ту картинку до которй дошел фокус
	}

}

// var num = 0;
// function newNext() {
// 	var slider = document.getElementById('slider');
// 	num++;
// 	if(num >= images.length) {
// 		num = 0;
// 	}
// 	slider.src = images[num];
// 	document.getElementsByClassName('main_img')[0].src = images[num]
// 	//alert(images[num])
// }
//
// function newPrev() {
// 	var slider = document.getElementById('slider');
// 	num--;
// 	if(num < 0) {
// 		num = images.length-1;
// 	}
// 	slider.src = images[num];
// 	document.getElementsByClassName('main_img')[0].src = images[num]
// }


// var tmp_my_arr = []
// console.log('active_photo')
// console.log(active_photo)
// for (my_item of [active_photo]){
// 	console.log('my_item')
// 	console.log(my_item)
// 	tmp_my_arr.push(my_item)
// 	console.log('tmp_my_arr')
// 	console.log(tmp_my_arr[0].src)
// 	// tmp_my_arr = tmp_my_arr.slace(0)
// 	// console.log(tmp_my_arr.slace(0))
//
// }
// // console.log('0')
// // console.log(active_photo.src)
// // tmp_my_arr.push(active_photo.src)
// // console.log('0.5')
// // console.log(tmp_my_arr)
// // active_photo.src = tmp_my_arr
// console.log('1')
// console.log(active_photo.src)