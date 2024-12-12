import { useQuery } from "@tanstack/react-query"
import axios from "axios";


const getOrdersData = () => {
    return axios.get(`http://127.0.0.1:8000/get_all_orders`)
}

const handleDelete = (event) => {
    const order_field = event.target.parentNode
    order_field.classList.add("deleted")
    const del_order_id = order_field.innerText.match(/ID:\s*(\d+)/)[1];
    axios.delete(`http://127.0.0.1:8000/delete_order/${del_order_id}`)
}

function OrderList() {

    const {data, isLoading, isSuccess} = useQuery({
        queryKey: ["ordersList"],
        queryFn: getOrdersData,
        select: data => data.data
    })


    if (isLoading) {
        return <p>Loading....</p>
    }

    if (isSuccess) {

        const orders = data.map((order) => 
                        <div className="customer orderUnit" key={order.order_id}>
                            <div><strong>ID:</strong> {order.order_id}, <strong>Имя пользователя:</strong> {order.user_name}, <strong>Дата:</strong> {order.order_date}, <strong>Адрес:</strong> {order.delivery_address}</div>
                            <button className="delNum" onClick={handleDelete}>Удалить</button>
                        </div>
                        )
        

        return (
            <div className='main'>
                <h1>Список заказов</h1>
                <div id="customerList">
                    {orders}
                </div>
            </div>
        )
    }
}

export default OrderList