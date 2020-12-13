
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
            console.log(response)
        }
    })


}
    /*<!-- выведем даные из сайта: -->*/
    render() {//  render зарезервированное имя в реакте выводит даные
        return <div>

            <section id="shop-list" className="shop-list-section top-sale-section">
                <div className="container">
                    <div className="row button-block">
                        <div className="col-md-12">
                            <ul>
                                <li className="pull-right">
                                    <ul className="nav nav-tabs" role="tablist">
                                        <li className="btn-group list view-type">Показать как:</li>
                                        <li className="btn-group list active" role="presentation"><a href="goods" title="Списком" role="tab" data-toggle="tab"><i className="fa fa-th-list" /></a>
                                        </li>
                                        <li className="btn-group grid" role="presentation"><a href="index" title="Сеткой"><i className="fa fa-th-large" /></a>
                                        </li>
                                    </ul>
                                </li>
                                <li className="btn-group item-sort">
                                    <button type="button" className="btn btn-default dropdown-toggle" data-toggle="dropdown"><span className="pull-right"><i className="fa fa-angle-down" /></span>Сортировать: <span>Выберите вариант</span>
                                    </button>
                                    <ul className="dropdown-menu" role="menu">
                                        <li><a href="#">По цене</a>
                                        </li>
                                        <li><a href="#">По популярности</a>
                                        </li>
                                        <li><a href="#">По дате</a>
                                        </li>
                                        <li><a href="#">По доставке</a>
                                        </li>
                                    </ul>
                                </li>
                                <li className="btn-group">
                                    <button type="button" className="btn btn-default top-icon"><i className="fa fa-arrow-up" />
                                    </button>
                                </li>
                                <li className="btn-group item-show">
                                    <button type="button" className="btn btn-default dropdown-toggle" data-toggle="dropdown"><span className="pull-right"><i className="fa fa-angle-down" /></span>Выводить: <span>по 12 товаров</span>
                                    </button>
                                    <ul className="dropdown-menu" role="menu">
                                        <li><a href="#">по 18 товаров</a>
                                        </li>
                                        <li><a href="#">по 24 товара</a>
                                        </li>
                                        <li><a href="#">ВСЕ</a>
                                        </li>
                                    </ul>
                                </li>
                                <li className="btn-group item-categories">
                                    <button type="button" className="btn btn-default dropdown-toggle" data-toggle="dropdown"><span className="pull-right"><i className="fa fa-angle-down" /></span>Выбрать: <span>категорию</span>
                                    </button>
                                    <ul className="dropdown-menu" role="menu">
                                        //for category_on_goods_s in category_on_goods
                                        <li><a href="sort_goods_categ?i=category_on_goods_s.0"> <span>category_on_goods_s.1</span></a>
                                            {'{'}#                                    <a href="#">Все</a>#{'}'}
                                        </li>
                                        //endfor
                                    </ul>
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
                                        <div className="nstSlider range" data-range_min={0} data-range_max={1500} data-cur_min={0} data-cur_max={150}>
                                            <div className="bar" />
                                            <div className="leftGrip"><span className="drag"><span className="leftLabel" /></span>
                                            </div>
                                            <div className="rightGrip"><span className="drag"><span className="rightLabel" /></span>
                                            </div>
                                        </div>
                                        <ul className="filter-print-price">
                                            <li><a href="#"><h4>фильтр</h4></a>
                                            </li>
                                            <li className="price"><span>Цена:</span> <span className="leftLabel" /> <span>-</span> <span className="rightLabel" />
                                            </li>
                                        </ul>
                                    </div>
                                    <div className="filter-category-box">
                                        <div className="filter-title">
                                            <h3>Категории</h3>
                                        </div>
                                        {/*for category_on_goods_s in category_on_goods*/}
                                        <div className="panel-group" id="accordion" role="tablist">
                                            <div className="panel panel-default">
                                                <div className="panel-heading">
                                                    <h4 className="panel-title"><a href="sort_goods_categ?i=category_on_goods_s.0"><span className="counting-box">13</span> <span className="panel-title">{/*category_on_goods_s.1*/}</span></a></h4>
                                                </div>
                                            </div>
                                        </div>
                                        {/*endfor*/}
                                    </div>
                                </div>
                                <div className="col-md-9 col-sm-9">
                                    {/**/}
                                    <div>
                                        {/*for goodss in goods %{'}'}*/}
                                        {/*start block*/}
                                        <div className="row">
                                            <div className="col-md-12">
                                                <div className="item-panel">
                                                    <div className="row margin-hide">
                                                        <div className="col-md-4 col-sm-4 padding-left-hide">
                                                            <a data-rel="prettyPhoto" href="images/shop-2/1.png" title="Название товара" className="img-body-" />
                                                            <img src="goodss.4" alt="" className="img-responsive" />
                                                        </div>
                                                        <div className="col-md-8 col-sm-8 padding-right-hide">
                                                            <div className="offer-box">
                                                                <h3>-50%</h3>
                                                                <h3>Акция</h3>
                                                            </div><a href="#"><h3>{/*goodss.1*/}</h3></a>
                                                            <h4>{/*goodss.3р.*/}</h4>
                                                            <h5>{/*goodss.2*/}</h5>
                                                            <p>{/*goodss.5*/}</p>
                                                            <p className="ratings">
                                                                <input defaultValue={2} type="number" className="rating" min={0} max={5} step="0.5" data-size="xs" /><span> рейтинг товара</span>
                                                            </p>
                                                            <ul>
                                                                <li className="show-link"><a href="show?i=goodss.0"><span>Подробнее..</span></a><span className="fa fa-angle-right right-icon" />
                                                                </li>
                                                                <li className="add-to-card"><span className="fa fa-shopping-cart" /><a href="shop_cart?i=goodss.0&name=goodss.1&price=goodss.3&img=goodss.4"><span>В корзину</span></a>
                                                                </li>
                                                            </ul>
                                                        </div>
                                                    </div>
                                                </div>
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
