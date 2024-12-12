
import axios from "axios";


function ProductInput() {

    const subHandler = (event) => {
        event.preventDefault();
        axios.post(`http://127.0.0.1:8000/add_product?name=${event.target[0].value}&price=${event.target[1].value}`)
        location.reload();
    }

    return (
        <div className='main'>
            <h1>Добавить товар</h1>
            <form id="orderForm" onSubmit={subHandler}>
                <label>Название товара:</label>
                <input type="text" id="productName" name="productName" required/><br/>
                
                <label>Цена:</label>
                <input type="text" id="productPrice" name="productPrice" required/><br/>
                
                <input type="submit" value="Отправить"/>
            </form>
        </div>
    )
}

export default ProductInput