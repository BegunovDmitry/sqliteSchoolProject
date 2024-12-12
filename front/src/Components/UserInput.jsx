
import axios from "axios";


function UserInput() {

    const subHandler = (event) => {
        event.preventDefault();
        axios.post(`http://127.0.0.1:8000/add_user?name=${event.target[0].value}&email=${event.target[1].value}&address=${event.target[2].value}`)
        location.reload();
    }

    return (
        <div className='main'>
            <h1>Добавить заказчика</h1>
            <form id="orderForm" onSubmit={subHandler}>
                <label>Имя заказчика:</label>
                <input type="text" id="customerName" name="customerName" required/><br/>
                
                <label>Email заказчика:</label>
                <input type="email" id="customerEmail" name="customerEmail" required/><br/>
                
                <label>Адрес заказчика:</label>
                <input type="text" id="customerAddress" name="customerAddress" required/><br/>
                
                <input type="submit" value="Отправить"/>
            </form>
        </div>
    )
}

export default UserInput