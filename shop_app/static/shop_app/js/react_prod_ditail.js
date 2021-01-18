
class App extends React.Component{
    constructor() {
        super();
        // помогает обращаться (запускат методы у себя из класса react.component)
        this.state = {  // state состояние глобальня память
            products: [],
            products_edit: [],
            products_filtr_price: [],
            products_search: [],
            category: [],
            search_input_state: [],
            down_up: 'Выберете вариант',
            sort_caregor_drop: 'Категорию',
            min_price: 100,
            max_price: 59999999999,
            orig_min_price: 100,
            orig_max_price: 59999999999,
            text_null_search: ''
        }
    }

    buttonOne(price, name_click){
        // сортируем по стоимости используем this.state.products;
        // alert(name_click)
        this.setState({down_up:name_click}) // отловили что было нажато и записано в стейте
        if(price == '1'){
            let tmpTovars = this.state.products;
            this.sortTovars(tmpTovars)
            this.setState({products:tmpTovars})
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
//this.setState({sort_caregor_drop:cat_names_state})
    //, cat_names_state
    buttonTwo(category, cat_names_state){
        // сортируем по категориям используем this.state.products_edit;
        this.setState({sort_caregor_drop:cat_names_state})

        if(category == '0'){
            let products_def = this.state.products_edit;
            this.setState({products:products_def})
        }if(category > '0'){
            let category_one_push = []
            for(let ii=0; ii<this.state.products_edit.length; ii++){ // здесь перебираем массив
                if (this.state.products_edit[ii].category == category){ // сравниваем два массива пр срезу перебора из цикла и category который прилетает при нажатии

                    category_one_push.push(this.state.products_edit[ii]) // пушим по срезу индентификатора в цикле, т.е совпавшено в массиве пр переборе фором
                }
            }
            this.setState({products:category_one_push})

        }
    }
    //сортируем товары по возростанию
    sortTovars(itemTovars){ //создаем переменную в ней сортируем массив
        //сортировка массива
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
        event.target.value = event.target.value.replace(/[^0-9]/g, ""); // запрет ввода букв

        if (event.target.value.length > 9) {
            event.target.value = event.target.value.substring(0, 9);
        }

        let tmp_min_cprice = this.state.orig_min_price
        if (Number(event.target.value) < this.state.orig_min_price){
            // console.log('if_min')
            // console.log('event_min')
            // console.log(Number(event.target.value))
            // console.log('min_price')
            // console.log(this.state.orig_min_price)
            // event.target.value = this.state.min_price
            this.setState({min_price:tmp_min_cprice})
        }

        else{
            console.log("else_min")
            this.setState({min_price:Number(event.target.value)})
        }
    }
    sortPriceMax(event){

        event.target.value = event.target.value.replace(/[^0-9]/g, "");

        if (event.target.value.length > 9) {
            event.target.value = event.target.value.substring(0, 9);
        }

        let ev_targ = event.target.value
        let tmp_max_cprice = this.state.max_price
        if (Number(ev_targ) > Number(this.state.orig_max_price)){
            // event.target.value = Number(this.state.max_price)
            this.setState({max_price:tmp_max_cprice})
        }else {
            this.setState({max_price:event.target.value})
        }


        console.log('max_price-2')
            console.log(this.state.max_price)
    }

    filtrPrice(){
        //фильтруем по цене из инпутов

        let final_array = []
        for (let p=0; p<this.state.products_filtr_price.length; p++){

            if(Number(this.state.products_filtr_price[p].price) > Number(this.state.min_price) && Number(this.state.products_filtr_price[p].price) < Number(this.state.max_price)){
                final_array.push(this.state.products_filtr_price[p])

            }
        }

        this.setState({products:final_array})

    }

    updateInputValue(event){
        // записываем в стейт набранные данные в ипнпуте
        let search_input = event.target.value
        console.log("search_input_state")
        console.log(search_input)
        this.setState({search_input_state:search_input})

    }

    filterItems(event){
        // фильтруем товары или категори по записанными в стейт набранные данные в инпуте
        // console.log('1')
        // console.log(this.state.products_search)
        let final_array_search = []
        // let tmpTovars = this.state.products_edit;
        for (let n=0; n<this.state.products_search.length; n++){
            console.log('name')
            console.log(this.state.products_search[n].category)

        if (this.state.products_search[n].goodsname.indexOf(this.state.search_input_state) >= 0 || this.state.products_search[n].category_choices.indexOf(this.state.search_input_state) >= 0 ){
            final_array_search.push(this.state.products_search[n])
            console.log('search_yes')
            console.log(this.state.products)
            }
        }
        if (final_array_search.length == 0){
            this.state.text_null_search = 'Товары не найдены, попробуйте еще раз!!!'
        }
        this.setState({products:final_array_search})
    }


    productsApi(json){ // в одной функции делаем 2 задания во время фетча, т.е одну и ту же выборку назначаем двум переменным
        this.setState({products:json}) //
        this.setState({products_edit:json})
        this.setState({products_filtr_price:json})
        this.setState({products_search:json})
        // console.log('products_edit')
        //
        // console.log(this.state.products_edit, this.state.products)
    }
    componentDidMount(){
        console.log('hello_comp-2')

    // GET Request.
        fetch('http://127.0.0.1:8800/api')
            // Handle success
            .then(response => response.json())  // convert to json
            .then(json => this.productsApi(json))    //print data to console

        fetch('http://127.0.0.1:8800/api/category')
            // Handle success
            .then(responsec => responsec.json())  // convert to json
            .then(json => this.setState({category:json}))
            //.then(json => this.setState({products:json}))    //print data to console

            // .then(my_categ_state => console.log(this.state.category))
        // console.log('2')
        // console.log(this.state.category)
}
    /*<!-- выведем даные из сайта: -->*/
    render() {//  render зарезервированное имя в реакте выводит даные{

        let categories = this.state.category.map((item, index)=>{
            let cat_trues = item.cat_true
            let cat_names = item.catname
            // console.log('cat_true')
            // console.log(cat_trues)
            return <li key={index} onClick={this.buttonTwo.bind(this, cat_trues, cat_names)}><a href="#">{item.catname}</a>
            </li>

        });
        let myProducts = this.state.products.map((item, index)=>{ //index внутрення нумерация, его менять нельзя
            let href_url = '/show/'+item.id
            let href_url_cart = "/shop_cart?i="+item.id+"&name="+item.goodsname+"&price="+item.price+"&img="+item.img
            return <div key={index}>

                <div className="item-panel">
                    <div className="row margin-hide">
                        <div className="col-md-4 col-sm-4 padding-left-hide">
                            <a data-rel="prettyPhoto" href="images/shop-2/1.png" title="Название товара" className="img-body-" />
                            <img src={item.img} alt="" className="img-responsive" />
                        </div>

                        <div className="col-md-8 col-sm-8 padding-right-hide">
                            <div className="offer-box">
                                <h3>-50%</h3>
                                <h3>Акция</h3>
                            </div><a href="#"><h3>Код:  {item.id}</h3></a>
                            <h4>{item.goodsname}</h4>
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
                <div className="container">
                    <div className="row button-block">
                        <div className="col-md-12">
                            <ul>

                                <li className="btn-group item-sort">
                                    <button type="button"  className="btn btn-default dropdown-toggle" data-toggle="dropdown"><span className="pull-right"><i className="fa fa-angle-down" />
                                    </span>Сортировать: <span>{this.state.down_up}</span>
                                    </button>
                                    <ul className="dropdown-menu" role="menu">
                                        <li onClick={this.buttonOne.bind(this,1, 'По цене возростание')}><a href="#">По цене возростание</a>
                                        </li>
                                        <li onClick={this.buttonOne.bind(this,2, 'По цене убывание')}><a href="#">По цене убывание</a>
                                        </li>
                                        <li onClick={this.buttonOne.bind(this,3, 'По имени возростание')}><a href="#">По имени возростание</a>
                                        </li>
                                        <li onClick={this.buttonOne.bind(this,4, 'По имени убывание')}><a href="#">По имени убывание</a>
                                        </li>
                                    </ul>
                                </li>
                                <li className="btn-group">
                                    <button type="button" className="btn btn-default top-icon"><i className="fa fa-arrow-up" />
                                    </button>
                                </li>
                                <li className="btn-group item-categories">
                                    <button type="button" className="btn btn-default dropdown-toggle" data-toggle="dropdown">
                                        <span className="pull-right">
                                            <i className="fa fa-angle-down" /></span>Выбрать: <span>{this.state.sort_caregor_drop}</span>
                                    </button>
                                    <ul className="dropdown-menu" role="menu">

                                        <li onClick={this.buttonTwo.bind(this,0,' Все')}><a href="#">Все</a>

                                        </li>

                                        {categories}

                                    </ul>
                                </li>

                                <li className="btn-group item-categories">
                                    <input type="search" onChange={this.updateInputValue.bind(this)}/>
                                    <button onClick={this.filterItems.bind(this)}>Искать</button>
                                </li>

                            </ul>

                        </div>
                    </div>
                    <div className="tab-content">
                        <div role="tabpanel" className="tab-pane fade in active shop-list-section" id="list">
                            <div className="row">
                                <div className="col-md-3 filter col-sm-3">
                                    <div className="filter-price-box">
                                        <div className="filter-title">
                                            <h3>фильтр по цене</h3>
                                        </div>
                                        <ul className="filter-print-price">

                                            <input onChange={this.sortPriceMin.bind(this)} placeholder="мин цена"/>
                                            <input onChange={this.sortPriceMax.bind(this)} placeholder="максимальная цена"/>
                                            <li className="filter_price"><a href="#"><h4 onClick={this.filtrPrice.bind(this)}>фильтр</h4></a>
                                            </li>


                                        </ul>
                                    </div>
                                    //left filter
                                    <div className="filter-category-box">
                                        <div className="filter-title">
                                            <h3>Категории</h3>
                                        </div>
                                        {/*for category_on_goods_s in category_on_goods*/}
                                        <div className="panel-group" id="accordion" role="tablist">
                                            <div className="panel panel-default">
                                                <div className="panel-heading">
                                                    // <h4 className="panel-title"><a href="sort_goods_categ?i=category_on_goods_s.0"><span className="counting-box">13</span> <span className="panel-title">{/*category_on_goods_s.1*/}</span></a></h4>
                                                </div>
                                            </div>
                                        </div>
                                        {/*endfor*/}
                                    </div>
                                    //left filter
                                </div>
                                <div className="col-md-9 col-sm-9">
                                    {/**/}
                                    <div>
                                        {/*for goodss in goods %{'}'}*/}
                                        {/*start block*/}
                                        <div className="row">
                                            <div className="col-md-12">
                                                {myProducts}
                                                {this.state.text_null_search}

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

        </div>;
    }
}

//  заливаем из виртуального дома при помощи обращения к айди
ReactDOM.render(
    <App/>,
    document.getElementById('app')
);
