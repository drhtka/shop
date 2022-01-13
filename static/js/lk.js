function onclickMenu(){
    console.log('my-collapse')
    console.log(document.getElementsByClassName('my-collapse')[0].classList.contains('in'))
    if(document.getElementsByClassName('my-collapse')[0].classList.contains('in') == false || document.getElementsByClassName('my-collapse')[0].style.display == 'none' ){
        document.getElementsByClassName('my-collapse')[0].classList.add('in')
        document.getElementsByClassName('my-collapse')[0].style.display = 'block'
        document.getElementsByClassName('my-collapse')[0].style.visibility = 'visible'
    }
    else{
        document.getElementsByClassName('my-collapse')[0].classList.remove('in')

        document.getElementsByClassName('my-collapse')[0].style.display = 'none'
        document.getElementsByClassName('my-collapse')[0].style.visibility = 'hidden'

    }
}