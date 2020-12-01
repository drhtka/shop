
class App extends React.Component{
    constructor() {
        super();
        // помогает обращаться (запускат методы у себя из класса react.component)
        this.state = {  // state состояние глобальня память
            name : 'Ivan',
            years : 25,

        }
    }

componentDidMount(){
        console.log('hello_comp')

    $.ajax({
        url: 'http://127.0.0.1:8800/api',
        type: 'GET',
        // data: 'products',
        success: function (response){
            console.log('response')
            console.log(response)
        }
    })

//     // 1. Создаём новый объект XMLHttpRequest
//     var xhr = new XMLHttpRequest();
//
// // 2. Конфигурируем его: GET-запрос на URL 'phones.json'
//     xhr.open('GET', 'http://127.0.0.1:8800/api', true);
//
// // 3. Отсылаем запрос
//     xhr.send();
//
// // 4. Если код ответа сервера не 200, то это ошибка
//     if (xhr.status != 200) {
//         // обработать ошибку
//         alert( xhr.status + ': ' + xhr.statusText ); // пример вывода: 404: Not Found
//     } else {
//         // вывести результат
//         alert( xhr.responseText ); // responseText -- текст ответа.
//     }

}
    /*<!-- выведем даные из сайта: -->*/
    render() {//  render зарезервированное имя в реакте выводит даные
        return <div>
            <div>имя: {this.state.name}</div> возраст: {this.state.years}
        </div>;
    }
}

//  заливаем из виртуального дома при помощи обращения к айди
ReactDOM.render(
    <App/>,
    document.getElementById('app')
);
