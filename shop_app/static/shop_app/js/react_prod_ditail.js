
class App extends React.Component{
    constructor() {
        super();
        // помогает обращаться (запускат методы у себя из класса react.component)
        this.state = {  // state состояние глобальня память
            products: [],
            products_pagin: [],
            products_edit: [],
            products_filtr_price: [],
            products_search: [],
            category: [],
            search_input_state: [],
            down_up: 'Выберете вариант',
            sort_categor_drop: 'Категорию',
            min_price: 100,
            max_price: 59999999999,
            orig_min_price: 100,
            orig_max_price: 59999999999,
            text_null_search: '',
            drop_categ: '',
            gener_array: [],
            count_page: 0

        }
    }

    buttonOne(price, name_click){
        // сортируем по стоимости используем this.state.products;
        // alert(name_click)
        this.setState({down_up:name_click}) // отловили что было нажато и записано в стейте
        if(price == '1'){
            let tmpTovars = this.state.products;
            this.sortTovars(tmpTovars)  // обращаемся к функции сортируем товары по возростаниюи цены применяем к функции
            this.setState({products:tmpTovars}) // перезаписываем пересортированные товары по ворзстанию в стейт
        }if(price == '2'){
            let tmpTovars = this.state.products;
            this.sortTovarsDown(tmpTovars)
            this.setState({products:tmpTovars})
        } if(price == '3'){
            let tmpTovars = this.state.products;
            this.sortName(tmpTovars)
            this.setState({products:tmpTovars})
        }if(price == '4'){
            let tmpTovars = this.state.products;
            this.sortNameDown(tmpTovars)
            this.setState({products:tmpTovars})
        }
    }
//this.setState({sort_categor_drop:cat_names_state})
    //, cat_names_state
    buttonTwo(category, cat_names_state){
        // сортируем по категориям используем this.state.products_edit;
        this.setState({sort_categor_drop:cat_names_state}) // название категории которое прилетело из button записалм в стейт
        this.setState({drop_categ: category}) // id категории которое прилетело из button записалм в стейт

        if(category == '0'){ // если значение которое прилетело из button равно 0, значит все категи записалм в стейт
            // для вывода в шаблон
            let products_def = this.state.products_edit;
            this.setState({products:products_def})
        }if(category > '0'){ // если значение которое прилетело из button больше 0
            let category_one_push = [] // создаем перменную с пустым массивом
            for(let ii=0; ii<this.state.products_edit.length; ii++){ // здесь перебираем массив из апи базы данных
                if (this.state.products_edit[ii].category == category){ // сравниваем массив пр срезу перебора из цикла и значение category который прилетает при нажатии

                    category_one_push.push(this.state.products_edit[ii]) // пушим по срезу индентификатора в цикле, т.е то что совпало в массиве при переборе фором и приравненое выше category
                }
            }
            this.setState({products:category_one_push}) // перезаписываем выбранные товары в стейт, для вывода в шаблон

        }
    }
    //сортируем товары по возростанию
    sortTovars(itemTovars){ //создаем переменную в ней сортируем массив
        //сортировка массива от меньшего к большему
        itemTovars.sort(function(a, b){
            // функция сортировка, перебирает весь массив
            // когда стоимость товара больше стоимости второго
            // вывести 1  иначе вывести -1
            if (Number(a.price) > Number(b.price)){
                return 1;
            }else {
                return -1;
            }
        });
    }

    //сортируем товары по убыванию цены
    sortTovarsDown(itemTovars){
        itemTovars.sort(function (a, b) {
            if(Number(a.price) < Number(b.price)){
                return 1;
            }else{
                return -1;
            }
        })
    }

    sortName(itemTovars){
        itemTovars.sort(function (a, b) {
            if (a.goodsname > b.goodsname){
                return 1;
            }else {
                return -1;
            }

        });
    }
    sortNameDown(itemTovars){
        itemTovars.sort(function (a, b){
            if(a.goodsname < b.goodsname){
                return 1;
            }else {
                return -1;
            }
        })
    }

//[A-Za-zА-Яа-яЁё]
    ///^\d+$/ цифры
    // event.target.value != '' && event.target.value == Number

    sortPriceMin(event){
        // сортируем по введенному значению, в поле мин стоимости
        event.target.value = event.target.value.replace(/[^0-9]/g, ""); // запрет ввода букв

        if (event.target.value.length > 9) { // запрещаем ввод больше 9 символов в поле минимальной цены
            event.target.value = event.target.value.substring(0, 9); // записываем в значение поля, значение без букв и 0 до 9 символов

        }

        let tmp_min_cprice = this.state.orig_min_price
        if (Number(event.target.value) < this.state.orig_min_price){ // если значение введёного меньше значения по умолчанию
            this.setState({min_price:tmp_min_cprice}) // тогда записываем в стейт значение по умолчанию из стейта
        }

        else{
            console.log("else_min")
            this.setState({min_price:Number(event.target.value)}) // если значение больше, тогда записываем в стейт значение из инпута
        }
    }
    sortPriceMax(event){
        event.target.value = event.target.value.replace(/[^0-9]/g, "");// запрет ввода букв
        if (event.target.value.length > 9) {// запрещаем ввод больше 9 символов в поле минимальной цены
            event.target.value = event.target.value.substring(0, 9);// записываем в значение поля, значение без букв и 0 до 9 символов
        }

        let ev_targ = event.target.value // значение введёного в поле инпута
        let tmp_max_cprice = this.state.max_price // значение по умолчанию из стейта
        if (Number(ev_targ) > Number(this.state.orig_max_price)){ // если значение из инпута больше из зеначения из стейта
            // event.target.value = Number(this.state.max_price)
            this.setState({max_price:tmp_max_cprice}) // тогда записываем в стейт значение по умолчанию из стейта
        }else {
            this.setState({max_price:event.target.value}) // если меньше тогда заносим в стейт значение по умолчанию из стейта
        }
    }

    filtrPrice(){
        //фильтруем по цене из инпутов

        // совместная функция, которая содержит отфильтованные товары по категориии и мин и макс цене
        // let max_tmp_price = this.state.orig_max_price
        let max_tmp_price = this.state.orig_max_price
        // console.log(this.state.max_price.length)
        if(this.state.max_price.length == 0){
        this.state.max_price = max_tmp_price
        }
        this.setState({max_price:this.state.max_price})
        this.filterJointly()
    }

    updateInputValue(event){
        // записываем в стейт набранные данные в ипнпуте
        let search_input = event.target.value

        this.setState({search_input_state:search_input.toLowerCase()}) // приравниваем введеное в поле поиска слово к нижнему регстру
    }

    filterItems(event){
        // фильтруем товары или категори по записанными в стейт набранные данные в инпуте
        // console.log('1')
        // console.log(this.state.products_search)
        let final_array_search = []
        // let tmpTovars = this.state.products_edit;
        for (let n=0; n<this.state.products_search.length; n++){

        var lower_case = this.state.products_search[n].goodsname.toLowerCase() // приравниваем название товара из базы к нижнему регистру

        if (lower_case.indexOf(this.state.search_input_state) >= 0 || this.state.products_search[n].category_choices.indexOf(this.state.search_input_state) >= 0 ){ //
            // здесь сравниваем выгрузку и введеное в поле поиска слово к нижнему регистру
            final_array_search.push(this.state.products_search[n]) // если условие совпадает, пушим

            }
        }
        if (final_array_search.length == 0){ // если поле пустое
            this.state.text_null_search = 'Товары не найдены, попробуйте еще раз!!!'
        }
        this.setState({products:final_array_search})
    }

        filterJointly(){
                //совместный фильтр по категориям и цене
            //this.filtrPrice() // фильтр по цене
            var filtr_tmp_array = this.state.products_filtr_price; // значение из стейта. в котором вся выгрузка из апи
            let category_one_push = [] // пустой массив
            if(this.state.drop_categ == '0'){ // если категория 0
                let products_def = filtr_tmp_array;  // тогда заносим все товары этой категи в переменную
                this.setState({products:products_def}) // и в стейт для прорисовки на странице тваров
                // console.log('1')

            }if(this.state.drop_categ > '0'){ // если id категории больше 0
                // console.log('2')

                for(let ii=0; ii<filtr_tmp_array.length; ii++){ // тогда здесь перебираем массив из апи
                    if (filtr_tmp_array[ii].category == this.state.drop_categ){ // сравниваем два массива пр срезу перебора из цикла и id category который прилетает при нажатии

                        category_one_push.push(filtr_tmp_array[ii]) // пушим по срезу индентификатора в цикле, т.е совпало в массиве при переборе фором с тем что прилетело, выше
                    }
                }

                let final_array = [] // создаем для пуша переменую с масивом
                for (let p=0; p<category_one_push.length; p++){ // перебираем запушеные отсортированные по id категории товары циклом для отсортировки по введеному значению цены в инпуте
                    // console.log('max_price_new')
                    // console.log(this.state.max_price)
                    if(Number(category_one_push[p].price) >= Number(this.state.min_price) && Number(category_one_push[p].price) <= Number(this.state.max_price)){ // сравниваем цену товара
                        // отсортирванную по категориям и минимальную цену
                        // и цену товара отсортирванную по категориям и максимальную цену
                        final_array.push(category_one_push[p]) // когда эти условия совпадают, тогда пушим для создания ключ

                    }
                }

                this.setState({products:final_array}) // и заносим в стейт для прорисовки в шаблоне
            }
        }

    paginProd(num_pagin, event){

        // let tmp_gener_array = this.state.gener_array(0, 6)
        // let start = 0
        // let end = 6
        let step = 6
        // let x_end = (step * num_pagin) - 5
        let xstart = 0
        let xend = 0
        // let all_pages = (this.state.products_pagin.length/6).toFixed()
        for (let i=0; i<num_pagin; i++){
            // console.log('num_pagin')
            // console.log(num_pagin)
            // console.log('actiual-1')
            // console.log(xstart)
            // console.log(xend)
            xstart = xend //xstart счетчик номер стартового эллемента массива
            xend = xend + step //xend счетчик последнего эллемента массива
            console.log('actiual-2')
            console.log(xstart)
            console.log(xend)
        }
        let tmp_gener_array = this.state.products_pagin.slice(xstart, xend) // слайсом ограничиваем начало и конец по номеру нажатого
        this.setState({gener_array: tmp_gener_array})

        // if (event.target.innerHTML == '1'){
        //     let tmp_gener_array = this.state.products_pagin.slice(0, 6)
        //     this.setState({gener_array: tmp_gener_array})
        //     // console.log('this.state.gener_array-1')
        //     // console.log(this.state.gener_array)
        // }
        // if (event.target.innerHTML == '2'){
        //     let tmp_gener_array = this.state.products_pagin.slice(7, 13)
        //     this.setState({gener_array: tmp_gener_array})
        //     console.log('this.state.gener_array-2')
        //     console.log(this.state.gener_array)
        // }
        // if (event.target.innerHTML == '3'){
        //     let tmp_gener_array = this.state.products_pagin.slice(14, 20)
        //     this.setState({gener_array: tmp_gener_array})
        //     console.log('this.state.gener_array-2')
        //     console.log(this.state.gener_array)
        // }

        // this.setState({gener_array: tmp_gener_array})
        // console.log(animals.slice(2, 4));
    }



    productsApi(json){ // в одной функции делаем 2 задания во время фетча, т.е одну и ту же выборку назначаем двум переменным
        this.setState({products:json}) //
        this.setState({products_edit:json})
        this.setState({products_filtr_price:json})
        this.setState({products_search:json})
        this.setState({products_pagin:json})//передаем в формате json в функцию
        this.setState({gener_array:json.slice(0, 6)}) //пердаем в формате json в функцию, слайсом выбираем первые 6 товаров для первой страница

        // console.log('products_edit')
        //
        // console.log(this.state.products_edit, this.state.products)
    }
    componentDidMount(){
        // console.log('hello_comp-2')
        // let products_pagin_len = this.state.products_pagin
        // console.log('products_pagin_len')
        // console.log(products_pagin_len)

    // GET Request.
        fetch('http://127.0.0.1:8800/api')
            // Handle success
            .then(response => response.json())  // convert to json
            .then(json => this.productsApi(json))    //   //пердаем в фомате json в функцию
            // .then(json => this.mySetArray.bind(this, json))

        fetch('http://127.0.0.1:8800/api/category')
            // Handle success
            .then(responsec => responsec.json())  // convert to json
            .then(json => this.setState({category:json}))

            //.then(json => this.setState({products:json}))    //print data to console
            // .then(data2 => this.setState({products_pagin:data2}))
            //  let products_pagin = gener_array.slice(0, 6)
            // console.log('1223')
            // console.log(products_pagin)

            // .then(my_categ_state => console.log(this.state.category))
        // console.log('2')
        // console.log(this.state.category)
}

    /*<!-- выведем даные из сайта: -->*/
    render() {//  render зарезервированное имя в реакте выводит даные{
        let count_page_var = (this.state.products_pagin.length/6).toFixed() // получаем количество страниц по 6 товаров .toFixed() округляет в большую
        // this.setState({count_page: count_page_var})
        let pag_array = []
        for (let i = 1; i<=count_page_var; i++){ //перебираем циклом и получаем количество страниц
            // console.log('count_page_var-i')
            // console.log(i)
            pag_array.push(i) // пушим чтоб сделать ключ значение, для передачи в шаблон
        }
        // console.log('pag_array')
        // console.log(pag_array)

        const pages = pag_array.map((item, index)=>{ //
            // let item_pagin = item
            // return <li key={index}>{item}<div>{item} $</div></li>

            return <li key={index} onClick={this.paginProd.bind(this, item)}><a>{item}</a></li>

            // <li><a href="#" onClick={this.paginProd.bind(this)}>&laquo;</a></li>

        });

        // let pagin= "{% paginate %}"
        let categories = this.state.category.map((item, index)=>{
            let cat_trues = item.cat_true
            let cat_names = item.catname
            // console.log('cat_true')
            // console.log(cat_trues)
            return <li key={index} onClick={this.buttonTwo.bind(this, cat_trues, cat_names)}><a href="#">{item.catname}</a>
            </li>

        });
        let myProducts = this.state.gener_array.map((item, index)=>{ //index внутрення нумерация, его менять нельзя, выводим товары на страницу gener_array
            let href_url = '/show/'+item.id
            let href_url_cart = "/shop_cart?i="+item.id+"&name="+item.goodsname+"&price="+item.price+"&img="+item.img

            return <div key={index}>
                {/*<div className="pagin-up">{pagin}</div>*/}
                <div className="item-panel product-grid-child">
                    <div className="row margin-hide">
                        <div className="col-md-4 col-sm-4 padding-left-hide">
                            <a data-rel="prettyPhoto" href="images/shop-2/1.png" title="Название товара" className="img-body-" />
                            <img src={item.img} alt="" className="img-responsive img-responsive-prod" />
                        </div>
                        <div className="col-md-8 col-sm-8 padding-right-hide">
                            <div className="offer-box">
                                <h3>-50%</h3>
                                <h3>Акция</h3>
                            </div><a href="#"><h3>Код:  {item.id}</h3></a>
                            <h4 className="goodsname-hide">{item.goodsname}</h4>
                            <h5>{item.price}</h5>
                            <p>{item.category_choices}</p>
                            <ul>
                                <li className="show-link"><a href={href_url}><span>Подробнее..</span></a><span className="fa fa-angle-right right-icon"></span>
                                </li>
                                <li className="add-to-card"><span className="fa fa-shopping-cart"><a href={href_url_cart}><span>В корзину</span></a></span>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

        });

        return <div>

            <section id="shop-list" className="shop-list-section top-sale-section">
                <div className="container container-filter">
                    <div className="row button-block">
                        <div className="col-md-12 col-md-12-prodlist">
                            <ul>
                                <li className="btn-group item-sort">
                                    <button type="button"  className="btn btn-default dropdown-toggle dropdown-toggle-heght" data-toggle="dropdown"><span className="pull-right"><i className="fa fa-angle-down" />
                                    </span>Сортировать: <span>{this.state.down_up}</span>
                                    </button>
                                    <ul className="dropdown-menu" role="menu">
                                        <li onClick={this.buttonOne.bind(this,1, 'По цене возростанию')}><a href="#">По цене возростание</a>
                                        </li>
                                        <li onClick={this.buttonOne.bind(this,2, 'По цене убыванию')}><a href="#">По цене убывание</a>
                                        </li>
                                        <li onClick={this.buttonOne.bind(this,3, 'По имени возростание')}><a href="#">По имени возростание</a>
                                        </li>
                                        <li onClick={this.buttonOne.bind(this,4, 'По имени убывание')}><a href="#">По имени убывание</a>
                                        </li>
                                    </ul>
                                </li>
                                {/*<li className="btn-group">*/}
                                {/*    <button type="button" className="btn btn-default top-icon"><i className="fa fa-arrow-up" />*/}
                                {/*    </button>*/}
                                {/*</li>*/}
                                <li className="btn-group item-categories">
                                    <button type="button" className="btn btn-default dropdown-toggle dropdown-toggle-my" data-toggle="dropdown">
                                        <span className="pull-right">
                                            <i className="fa fa-angle-down" /></span>Выбрать: <span>{this.state.sort_categor_drop}</span>
                                    </button>
                                    <ul className="dropdown-menu" role="menu">

                                        <li onClick={this.buttonTwo.bind(this,0,' Все')}><a href="#">Все</a>

                                        </li>

                                        {categories}

                                    </ul>
                                </li>

                                <li className="btn-group item-categories item-categories-my">
                                    <input className="input-search" type="search" onChange={this.updateInputValue.bind(this)}/>
                                    <button className="button-search" onClick={this.filterItems.bind(this)}>Искать</button>
                                </li>

                            </ul>

                        </div>
                    </div>
                    <div className="tab-content">
                        <div role="tabpanel" className="tab-pane fade in active shop-list-section" id="list">
                            <div className="row shop-list-row">
                                <div className="col-md-3 filter col-sm-3 col-sm-3-my">
                                    <div className="filter-price-box">
                                        <div className="filter-title">
                                            <h3>фильтр по цене</h3>
                                        </div>
                                        <ul className="filter-print-price my_filter-print-price">

                                            <input id="input_first" onChange={this.sortPriceMin.bind(this)} placeholder="мин цена"/>
                                            <input id="input_second" onChange={this.sortPriceMax.bind(this)} placeholder="максимальная цена"/>
                                            <li className="filter_price my_filter_price"><a href="#"><h4 onClick={this.filtrPrice.bind(this)}>фильтр</h4></a>
                                            </li>


                                        </ul>
                                    </div>

                                </div>
                                <div className="col-md-9 col-sm-9 col-md-9-my">
                                    {/**/}
                                    <div>
                                        {/*for goodss in goods %{'}'}*/}
                                        {/*start block*/}
                                        <div className="row">
                                            <div className="col-md-12 col-md-12-grid">
                                                {myProducts}
                                                <div className="text_null_search col-md-6">{this.state.text_null_search}</div>
                                            </div>
                                        </div>
                                        {/*endfor */}
                                    </div>
                                </div>
                                {/*end block*/}
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <nav>
                <ul className="pagination">
                    <li><a href="#" onClick={this.paginProd.bind(this)}>&laquo;</a></li>
                    <li><a href="#" onClick={this.paginProd.bind(this)}>1</a></li>
                    <li><a href="#" onClick={this.paginProd.bind(this)}>2</a></li>
                    <li><a href="#" onClick={this.paginProd.bind(this)}>3</a></li>
                    <li><a href="#" onClick={this.paginProd.bind(this)}>4</a></li>
                    <li><a href="#" onClick={this.paginProd.bind(this)}>5</a></li>
                    <li><a href="#">&raquo;</a></li>
                </ul>
            </nav>
            <ul className="pagination">
                <li><a href="#" onClick={this.paginProd.bind(this)}>&laquo;</a></li>
                    {pages}
                <li><a href="#">&raquo;</a></li>
            </ul>
        </div>;

    }
}

//  заливаем из виртуального дома при помощи обращения к айди
ReactDOM.render(
    <App/>,
    document.getElementById('app')
);
