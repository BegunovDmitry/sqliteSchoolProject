import { useQuery } from "@tanstack/react-query"

import axios from "axios";

const getUsersData = () => {
    return axios.get(`http://127.0.0.1:8000/get_all_users`)
}

function OrderInput() {

    const {data, isLoading, isSuccess} = useQuery({
        queryKey: ["usersList"],
        queryFn: getUsersData,
        select: data => data.data
    })

    const subHandler = (event) => {
        event.preventDefault();

        let chosen_user_id;

        data.forEach(element => {
            if (element.user_name == event.target[0].value) {        
                chosen_user_id = element.user_id
            }
        }); 

        axios.post(`http://127.0.0.1:8000/add_order?user_id=${chosen_user_id}&delivery_address=${event.target[1].value}`)
        location.reload();
    }

    if (isLoading) {
        return <p>Loading....</p>
    }


    if (isSuccess) {

        const users = data.map((user) => 
            <option value={user.user_name} key={user.user_id}/>
            )

        return (
            <div className='main'>
                <h1>Добавить заказ</h1>
                <form id="orderForm" onSubmit={subHandler}>
                    <label>Имя заказчика:</label>
                    <input type="text" id="ordererName" name="ordererName" list="options" required/><br/>
                    <datalist id="options">
                        {users}
                    </datalist>
                    
                    <label>Адрес доставки:</label>
                    <input type="text" id="orderAddress" name="orderAddress" required/><br/>
                    
                    <input type="submit" value="Отправить"/>
                </form>
            </div>
        )
    }
}

export default OrderInput