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
            down_up: 'Сортировать',
            sort_categor_drop: 'Категории',
            min_price: 100,
            max_price: 59999999999,
            orig_min_price: 100,
            orig_max_price: 59999999999,
            text_null_search: '',
            drop_categ: '',
            gener_array: [],
            count_page: 0,
            num_pagin_state: 0,
            batton_end: 'none',
            filtr_baton_price: 0,
            num_pagin_style: 0
        }
    }



buttonOne(price, name_click){
        // сортируем по стоимости используем this.state.products;
        // alert(price)
            if(this.state.num_pagin_state > 1){
                // console.log('сюда перенести услове из пагинации')
            }
        this.setState({down_up:name_click}) // отловили что было нажато и записано в стейте
        this.setState({filtr_baton_price: price})
        // console.log('filtr_baton_price')
        // console.log(this.state.filtr_baton_price)
        if(price == '1'){

            console.log('page-1')
            let tmpTovars = this.state.products_pagin;
            this.sortTovars(tmpTovars)  // обращаемся к функции сортируем товары по возростаниюи цены применяем к функции
            this.setState({products_pagin:tmpTovars}) // перезаписываем пересортированные товары пагинацией по ворзстанию в стейт
            // console.log('возр')
            // console.log(tmpTovars)

        }if(price == '2'){

            console.log('page-2')
            let step = 6
            // let x_end = (step * num_pagin) - 5
            let xstart = 0
            let xend = 0
            // console.log('this.state.num_pagin_state')
            // console.log(this.state.num_pagin_state)
            if (this.state.num_pagin_state == 0){
                this.state.num_pagin_state = 1
            }
            // let all_pages = (this.state..products_pagin.length/6).toFixed()
            if (this.state.num_pagin_state > 0){  // num_pagin_state  записвывается только при нажатии пагинации
                console.log('зашли в иф ')
                var mainTmpTovars = this.state.products_pagin
                this.sortTovarsDown(mainTmpTovars)
                console.log('mainTmpTovars-61')
                console.log(mainTmpTovars)
                this.setState({products_pagin: mainTmpTovars})
                this.setState({gener_array: mainTmpTovars})

            for (let i=0; i<this.state.num_pagin_state; i++) {
                xstart = xend //xstart счетчик номер стартового эллемента массива
                xend = xend + step //xend счетчик последнего эллемента массива, здесь мы задаем шаг в 6 товаров
            }
            console.log('xstart')
            console.log(xstart, xend)
            let tmpTovars = mainTmpTovars.slice(xstart, xend);
            // this.sortTovarsDown(tmpTovars)
                console.log('tmpTovars-2')
                // var my_tmp = this.sortTovarsDown(tmpTovars)
                console.log('tmpTovars')
                console.log(tmpTovars)
            // this.setState({gener_array:tmpTovars})
                this.setState({products_pagin:mainTmpTovars})
                //  alert(Math.ceil(mainTmpTovars.length / 6))// количество траниц
                this.setState({gener_array: mainTmpTovars})

                // console.log('this.state.products_pagin')
                // console.log(this.state.products_pagin)
            // this.setState({products_pagin:tmpTovars})
            }

        }if(price == '3'){
            // alert(price)
            let step = 6
            // let x_end = (step * num_pagin) - 5
            let xstart = 0
            let xend = 0
            // let all_pages = (this.state.products_pagin.length/6).toFixed()
            for (let i=0; i<price; i++) {
                xstart = xend //xstart счетчик номер стартового эллемента массива
                xend = xend + step //xend счетчик последнего эллемента массива, здесь мы задаем шаг в 6 товаров
            }
            console.log('page-3')
            console.log('xstart')
            console.log(xstart, xend)

            let tmpTovars = this.state.products_pagin;
            this.sortName(tmpTovars)
            this.setState({products_pagin:tmpTovars})

        }if(price == '4'){
            // alert(price)
            let tmpTovars = this.state.products_pagin;
            this.sortNameDown(tmpTovars)
            this.setState({products_pagin:tmpTovars})
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
            this.setState({gener_array:products_def})
            this.setState({products_pagin:products_def})
        }if(category > '0'){ // если значение которое прилетело из button больше 0
            let category_one_push = [] // создаем переменную с пустым массивом
            for(let ii=0; ii<this.state.products_edit.length; ii++){ // здесь перебираем массив из апи базы данных
                if (this.state.products_edit[ii].category == category){ // сравниваем массив пр срезу перебора из цикла и значение category который прилетает при нажатии

                    category_one_push.push(this.state.products_edit[ii]) // пушим по срезу индентификатора в цикле, т.е то что совпало в массиве при переборе фором и приравненое выше category
                }
            }
            this.setState({gener_array:category_one_push}) // перезаписываем выбранные товары в стейт, для вывода в шаблон первую страницу пагинации
            this.setState({products_pagin:category_one_push}) // перезаписываем выбранные товары в стейт, для вывода в шаблон, отфильтрованные страницы с пагинацией
            //
            // console.log('this.state.batton_end-74')
            // console.log(this.state.batton_end)
            var x = Math.ceil(this.state.products_pagin.length/6)-1
            // console.log('xx')
            // console.log(x)
            if(x>1){
                this.state.batton_end = 'inline-block'
                // console.log('inline-block')
            }else{
                this.state.batton_end = 'none'
            }
        }
    }
    //сортируем товары по возростанию
    sortTovars(itemTovars){ //создаем переменную в ней сортируем массив tmpTovars
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
        // alert('123')
        itemTovars.sort(function (a, b) {
            if(Number(a.price) < Number(b.price)){
                return 1;
            }else{
                return -1;
            }

        })
        // console.log('itemTovars')
        // console.log(itemTovars)
    }
    //сортируем товары по возрастанию имени
    sortName(itemTovars){
        itemTovars.sort(function (a, b) {
            if (a.goodsname > b.goodsname){
                return 1;
            }else {
                return -1;
            }

        });
    }
    //сортируем товары по убыванию имени
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
        this.setState({products_pagin:final_array_search})
    }
        filterJointly(){
                //совместный фильтр по категориям и цене
            //this.filtrPrice() // фильтр по цене
            // console.log('1')
            // console.log(this.state.products)
            // alert('test')
            var filtr_tmp_array = this.state.products_filtr_price; // значение из стейта. в котором вся выгрузка из апи
            let category_one_push = [] // пустой массив
            if(this.state.drop_categ == '0'){ // если категория 0

                let final_array = [] // создаем для пуша переменую с масивом
                for (let p=0; p<this.state.products.length; p++){ // перебираем запушеные отсортированные по id категории товары циклом для отсортировки по введеному значению цены в инпуте
                    // console.log('max_price_new')
                    // console.log(this.state.max_price)
                    if(Number(this.state.products[p].price) >= Number(this.state.min_price) && Number(this.state.products[p].price) <= Number(this.state.max_price)){ // сравниваем цену товара
                        // отсортирванную по категориям и минимальную цену
                        // и цену товара отсортирванную по категориям и максимальную цену
                        // console.log('p')
                        // console.log(this.state.products[p])
                        final_array.push(this.state.products[p]) // когда эти условия совпадают, тогда пушим для создания ключ
                    }
                }
                this.state.gener_array=final_array

            }if(this.state.drop_categ > '0'){ // если id категории больше 0
                // console.log('2')

                for(let ii=0; ii<this.state.products.length; ii++){ // тогда здесь перебираем массив из апи
                    if (filtr_tmp_array[ii].category == this.state.drop_categ){ // сравниваем два массива пр срезу перебора из цикла и id category который прилетает при нажатии
                        category_one_push.push(filtr_tmp_array[ii]) // пушим по срезу индентификатора в цикле, т.е совпало в массиве при переборе фором с тем что прилетело, выше
                    }
                }

                let final_array = [] // создаем для пуша переменую с масивом
                for (let p=0; p<this.state.products.length; p++){ // перебираем запушеные отсортированные по id категории товары циклом для отсортировки по введеному значению цены в инпуте
                    // console.log('max_price_new')
                    // console.log(this.state.max_price)
                    if(Number(this.state.products[p].price) >= Number(this.state.min_price) && Number(this.state.products[p].price) <= Number(this.state.max_price) && Number(this.state.products[p].category) == this.state.drop_categ){ // сравниваем цену товара
                        // отсортирванную по категориям и минимальную цену
                        // и цену товара отсортирванную по категориям и максимальную цену
                        // console.log('p')
                        // console.log(this.state.products[p])
                        final_array.push(this.state.products[p]) // когда эти условия совпадают, тогда пушим для создания ключ
                    }
                }
                this.state.gener_array=final_array

                this.allFilterPagin.bind(this, final_array)


                let my_tmp_array = []
                for( let my_item of this.state.products_pagin ){ // пербираем фором массив с продуктами в пагинаторе, чтобы сравнить цену для выборки
                    // console.log(Number(this.state.min_price), Number(this.state.max_price), my_item.price)
                    if(Number(my_item.price) > Number(this.state.min_price) && Number(my_item.price) < Number(this.state.max_price)){// сравниваем и то что остается пушим в перменую
                        // console.log('est')
                        // console.log(my_item.price)
                        my_tmp_array.push(my_item)
                        // console.log(my_tmp_array)
                    }
                }

                let count_page_var = Math.ceil(this.state.products_pagin.length/6) // получаем количество страниц по 6 товаров .toFixed() округляет в большую
                // console.log(count_page_var)
                this.setState({products_pagin:my_tmp_array})// запушеные товары пердаем для прорисвки в шаблоне с пагинацией
                // console.log('products')
                // console.log(this.state.products_pagin)
                // console.log(this.state.products)
                let tmp_gener_array = my_tmp_array.slice(0, 6) // слайсом ограничиваем начало и конец по номеру нажатого

                let pag_array = []
                for (let i = 1; i<=count_page_var; i++){ //перебираем циклом и получаем количество страниц
                    // console.log('count_page_var-i')
                    // console.log(i)
                    pag_array.push(i) // пушим чтоб сделать ключ значение, для передачи в шаблон
                }
                // console.log('gener_array-2end')
                // console.log(this.state.gener_array)
                this.setState({products_pagin: this.state.gener_array})
            }
            var x = Math.ceil(this.state.products_pagin.length/6)-1
            // console.log('xx')
            // console.log(x)
            if(x>1){
                this.state.batton_end = 'inline-block'
                // console.log('inline-block')
            }else{
                this.state.batton_end = 'none'
            }
            // this.allFilterPagin('hello-2')
        }

    paginProd(num_pagin, event){
        // alert('pagionation')
        // функция пагинаци при нажатии на кнопки пацинации

        console.log('num_pagin')
        console.log(num_pagin)

        for (var i=0; i<document.getElementsByClassName('current').length; i++ ){
            document.getElementsByClassName('current')[i].classList.remove('curr_page_number')
        }

        document.getElementsByClassName('current')[num_pagin].classList.add('curr_page_number')


        this.setState({num_pagin_state: num_pagin})
        let step = 6
        // let x_end = (step * num_pagin) - 5
        let xstart = 0
        let xend = 0
        // let all_pages = (this.state.products_pagin.length/6).toFixed()
        for (let i=0; i<num_pagin; i++){
            xstart = xend //xstart счетчик номер стартового эллемента массива
            xend = xend + step //xend счетчик последнего эллемента массива, здесь мы задаем шаг в 6 товаров
        }
        let final_array = [] // создаем для пуша переменую с масивом
        console.log('this.state.products-388')
        console.log(this.state.products)
        for (let p=0; p<this.state.products.length; p++){ // перебираем запушеные отсортированные по id категории товары циклом для отсортировки по введеному значению цены в инпуте
            // console.log('products')
            // console.log(this.state.products)
            // console.log('123')
            // console.log(this.state.category)
            // console.log(this.state.max_price)
            if(Number(this.state.products[p].price) >= Number(this.state.min_price) && Number(this.state.products[p].price) <= Number(this.state.max_price) && Number(this.state.products[p].category) == this.state.drop_categ){ // сравниваем цену товара
                // отсортирванную по категориям и минимальную цену
                // и цену товара отсортирванную по категориям и максимальную цену
                final_array.push(this.state.products[p]) // когда эти условия совпадают, тогда пушим для создания ключ
            }else{
                final_array.push(this.state.products[p]) // когда эти условия совпадают, тогда пушим для создания ключ
            }
        }

        // console.log('filtr_baton_price')
        // console.log(this.state.filtr_baton_price -1)
        this.state.filtr_baton_price -1
        if (this.state.filtr_baton_price == 0){
            this.sortTovars(final_array)  // обращаемся к функции сортируем товары по возростаниюи цены применяем к функции
            // console.log('price == 0')
            // console.log(final_array)
        }

        if (this.state.filtr_baton_price == 1){
            this.sortTovarsDown(final_array)  // обращаемся к функции сортируем товары по возростаниюи цены применяем к функции
            // console.log('price == 1')
            // console.log(final_array)
        }


        console.log('final_array-364')
        console.log(final_array)
        let tmp_gener_array = final_array.slice(xstart, xend) // слайсом ограничиваем начало и конец по номеру нажатого

        this.setState({gener_array: tmp_gener_array})
    }
        allFilterPagin(array){
            // функция пагинаци при нажатии на цифры пацинации
            console.log('array')
            console.log(array)
            let step = 6
            // let x_end = (step * num_pagin) - 5
            let xstart = 0
            let xend = 0
            // let all_pages = (this.state.products_pagin.length/6).toFixed()
            for (let i=0; i<1; i++){
                xstart = xend //xstart счетчик номер стартового эллемента массива
                xend = xend + step //xend счетчик последнего эллемента массива, здесь мы задаем шаг в 6 товаров
            }
            let tmp_gener_array = array.slice(xstart, xend) // слайсом ограничиваем начало и конец по номеру нажатого
            this.setState({gener_array: tmp_gener_array})
    }

    productsApi(json){ // в одной функции делаем 2 задания во время фетча, т.е одну и ту же выборку назначаем двум переменным
        this.setState({products:json}) //
        this.setState({products_edit:json})
        this.setState({products_filtr_price:json})
        this.setState({products_search:json})
        this.setState({products_pagin:json})//передаем в формате json в стейт
        this.setState({gener_array:json.slice(0, 6)}) //пердаем в формате json в стейт, слайсом выбираем первые 6 товаров для первой страница

        // console.log('products_edit')
        console.log('products_edit')
        //
        console.log(this.state.products_edit, this.state.products)
    }
    componentDidMount(){
        // console.log('hello_comp-2')
        // let products_pagin_len = this.state.products_pagin
        // console.log('products_pagin_len')
        // console.log(products_pagin_len)
    // GET Request.
        fetch('http://127.0.0.1/api')
            // Handle success
            .then(response => response.json())  // convert to json
            .then(json => this.productsApi(json))  // передаем в фомате json в функцию
            // .then(json => this.mySetArray.bind(this, json))

        fetch('/api/category')
            // Handle success
            .then(responsec => responsec.json())  // convert to json
            .then(json => this.setState({category:json}))
}


    /*<!-- выведем даные из сайта: -->*/
    render() {//  render зарезервированное имя в реакте выводит даные{
        // console.log('(this.state.products_pagin.length/6)Math.ceil')
        // console.log(Math.ceil(this.state.products_pagin.length/6))
        // console.log(this.state.products_pagin.length)


        let count_page_var = Math.ceil(this.state.products_pagin.length/6) // получаем количество страниц по 6 товаров Math.ceil() округляет в большую

        // this.setState({count_page: count_page_var})
        // console.log('products_pagin-396')
        // console.log(this.state.products_pagin)
        // console.log((this.state.products_pagin.length/6).toFixed())

        let pag_array = []
        // console.log('count_page_var')
        // console.log(count_page_var)
        for (let i = 1; i<=count_page_var; i++){ //перебираем циклом и получаем количество страниц
            // console.log('count_page_var-i')
            // console.log("i")
            // console.log(i)
            pag_array.push(i) // пушим чтоб сделать ключ значение, для передачи в шаблон
        }
        // console.log('pag_array')
        // console.log(pag_array)
        if (pag_array.length > 1 ){
           this.state.batton_end = 'inline-block'
        }
        const pages = pag_array.map((item, index)=>{ // item => num_pagin
            // let item_pagin = item
            // return <li key={index}>{item}<div>{item} $</div></li>
            return <a key={index} onClick={this.paginProd.bind(this, item)} className="pagination_react">
                <span className="current page pagination__link_state_active pagination__link ">{item}</span></a>
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
        // console.log('this.state.products_pagin')
        // console.log(this.state.products_pagin)
            let myProducts = this.state.gener_array.slice(0, 6).map((item, index)=>{ //index внутрення нумерация, его менять нельзя, выводим товары на страницу gener_array
            let href_url = '/show/'+item.id
            let href_url_cart = "/shop_cart?i="+item.id+"&name="+item.goodsname+"&price="+item.price+"&img="+item.img

            return <div key={index}>
                {/*<div className="pagin-up">{pagin}</div>*/}
                <div className="item-panel product-grid-child">
                    <div className="row margin-hide margin-hide-prod">
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

            <section id="shop-list" className="shop-list-section- top-sale-section-">
                <div className="container container-filter">
                    <div className="row button-block">
                        <div className="col-md-12 col-md-12-prodlist">
                            <ul>
                                <li className="btn-group item-sort">
                                    <button type="button"  className="btn btn-default dropdown-toggle dropdown-toggle-heght" data-toggle="dropdown"><span className="pull-right"><i className="fa fa-angle-down" />
                                    </span><span>{this.state.down_up}</span>
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
                                            <i className="fa fa-angle-down" /></span><span>{this.state.sort_categor_drop}</span>
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
            {/*<nav>*/}
            {/*    <ul className="pagination">*/}
            {/*        <li><a href="#" onClick={this.paginProd.bind(this)}>&laquo;</a></li>*/}
            {/*        <li><a href="#" onClick={this.paginProd.bind(this)}>1</a></li>*/}
            {/*        <li><a href="#" onClick={this.paginProd.bind(this)}>2</a></li>*/}
            {/*        <li><a href="#" onClick={this.paginProd.bind(this)}>3</a></li>*/}
            {/*        <li><a href="#" onClick={this.paginProd.bind(this)}>4</a></li>*/}
            {/*        <li><a href="#" onClick={this.paginProd.bind(this)}>5</a></li>*/}
            {/*        <li><a href="#">&raquo;</a></li>*/}
            {/*    </ul>*/}
            {/*</nav>*/}
            <div className="pagin-up pagination-react">
                <div className="pagination">
                    <a onClick={this.paginProd.bind(this, 1)} className="current page pagination__link_state_active pagination__link pagination_react"></a>
                        {pages}
                    <a onClick={this.paginProd.bind(this, 2)}  className="next pagination__link_state_active pagination__link line_null array pagination__link_index pagination_react" style={{'display': this.state.batton_end}}></a>

                </div>
            </div>
        </div>;

    }
}
// &laquo;  &raquo;
//  заливаем из виртуального дома при помощи обращения к айди
ReactDOM.render(
    <App/>,
    document.getElementById('app')
);
