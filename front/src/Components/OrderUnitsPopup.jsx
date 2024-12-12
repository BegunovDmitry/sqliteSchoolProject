import { useQuery } from "@tanstack/react-query"
import axios from "axios";

import OrderUnitsInput from "./OrderUnitsInput";


const getOrderUnitsData = (order_id) => {
    return axios.get(`http://127.0.0.1:8000/get_all_order_units/${order_id}`)
}


const handleDelete = (order_id, product_id) => {
    const product_field = event.target.parentNode
    product_field.classList.add("deleted")
    axios.delete(`http://127.0.0.1:8000/delete_order_units/${order_id}/${product_id}`)
}


const handleClosePopup = () => {
    localStorage.setItem("popupView", "Invisible")
    localStorage.removeItem("popupOrderId")
    location.reload()
};


function OrderUnitsPopup(props) {

    if (props.order_id == "None") {
        return (
            <div className="popup deleted" id="popup">
                <div className='main'>
                    <button className="close-button" id="closeButton" onClick={handleClosePopup}>×</button>
                    <h1>No order chosen</h1>
                </div>
            </div>
        )
    }

    const {data, isLoading, isSuccess} = useQuery({
        queryKey: ["orderUnitsList"],
        queryFn: () => getOrderUnitsData(props.order_id),
        select: data => data.data
    })


    if (isLoading) {
        return <p>Loading....</p>
    }

    if (isSuccess) {

        const products = data.map((product) => 
                        <div className="customer" key={product.name}>
                            <div><strong>Товар:</strong> {product.name}, <strong>Кол-во:</strong> {product.amount}, <strong>Цена за 1шт:</strong> {product.cost}</div>
                            <button className="delNum" onClick={() => handleDelete(props.order_id, product.id)}>Удалить</button>
                        </div>
                        )
        if (localStorage.getItem("popupView") == "Visible") {
            return (
                <div className="popup" id="popup">
                    <div className='main'>
                        <button className="close-button" id="closeButton" onClick={handleClosePopup}>×</button>
                        <h1>Order ID: {props.order_id}</h1>
                        <div id="customerList">
                            {products}
                        </div>
                        <OrderUnitsInput order_id={props.order_id}/>
                    </div>
                </div>
            )
        }          
        return (
            <div className="popup deleted" id="popup">
                <div className='main'>
                    <button className="close-button" id="closeButton" onClick={handleClosePopup}>×</button>
                    <h1>Order ID: {props.order_id}</h1>
                    <div id="customerList">
                        {products}
                    </div>
                    <OrderUnitsInput order_id={props.order_id}/>
                </div>
            </div>
        )
    }
}

export default OrderUnitsPopup